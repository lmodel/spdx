#!/usr/bin/env python3
"""Render the SPDX 3 model, OWL and SHACL in Turtle, as LinkML schema modules.

The script reads the vendored model, ``src/spdx/schema/upstream/spdx-model.ttl``,
and writes one LinkML module per SPDX profile plus an umbrella into
``src/spdx/schema/``. Every YAML file in that folder is its output: change the
script, or the vendored model, and run it again.

Usage::

    uv run python scripts/spdx_to_linkml.py [--ttl FILE] [-d OUTPUT_DIR] [--check]

``--check`` writes to a temporary folder and exits 1 when the result differs
from what the output folder holds, so a test can tell a hand edit from a
regeneration.

The rules, each applied the same way to every element:

- An ``owl:Class`` whose individuals carry ``rdfs:label`` is an enum, and the
  labels are its permissible values; every other ``owl:Class`` is a class. The
  individuals without a label (NoAssertionElement, NoneElement,
  NoAssertionLicense, NoneLicense, SpdxOrganization) are instance data and are
  left out.
- A class's ``sh:property`` shapes are its fields. ``sh:class`` or
  ``sh:datatype`` is the range, falling back to the property's ``rdfs:range``;
  ``sh:minCount 1`` is ``required``; no ``sh:maxCount`` is ``multivalued``.
- A property one class uses is that class's attribute. A property two or more
  classes use is a top-level slot in the module of its namespace, carrying what
  every use agrees on, with ``slot_usage`` on a class only where it differs.
- The classes of ``sh:nodeKind sh:IRI`` are Element and its descendants, so
  Element carries the identifier ``spdxId`` and a reference to any Element is
  its IRI. The other classes have no identifier and are inlined where used.
- A ``sh:not [sh:hasValue <class>]`` shape on ``rdf:type`` marks the class abstract.
- The datatypes SPDX constrains with a pattern become LinkML types
  (``date_time_stamp``, ``media_type``, ``semver``), and xsd:positiveInteger
  and xsd:nonNegativeInteger become bounded integer types.
- Every element keeps its SPDX IRI, as ``class_uri``, ``slot_uri``,
  ``enum_uri`` or a value's ``meaning``, written as a CURIE under a prefix per
  profile. Names are SPDX's own; a property whose local name another profile
  also uses takes the SPDX JSON-LD context's key (``security_locator``).
- Extension and AnyLicenseInfo are declared in the core module, because Core's
  own fields range over them; their IRIs stay in their profiles' namespaces.
- ``type``, the ``rdf:type`` designator, is a slot of every class that has no
  parent. Its value is the class's CURIE, such as ``spdx_core:Hash``, so an
  inlined object says which IntegrityMethod it is.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

import rdflib.collection
import yaml
from rdflib import Graph, URIRef
from rdflib.namespace import OWL, RDF, RDFS, SH, XSD

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_TTL = ROOT / "src" / "spdx" / "schema" / "upstream" / "spdx-model.ttl"
DEFAULT_OUT = ROOT / "src" / "spdx" / "schema"

SCHEMA_ID = "https://w3id.org/lmodel/spdx"
OWN_PREFIX = "spdx_linkml"
OWN_NS = SCHEMA_ID + "/"
DOCS_SITE = "https://lmodel.github.io/spdx"
LICENSE = "Apache-2.0"
UMBRELLA = "spdx"
CORE = "spdx_core"

# The patterns the model puts on its datatypes, each declared once as a type.
DATE_TIME_PATTERN = r"^\d\d\d\d-\d\d-\d\dT\d\d:\d\d:\d\dZ$"
MEDIA_TYPE_PATTERN = r"^[^\/]+\/[^\/]+$"
SEMVER_PATTERN = (
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
    r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$"
)

# Each type names its base as well as its typeof, because the SQL generator reads the
# base from the type itself and does not follow typeof (linkml 1.12.1, linkml issue
# 3491). date_time_stamp is a string, not a datetime: the Python runtime writes a UTC
# datetime back as +00:00, which the type's pattern and SPDX's SHACL both reject.
TYPES = {
    "date_time_stamp": {
        "typeof": "string",
        "base": "str",
        "uri": "xsd:dateTimeStamp",
        "description": "A UTC timestamp as SPDX writes one: a date, a time to the second and a trailing Z.",
        "pattern": DATE_TIME_PATTERN,
    },
    "media_type": {
        "typeof": "string",
        "base": "str",
        "uri": "xsd:string",
        "description": "An IANA media type, such as text/plain.",
        "pattern": MEDIA_TYPE_PATTERN,
    },
    "semver": {
        "typeof": "string",
        "base": "str",
        "uri": "xsd:string",
        "description": "A semantic version, such as 3.0.1.",
        "pattern": SEMVER_PATTERN,
    },
    "positive_integer": {
        "typeof": "integer",
        "base": "int",
        "uri": "xsd:positiveInteger",
        "description": "An integer of one or more.",
        "minimum_value": 1,
    },
    "non_negative_integer": {
        "typeof": "integer",
        "base": "int",
        "uri": "xsd:nonNegativeInteger",
        "description": "An integer of zero or more.",
        "minimum_value": 0,
    },
}

# (XSD datatype, SHACL pattern or None) -> the LinkML range to use
DATATYPES = {
    (str(XSD.string), None): "string",
    (str(XSD.string), MEDIA_TYPE_PATTERN): "media_type",
    (str(XSD.string), SEMVER_PATTERN): "semver",
    (str(XSD.anyURI), None): "uri",
    (str(XSD.boolean), None): "boolean",
    (str(XSD.decimal), None): "decimal",
    (str(XSD.integer), None): "integer",
    (str(XSD.dateTimeStamp), None): "date_time_stamp",
    (str(XSD.dateTimeStamp), DATE_TIME_PATTERN): "date_time_stamp",
    (str(XSD.positiveInteger), None): "positive_integer",
    (str(XSD.nonNegativeInteger), None): "non_negative_integer",
}

# Classes a Core field ranges over, declared in the core module so that no
# module imports a module that imports it back.
HOISTED_TO_CORE = {"Extension", "AnyLicenseInfo"}

PROFILES = {
    # profile -> (title, description)
    "Core": (
        "SPDX Core profile",
        "The Core profile: the Element that every SPDX object descends from, agents, relationships, "
        "collections and documents, creation information, integrity methods and external references. "
        "The other profiles build on it, and the LinkML types this schema declares live here.",
    ),
    "Software": (
        "SPDX Software profile",
        "The Software profile: packages, files and snippets, their purposes and content identifiers, "
        "and the SBOM collection.",
    ),
    "Security": (
        "SPDX Security profile",
        "The Security profile: vulnerabilities and the assessment relationships that score them, "
        "with CVSS, EPSS, SSVC, exploit catalogues and VEX statements.",
    ),
    "SimpleLicensing": (
        "SPDX Simple Licensing profile",
        "The Simple Licensing profile: a license expression string and a block of license text.",
    ),
    "ExpandedLicensing": (
        "SPDX Expanded Licensing profile",
        "The Expanded Licensing profile: listed and custom licenses and additions, and the operators "
        "that compose them into license sets.",
    ),
    "AI": (
        "SPDX AI profile",
        "The AI profile: an AI package with its model, training, energy and safety information.",
    ),
    "Dataset": (
        "SPDX Dataset profile",
        "The Dataset profile: a dataset package with its collection, sensitivity, availability and "
        "bias information.",
    ),
    "Build": (
        "SPDX Build profile",
        "The Build profile: a build with its type, configuration source, parameters and environment.",
    ),
    "Extension": (
        "SPDX Extension profile",
        "The Extension profile: the extension hook on every Element and the CycloneDX properties extension.",
    ),
}

# The designator's range is uriorcurie, not string: the LinkML runtime writes the
# designator's value as the node's rdf:type, so a class name would be a literal.
TYPE_SLOT = {
    "description": "The class an object is an instance of, as the class's CURIE, such as spdx_software:Package.",
    "slot_uri": "rdf:type",
    "designates_type": True,
    "range": "uriorcurie",
    "comments": [
        "SPDX JSON-LD writes the same key with a term of its context, software_Package for a Package. "
        "This schema takes the class's CURIE or its full IRI, so RDF written from the data types each "
        "object with its SPDX class.",
    ],
}

SPDX_ID_ATTRIBUTE = {
    "description": "The IRI that identifies this Element. A reference to an Element from any field is this IRI.",
    "identifier": True,
    "range": "uri",
    "comments": [
        "SPDX JSON-LD writes an Element's IRI as spdxId. The model has no property for it, "
        "so this key is the schema's own, in its own namespace.",
    ],
}


def local(iri) -> str:
    return str(iri).rsplit("/", 1)[-1]


def module_of_profile(profile: str) -> str:
    return "spdx_" + re.sub(r"(?<=[a-z])(?=[A-Z])", "_", profile).lower()


def toposort(deps: dict[str, set[str]]) -> list[str]:
    """Order the modules so that each comes after the modules it imports."""
    order: list[str] = []
    pending = {k: set(v) for k, v in deps.items()}
    while pending:
        ready = sorted(k for k, v in pending.items() if not v)
        if not ready:
            raise SystemExit(f"import cycle among modules: {sorted(pending)}")
        for k in ready:
            order.append(k)
            del pending[k]
        for v in pending.values():
            v.difference_update(ready)
    return order


class Converter:
    def __init__(self, ttl: Path) -> None:
        self.g = Graph().parse(str(ttl), format="turtle")
        ontology = next(self.g.subjects(RDF.type, OWL.Ontology))
        self.terms_ns = str(ontology)
        match = re.search(r"/rdf/([^/]+)/terms/$", self.terms_ns)
        if not match:
            raise SystemExit(f"cannot read the SPDX version from the ontology IRI {self.terms_ns}")
        self.version = match.group(1)
        self.spec = f"https://spdx.github.io/spdx-spec/v{self.version}"
        self.source = f"https://spdx.org/rdf/{self.version}/spdx-model.ttl"
        self.report: list[str] = []
        self._classify()
        self._name_properties()
        self._collect_fields()

    # -- reading the model --------------------------------------------------

    def profile(self, iri) -> str:
        if not str(iri).startswith(self.terms_ns):
            raise SystemExit(f"{iri} is outside the SPDX terms namespace")
        return str(iri)[len(self.terms_ns) :].split("/")[0]

    def curie(self, iri) -> str:
        if str(iri).startswith(self.terms_ns):
            return f"{module_of_profile(self.profile(iri))}:{str(iri)[len(self.terms_ns) + len(self.profile(iri)) + 1 :]}"
        raise SystemExit(f"no prefix for {iri}")

    def text(self, subject, predicate=RDFS.comment) -> str:
        value = self.g.value(subject, predicate)
        if value is None:
            return ""
        s = re.sub(r"\s*\n\s*", " ", str(value).replace("\r\n", "\n")).strip()
        s = re.sub(r"[ \t]{2,}", " ", s)
        s = s.replace("\\*", "*")  # a Markdown escape upstream, a stray backslash in generated code
        s = s.replace("](../../../annexes/", f"]({self.spec}/annexes/").replace(".md)", "/)")
        if "](../" in s:
            self.report.append(f"relative link left in the description of {local(subject)}")
        return s

    def _classify(self) -> None:
        g = self.g
        owl_classes = set(g.subjects(RDF.type, OWL.Class))
        by_class: dict[URIRef, list[URIRef]] = defaultdict(list)
        for individual in g.subjects(RDF.type, OWL.NamedIndividual):
            for t in g.objects(individual, RDF.type):
                if t != OWL.NamedIndividual:
                    by_class[t].append(individual)
        self.enum_classes = {c for c, members in by_class.items() if any(g.value(m, RDFS.label) for m in members)}
        self.enum_members = {c: sorted(by_class[c], key=lambda m: str(g.value(m, RDFS.label))) for c in self.enum_classes}
        self.classes = owl_classes - self.enum_classes
        for c, members in by_class.items():
            if c not in self.enum_classes:
                self.report.append(f"left out, instance data: {', '.join(sorted(local(m) for m in members))} (a {local(c)})")
        self.element = URIRef(self.terms_ns + "Core/Element")
        names = defaultdict(list)
        for c in self.classes | self.enum_classes:
            names[local(c)].append(c)
        clashes = {n: v for n, v in names.items() if len(v) > 1}
        if clashes:
            raise SystemExit(f"two classes share a local name: {clashes}")
        self.by_name = {local(c): c for c in self.classes | self.enum_classes}

    def parent(self, cls):
        return self.g.value(cls, RDFS.subClassOf)

    def is_element(self, cls) -> bool:
        while cls is not None:
            if cls == self.element:
                return True
            cls = self.parent(cls)
        return False

    def is_abstract(self, cls) -> bool:
        for shape in self.g.objects(cls, SH.property):
            if self.g.value(shape, SH.path) == RDF.type and self.g.value(shape, SH["not"]) is not None:
                return True
        return False

    def module_of_class(self, cls) -> str:
        if local(cls) in HOISTED_TO_CORE:
            return CORE
        return module_of_profile(self.profile(cls))

    def _name_properties(self) -> None:
        g = self.g
        self.properties = set(g.subjects(RDF.type, OWL.ObjectProperty)) | set(g.subjects(RDF.type, OWL.DatatypeProperty))
        counts = defaultdict(int)
        for p in self.properties:
            counts[local(p)] += 1
        self.slot_name: dict[URIRef, str] = {}
        for p in self.properties:
            if counts[local(p)] > 1 and self.profile(p) != "Core":
                self.slot_name[p] = f"{self.profile(p).lower()}_{local(p)}"
                self.report.append(f"property {self.curie(p)} is the slot {self.slot_name[p]}: Core also has a {local(p)}")
            else:
                self.slot_name[p] = local(p)

    def _collect_fields(self) -> None:
        """For each class, one merged constraint per property; and who uses each property."""
        g = self.g
        self.fields: dict[URIRef, dict[URIRef, dict]] = {}
        self.uses: dict[URIRef, list[URIRef]] = defaultdict(list)
        for cls in self.classes:
            merged: dict[URIRef, dict] = {}
            for shape in g.objects(cls, SH.property):
                path = g.value(shape, SH.path)
                if path == RDF.type:
                    continue
                c = merged.setdefault(path, {"target": None, "min": None, "max": None, "pattern": None, "in": None})
                for key, predicate in (
                    ("target", SH["class"]),
                    ("target", SH.datatype),
                    ("min", SH.minCount),
                    ("max", SH.maxCount),
                    ("pattern", SH.pattern),
                ):
                    value = g.value(shape, predicate)
                    if value is not None:
                        c[key] = value
                members = g.value(shape, SH["in"])
                if members is not None:
                    c["in"] = list(rdflib.collection.Collection(g, members))
            self.fields[cls] = {p: self.resolve(cls, p, c) for p, c in merged.items()}
            for p in merged:
                self.uses[p].append(cls)
        unused = sorted(self.slot_name[p] for p in self.properties if p not in self.uses)
        if unused:
            self.report.append(f"properties no class uses, left out: {unused}")
        self.shared = {p for p, classes in self.uses.items() if len(classes) > 1}

    def resolve(self, cls, prop, c) -> dict:
        """The LinkML field for one property shape: range, cardinality, inlining, pattern."""
        target = c["target"] if c["target"] is not None else self.g.value(prop, RDFS.range)
        pattern = str(c["pattern"]) if c["pattern"] is not None else None
        field = {"description": self.text(prop), "slot_uri": self.curie(prop)}
        if target in self.enum_classes:
            field["range"] = local(target)
            if c["in"] is not None:
                listed = {local(m) for m in c["in"]}
                declared = {local(m) for m in self.enum_members[target]}
                if listed != declared:
                    self.report.append(f"{local(cls)}.{local(prop)} lists {sorted(listed ^ declared)} differently from {local(target)}")
        elif target in self.classes:
            field["range"] = local(target)
        elif str(target).startswith(str(XSD)):
            key = (str(target), pattern)
            if key in DATATYPES:
                field["range"] = DATATYPES[key]
                pattern = None
            elif (str(target), None) in DATATYPES:
                field["range"] = DATATYPES[(str(target), None)]
                self.report.append(f"{local(cls)}.{local(prop)} keeps a pattern no type declares: {pattern}")
            else:
                raise SystemExit(f"no LinkML range for {target} on {local(cls)}.{local(prop)}")
        else:
            raise SystemExit(f"no LinkML range for {target} on {local(cls)}.{local(prop)}")
        minimum = int(c["min"]) if c["min"] is not None else 0
        maximum = int(c["max"]) if c["max"] is not None else None
        if minimum >= 1:
            field["required"] = True
        if maximum != 1:
            field["multivalued"] = True
        if minimum > 1:
            field["minimum_cardinality"] = minimum
        if maximum is not None and maximum > 1:
            field["maximum_cardinality"] = maximum
        if target in self.classes and not self.is_element(target):
            field["inlined"] = True
            if maximum != 1:
                field["inlined_as_list"] = True
        if pattern:
            field["pattern"] = pattern
        field["see_also"] = [f"{self.spec}/model/{self.profile(prop)}/Properties/{local(prop)}/"]
        return field

    # -- building the schema dictionaries ------------------------------------

    def prefixes(self) -> dict:
        p = {OWN_PREFIX: OWN_NS, UMBRELLA: self.terms_ns}
        for profile in PROFILES:
            p[module_of_profile(profile)] = f"{self.terms_ns}{profile}/"
        p.update({"linkml": "https://w3id.org/linkml/", "rdf": str(RDF), "xsd": str(XSD)})
        return p

    def header(self, name: str, title: str, description: str, see_also: list[str], imports: list[str], comments=None) -> dict:
        h: dict = {
            "id": SCHEMA_ID if name == UMBRELLA else f"{SCHEMA_ID}/{name}",
            "name": name,
            "title": title,
            "description": description,
            "version": self.version,
            "source": self.source,
            "license": LICENSE,
            "see_also": see_also,
        }
        if comments:
            h["comments"] = comments
        h["prefixes"] = self.prefixes()
        h["default_prefix"] = OWN_PREFIX
        h["default_range"] = "string"
        h["imports"] = imports
        return h

    def slot_definition(self, prop) -> tuple[dict, dict[URIRef, dict]]:
        """A shared property's slot: the keys every use agrees on, and each class's differences."""
        uses = {cls: self.fields[cls][prop] for cls in self.uses[prop]}
        keys = []
        for f in uses.values():
            for k in f:
                if k not in keys:
                    keys.append(k)
        slot: dict = {}
        differences: dict[URIRef, dict] = defaultdict(dict)
        for k in keys:
            values = [f.get(k) for f in uses.values()]
            if all(v == values[0] for v in values):
                slot[k] = values[0]
            else:
                for cls, f in uses.items():
                    if k in f:
                        differences[cls][k] = f[k]
        return slot, differences

    def class_definition(self, cls, slot_level: dict[URIRef, tuple[dict, dict]]) -> dict:
        name = local(cls)
        d: dict = {}
        parent = self.parent(cls)
        if parent is not None:
            d["is_a"] = local(parent)
        if self.is_abstract(cls):
            d["abstract"] = True
        d["class_uri"] = self.curie(cls)
        d["description"] = self.text(cls)
        if name in HOISTED_TO_CORE:
            d["comments"] = [
                f"Declared in the core module because a Core field ranges over it. "
                f"Its IRI stays in the {self.profile(cls)} profile's namespace, and so does its subset."
            ]
        d["see_also"] = [f"{self.spec}/model/{self.profile(cls)}/Classes/{name}/"]
        d["in_subset"] = [module_of_profile(self.profile(cls))]
        slots = ["type"] if parent is None else []
        slots += sorted(self.slot_name[p] for p in self.fields[cls] if p in self.shared)
        if slots:
            d["slots"] = slots
        attributes: dict = {}
        if cls == self.element:
            attributes["spdxId"] = dict(SPDX_ID_ATTRIBUTE)
        for p in sorted(self.fields[cls], key=lambda p: self.slot_name[p]):
            if p not in self.shared:
                attributes[self.slot_name[p]] = self.fields[cls][p]
        if attributes:
            d["attributes"] = attributes
        usage = {}
        for p in sorted(self.fields[cls], key=lambda p: self.slot_name[p]):
            if p in self.shared and cls in slot_level[p][1]:
                usage[self.slot_name[p]] = slot_level[p][1][cls]
        if usage:
            d["slot_usage"] = usage
        return d

    def enum_definition(self, enum) -> dict:
        values = {}
        for member in self.enum_members[enum]:
            label = str(self.g.value(member, RDFS.label))
            values[label] = {"description": self.text(member), "meaning": self.curie(member)}
        return {
            "enum_uri": self.curie(enum),
            "description": self.text(enum),
            "see_also": [f"{self.spec}/model/{self.profile(enum)}/Vocabularies/{local(enum)}/"],
            "in_subset": [module_of_profile(self.profile(enum))],
            "permissible_values": values,
        }

    def build(self) -> dict[str, dict]:
        """Every schema file by name: the umbrella and one module per profile."""
        slot_level = {p: self.slot_definition(p) for p in self.shared}
        modules = {module_of_profile(profile): profile for profile in PROFILES}
        classes_in = defaultdict(list)
        for cls in self.classes:
            classes_in[self.module_of_class(cls)].append(cls)
        enums_in = defaultdict(list)
        for enum in self.enum_classes:
            enums_in[module_of_profile(self.profile(enum))].append(enum)
        slots_in = defaultdict(list)
        for p in self.shared:
            slots_in[module_of_profile(self.profile(p))].append(p)

        def module_of_range(name: str) -> str:
            if name in TYPES or name in ("string", "uri", "boolean", "decimal", "integer", "datetime"):
                return CORE
            return self.module_of_class(self.by_name[name])

        deps: dict[str, set[str]] = {m: set() for m in modules}
        for module in modules:
            needed = {CORE} if module != CORE else set()
            for cls in classes_in[module]:
                if self.parent(cls) is not None:
                    needed.add(self.module_of_class(self.parent(cls)))
                for p, f in self.fields[cls].items():
                    needed.add(module_of_range(f["range"]))
                    if p in self.shared:
                        needed.add(module_of_profile(self.profile(p)))
            for p in slots_in[module]:
                needed.add(module_of_range(slot_level[p][0]["range"]))
            deps[module] = needed - {module}
        order = toposort(deps)

        files: dict[str, dict] = {}
        for module in order:
            profile = modules[module]
            title, description = PROFILES[profile]
            imports = ["linkml:types"] + [f"./{m}" for m in sorted(deps[module], key=lambda m: (m != CORE, m))]
            schema = self.header(module, title, description, [f"{self.spec}/model/{profile}/{profile}/"], imports)
            if module == CORE:
                schema["subsets"] = {
                    module_of_profile(p): {"description": f"Elements of the {PROFILES[p][0]}."} for p in PROFILES
                }
                schema["types"] = {name: {**definition, "in_subset": [CORE]} for name, definition in TYPES.items()}
            if enums_in[module]:
                schema["enums"] = {local(e): self.enum_definition(e) for e in sorted(enums_in[module], key=local)}
            slots = {}
            if module == CORE:
                slots["type"] = {**TYPE_SLOT, "in_subset": [CORE]}
            for p in sorted(slots_in[module], key=lambda p: self.slot_name[p]):
                slots[self.slot_name[p]] = {**slot_level[p][0], "in_subset": [module_of_profile(self.profile(p))]}
            if slots:
                schema["slots"] = slots
            if classes_in[module]:
                schema["classes"] = {
                    local(c): self.class_definition(c, slot_level) for c in sorted(classes_in[module], key=local)
                }
            files[module] = schema

        umbrella = self.header(
            UMBRELLA,
            "System Package Data Exchange (SPDX)",
            f"A LinkML rendering of the SPDX {self.version} model: its nine profiles, each a module, "
            "with every class, property and vocabulary keeping its SPDX IRI.",
            [DOCS_SITE, f"{self.spec}/", "https://spdx.dev/specifications/"],
            ["linkml:types"] + [f"./{m}" for m in order],
            comments=[
                "scripts/spdx_to_linkml.py writes every YAML file in this folder from the vendored model, "
                "upstream/spdx-model.ttl. Change the script or the model, never the files.",
                "spdx_core imports only the LinkML types, each profile module imports the modules it "
                "references, and this file adds nothing of its own, so an importer can take one profile.",
                "The element descriptions are the model's own rdfs:comment texts, which the SPDX Project "
                "publishes under the Community Specification License 1.0.",
                "The model's individuals (NoAssertionElement, NoneElement, NoAssertionLicense, NoneLicense "
                "and SpdxOrganization) are instance data, not schema. A reference to one is an IRI like "
                "any other Element reference.",
            ],
        )
        return {UMBRELLA: umbrella, **files}


# -- writing YAML ---------------------------------------------------------------


class _Dumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):  # lists sit indented under their key
        return super().increase_indent(flow, False)


def _represent_str(dumper, data):
    if len(data) > 80 and " " in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style=">")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_Dumper.add_representer(str, _represent_str)

_SECTION_KEYS = {"prefixes", "default_prefix", "imports", "subsets", "types", "enums", "slots", "classes"}
_ELEMENT_SECTIONS = {"subsets", "types", "enums", "slots", "classes"}


def dump(schema: dict) -> str:
    raw = yaml.dump(schema, Dumper=_Dumper, default_flow_style=False, allow_unicode=True, sort_keys=False, width=100)
    out: list[str] = []
    in_elements = False
    for line in raw.split("\n"):
        indent = len(line) - len(line.lstrip())
        if line.strip() and indent == 0 and ":" in line:
            key = line.split(":", 1)[0]
            if key in _SECTION_KEYS and out and out[-1] != "":
                out.append("")
            in_elements = key in _ELEMENT_SECTIONS
        elif line.strip() and indent == 2 and in_elements and not line.lstrip().startswith("-"):
            if out and out[-1] != "":
                out.append("")
        out.append(line)
    text = "\n".join(out).rstrip("\n") + "\n"
    return "---\n" + text


def write_all(files: dict[str, dict], out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    for name, schema in files.items():
        (out_dir / f"{name}.yaml").write_text(dump(schema), encoding="utf-8")


def check(files: dict[str, dict], out_dir: Path) -> int:
    """Compare a fresh rendering with the files in out_dir; 0 when they agree."""
    with tempfile.TemporaryDirectory() as tmp:
        fresh = Path(tmp)
        write_all(files, fresh)
        status = 0
        expected = {f"{name}.yaml" for name in files}
        present = {p.name for p in out_dir.glob("*.yaml")}
        for name in sorted(present - expected):
            print(f"not written by the converter: {out_dir / name}")
            status = 1
        for name in sorted(expected):
            new = (fresh / name).read_text(encoding="utf-8")
            old_path = out_dir / name
            old = old_path.read_text(encoding="utf-8") if old_path.exists() else ""
            if new != old:
                status = 1
                diff = difflib.unified_diff(old.splitlines(), new.splitlines(), str(old_path), "regenerated", lineterm="", n=1)
                print("\n".join(list(diff)[:40]))
        return status


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--ttl", type=Path, default=DEFAULT_TTL, help="the vendored SPDX model")
    parser.add_argument("-d", "--output-dir", type=Path, default=DEFAULT_OUT, help="where the modules go")
    parser.add_argument("--check", action="store_true", help="compare with the output folder instead of writing")
    args = parser.parse_args(argv)
    converter = Converter(args.ttl)
    files = converter.build()
    for line in converter.report:
        print(f"note: {line}", file=sys.stderr)
    if args.check:
        return check(files, args.output_dir)
    write_all(files, args.output_dir)
    classes = sum(len(s.get("classes", {})) for s in files.values())
    slots = sum(len(s.get("slots", {})) for s in files.values())
    attributes = sum(len(c.get("attributes", {})) for s in files.values() for c in s.get("classes", {}).values())
    enums = sum(len(s.get("enums", {})) for s in files.values())
    print(
        f"SPDX {converter.version}: {len(files) - 1} modules, {classes} classes, {slots} shared slots, "
        f"{attributes} attributes, {enums} enums, written to {args.output_dir}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
