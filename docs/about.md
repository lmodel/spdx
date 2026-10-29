# About spdx

This page is for anyone who uses or maintains this schema. The schema renders
the SPDX 3.0.1 model in LinkML, as the SPDX Project publishes it. Its
identifier, <https://w3id.org/lmodel/spdx>, redirects a browser to this site
and a request for YAML to the schema. Its source is the
[lmodel/spdx](https://github.com/lmodel/spdx) repository.

## Where the model comes from

The SPDX Project publishes its model as OWL and SHACL in Turtle at
<https://spdx.org/rdf/3.0.1/spdx-model.ttl>. The repository holds a copy at
`src/spdx/schema/upstream/spdx-model.ttl`, and `scripts/spdx_to_linkml.py`
writes every schema file from it. Those files are `spdx.yaml`, the umbrella
that imports the rest, and one module per profile, such as `spdx_core.yaml`
and `spdx_software.yaml`. The script's docstring lists the rules it applies.

- `just gen-linkml` rewrites the schema from the vendored model.
- `just gen-linkml-check` fails when a schema file was edited by hand.
- `just upstream-check` compares the vendored copy with the published model,
  and reports a newer SPDX release. The Upstream watch workflow runs the same
  check every Monday, and opens an issue when it fails.

To move to a new SPDX release:

1. Replace the vendored file with the published one.
2. Run `just gen-linkml`.
3. Run `just lint`, `just gen-project` and `just test`.

## What the rendering adds

Every class, slot, enum and value carries its SPDX IRI, so the OWL, SHACL and
JSON-LD context the generators write use SPDX's terms. The schema adds five
things the model does not have:

- `spdxId`, the identifier of an Element. SPDX writes an Element's IRI as the
  `spdxId` key in JSON-LD, and the model has no property for it.
- `type`, the type designator every root class carries. Its value is the
  class's CURIE, such as `spdx_core:Hash`, so an inlined object inside
  `verifiedUsing` says which IntegrityMethod it is.
- Five types for the datatypes SPDX constrains: `date_time_stamp`,
  `media_type`, `semver`, `positive_integer` and `non_negative_integer`.
- One module per profile, with `Extension` and `AnyLicenseInfo` declared in
  the core module because Core's fields range over them.
- One subset per profile, so the documentation can be read a profile at a time.

The element descriptions are the model's texts, which the SPDX Project
publishes under the Community Specification License 1.0. The model's
individuals (NoAssertionElement, NoneElement, NoAssertionLicense, NoneLicense
and SpdxOrganization) are instance data and are not in the schema. A reference
to one is an IRI like any other Element reference.

## Where it differs from SPDX's serialisations

A document in SPDX's JSON-LD serialisation does not validate against this
schema as it stands:

- SPDX JSON-LD prefixes the name of a class or property outside Core with its
  profile, as in `software_Package` and `software_packageVersion`. This schema
  uses the bare name, and the class's CURIE as the value of `type`.
- SPDX JSON-LD gives CreationInfo a blank-node identifier, and each Element
  refers to it, as in `"creationInfo": "_:creationinfo"`. This schema inlines
  CreationInfo in each Element.

RDF written from this schema's data differs from SPDX's RDF in two ways, both
in LinkML 1.12.1:

- The LinkML Python runtime writes the value of an `xsd:anyURI` property, such
  as `downloadLocation`, as an IRI. SPDX's SHACL wants a literal, and reports
  each such value as a violation. The JSON-LD context writes these values as
  literals.
- The JSON-LD context writes `type` as an `xsd:anyURI` literal, so JSON-LD read
  as RDF gives a node no SPDX class. The Python runtime writes the class IRI.

SPDX's SHACL also says that an Element's `extension` must not be an instance of
a class of the model. The schema has no such rule.

## Examples and tests

- `tests/data/valid/` and `tests/data/problem/valid/` hold examples named
  `<Class>-<anything>.yaml`, each validated against its class. They cover
  every concrete class but IndividualElement and IndividualLicensingInfo,
  whose only instances are the model's individuals.
- `tests/data/invalid/` holds counter-examples, each failing for the one
  reason its name states.
- `tests/data/problem/` holds the examples the example runner cannot load,
  because a Relationship's `from` key and an SpdxDocument's `import` key are
  Python keywords. The validator checks them like the others.
- `tests/test_rdf.py` writes each example in `tests/data/valid/` as RDF, and
  checks that every node has an SPDX class and every timestamp keeps its `Z`.
- `tests/data/spdx-examples/` is a copy of the SPDX Project's
  [spdx-examples](https://github.com/spdx/spdx-examples) repository. The tests
  read its SPDX 3 documents for class names, required fields and vocabulary
  values.

## References

- [SPDX specification 3.0.1](https://spdx.github.io/spdx-spec/v3.0.1/)
- [The SPDX 3.0.1 model in Turtle](https://spdx.org/rdf/3.0.1/spdx-model.ttl)
- [spdx-examples](https://github.com/spdx/spdx-examples)
