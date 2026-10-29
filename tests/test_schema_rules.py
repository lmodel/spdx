"""Checks that the adapt copy can sit beside LOKF's schema and the neighbour copies.

`.lokf/spdx.yaml` is the copy `lokf adapt` writes from the schema, and a host
imports it beside `lokf.yaml` and the copies other lmodel repositories release.
LinkML merges a host's imports into one namespace, where the last definition of
a name wins, and the JSON-LD context gives each key one IRI. So a name the copy
shares with another file must mean the same thing there, or be listed here.
"""

from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent

# What a host may import beside this schema's adapt copy: LOKF's schema, pinned
# by the sidecar, and the adapt copies other lmodel repositories release. Each
# neighbour is the schema asset of a release, checked against its .sha256 and
# its build-provenance attestation: schema-v0.7.0-slsa.yaml from lmodel/slsa,
# schema-v0.2.1-github-actions.yaml from lmodel/github-actions and
# schema-v0.1.0-oscal.yaml from lmodel/oscal.
COPY = ROOT / ".lokf" / "spdx.yaml"
LOKF = ROOT / ".lokf" / "lokf.yaml"
NEIGHBOURS = (
    ROOT / "tests" / "neighbours" / "slsa.yaml",
    ROOT / "tests" / "neighbours" / "github-actions.yaml",
    ROOT / "tests" / "neighbours" / "oscal.yaml",
)
ELEMENT_KINDS = ("classes", "enums", "types", "subsets")

# Keys the copy shares with a neighbour under another IRI. They are SPDX's own
# property names, and `lokf adapt` renames only what lokf.yaml defines, so they
# stay until it can rename what a neighbour copy defines too (lokf #169). A host
# that imports this copy beside one of these neighbours projects each key under
# one vocabulary's IRI. A new overlap fails the test.
SHARED_KEYS = {
    "slsa.yaml": {"subject", "value"},
    "github-actions.yaml": set(),
    "oscal.yaml": {"identifier", "statement", "subject", "value"},
}

# Classes the copy and a neighbour both define. SPDX's Hash and OSCAL's hash are
# two classes with one name, so a host cannot import this copy beside oscal's:
# the merged namespace keeps one Hash, and `lokf convert` stops on its two IRIs.
SHARED_CLASSES = {
    "slsa.yaml": set(),
    "github-actions.yaml": set(),
    "oscal.yaml": {"Hash"},
}

# Every key whose value LinkML expands as a CURIE, and the mapping keys.
CURIE_KEYS = (
    "class_uri",
    "slot_uri",
    "enum_uri",
    "uri",
    "meaning",
    "mappings",
    "exact_mappings",
    "close_mappings",
    "related_mappings",
    "narrow_mappings",
    "broad_mappings",
)


def _names(path):
    """Each kind of element a schema file declares, and every slot and
    attribute name with the IRI it expands to."""
    doc = yaml.safe_load(path.read_text())
    prefixes = doc.get("prefixes") or {}

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return prefixes[prefix] + local if prefix in prefixes else curie

    default = doc.get("default_prefix")
    elements = {kind: set(doc.get(kind) or {}) for kind in ELEMENT_KINDS}
    slots = {}
    owners = [doc.get("slots") or {}]
    owners += [
        (cls or {}).get("attributes") or {}
        for cls in (doc.get("classes") or {}).values()
    ]
    for owner in owners:
        for name, slot in owner.items():
            uri = (slot or {}).get("slot_uri") or f"{default}:{name}"
            slots.setdefault(name, set()).add(expand(uri))
    return elements, slots


def _overlap(neighbour):
    """The elements of each kind the copy shares with a neighbour, and the keys
    it shares under another IRI."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(neighbour)
    shared = {kind: elements[kind] & their_elements[kind] for kind in ELEMENT_KINDS}
    keys = {
        name
        for name in slots.keys() & their_slots.keys()
        if slots[name] != their_slots[name]
    }
    return shared, keys


def test_names_apart_from_lokf():
    """No class, enum, type or subset name of the copy is LOKF's, and no key is
    LOKF's under another IRI: the copy renamed each name the two shared."""
    shared, keys = _overlap(LOKF)
    assert not any(shared.values()), shared
    assert not keys, keys


def test_names_apart_from_neighbours():
    """The copy shares no enum, type or subset name with a neighbour, and only
    the listed classes and keys."""
    for neighbour in NEIGHBOURS:
        shared, keys = _overlap(neighbour)
        assert shared["classes"] == SHARED_CLASSES[neighbour.name], neighbour.name
        for kind in ("enums", "types", "subsets"):
            assert not shared[kind], (neighbour.name, kind, shared[kind])
        assert keys == SHARED_KEYS[neighbour.name], neighbour.name


def _curies(node):
    """Every value of a key that LinkML expands as a CURIE, anywhere in a
    parsed schema file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in CURIE_KEYS and isinstance(value, (str, list)):
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _curies(value)
    elif isinstance(node, list):
        for item in node:
            yield from _curies(item)


def test_curies_use_a_bound_prefix():
    """Every IRI the copy names is a CURIE whose prefix the copy binds. A full
    address that no prefix covers makes every `lokf convert --schema` over the
    copy warn that it has no namespace."""
    doc = yaml.safe_load(COPY.read_text())
    prefixes = doc.get("prefixes") or {}
    curies = list(_curies(doc))
    assert curies
    for curie in curies:
        prefix, sep, _ = curie.partition(":")
        assert sep and prefix in prefixes, curie


def test_no_prefix_is_bound_twice():
    """A prefix the copy binds means what lokf.yaml and each neighbour bind it
    to, so LinkML can merge the files in one composite."""
    ours = yaml.safe_load(COPY.read_text()).get("prefixes") or {}
    for other in (LOKF, *NEIGHBOURS):
        theirs = yaml.safe_load(other.read_text()).get("prefixes") or {}
        for prefix in ours.keys() & theirs.keys():
            assert ours[prefix] == theirs[prefix], (other.name, prefix)
