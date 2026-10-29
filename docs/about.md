# About spdx

This schema renders the SPDX 3.0.1 model, as the SPDX Project publishes it, in
LinkML. Its identifier is <https://w3id.org/lmodel/spdx>, which serves the
schema files, and its source is the [lmodel/spdx](https://github.com/lmodel/spdx)
repository.

## Where the model comes from

The SPDX Project publishes its model as OWL and SHACL in Turtle at
<https://spdx.org/rdf/3.0.1/spdx-model.ttl>. A copy sits in the repository at
`src/spdx/schema/upstream/spdx-model.ttl`, and `scripts/spdx_to_linkml.py`
writes every schema file from it: `spdx.yaml`, the umbrella that imports the
rest, and one module per profile, `spdx_core.yaml`, `spdx_software.yaml` and
so on. The script's docstring lists the rules it applies.

- `just gen-linkml` rewrites the schema from the vendored model.
- `just gen-linkml-check` fails when a schema file was edited by hand.
- `just upstream-check` compares the vendored copy with the published model
  and reports a newer SPDX release.

To move to a new SPDX release, replace the vendored file with the published
one, run `just gen-linkml`, then the usual `just lint`, `just gen-project` and
`just test`.

## What the rendering adds

Every class, slot, enum and value carries its SPDX IRI, so the OWL, SHACL and
JSON-LD context the generators write use SPDX's terms. The schema adds five
things of its own, each in its own namespace:

- `spdxId`, the identifier of an Element. SPDX writes an Element's IRI as the
  `spdxId` key in JSON-LD; the model has no property for it.
- `type`, the type designator every root class carries, so an inlined object
  such as a Hash inside `verifiedUsing` says which IntegrityMethod it is.
- Five types for the datatypes SPDX constrains: `date_time_stamp`,
  `media_type`, `semver`, `positive_integer` and `non_negative_integer`.
- One module per profile, with `Extension` and `AnyLicenseInfo` declared in
  the core module because Core's own fields range over them.
- One subset per profile, so the documentation can be read a profile at a time.

The element descriptions are the model's own texts, which the SPDX Project
publishes under the Community Specification License 1.0. The model's
individuals (NoAssertionElement, NoneElement, NoAssertionLicense, NoneLicense
and SpdxOrganization) are instance data and are not in the schema; a reference
to one is an IRI like any other Element reference.

## Examples and tests

- `tests/data/valid/` holds an example per class the upstream examples use,
  named `<Class>-<anything>.yaml`, each validated against its class.
- `tests/data/invalid/` holds one counter-example per constraint worth having,
  each failing for the one reason its name states.
- `tests/data/problem/valid/` holds the examples the example runner cannot
  load: a Relationship's `from` key and an SpdxDocument's `import` key are
  Python keywords. The validator still checks them.
- `tests/data/spdx-examples/` is a copy of the SPDX Project's
  [spdx-examples](https://github.com/spdx/spdx-examples) repository. The tests
  read its SPDX 3 documents for class names, required fields and vocabulary
  values.

## References

- [SPDX specification 3.0.1](https://spdx.github.io/spdx-spec/v3.0.1/)
- [The SPDX 3.0.1 model in Turtle](https://spdx.org/rdf/3.0.1/spdx-model.ttl)
- [spdx-examples](https://github.com/spdx/spdx-examples)
