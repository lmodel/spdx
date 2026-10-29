---
type: Dataset
id: https://w3id.org/lmodel/spdx/knowledge/datasets/test-data
genre: reference
title: Test data and schema tests
description: "Example instances of the spdx schema in tests/data/: 54 valid files and 88 counter-examples, one for each constraint the schema states, each named after its class (Package-with-hash.yaml, Hash-missing-hashValue.yaml), which tests/test_data.py holds to the validator; beside them, tests/test_rdf.py writes the valid examples as RDF, tests/test_schema_is_generated.py fails on a hand-edited schema, and tests/test_schema_rules.py checks the adapt copy's names against LOKF's and three neighbour copies."
resource: tests/data
about:
  - https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-linkml-schema
references:
  - https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-examples
sources:
  - id: data-readme.md
    resource: tests/data/README.md
    title: the folders and the naming rule
  - id: test_data.py
    resource: tests/test_data.py
    title: the docstring, NAMED_REASONS, REASONS and the test functions
  - id: test_rdf.py
    resource: tests/test_rdf.py
    title: the docstring and the three tests
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the docstring, the neighbour comment, the shared names and the four tests
  - id: justfile
    resource: justfile
    title: the test recipe and its three parts
  - resource: tests/test_schema_is_generated.py
    title: the one test
  - resource: tests/neighbours
    title: the three neighbour copies
  - resource: tests/__init__.py
    title: the package marker
  - resource: examples/README.md
    title: the examples output folder
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Test data and schema tests

`tests/data/README.md` sorts the example data into these folders:[^data-readme.md]

- `valid/`, with one or more files for each concrete class;
- `invalid/`, with a counter-example for each constraint the schema states;
- `problem/valid/` and `problem/invalid/`, for the examples the example runner cannot load because a key is a Python keyword: a Relationship's `from` and an SpdxDocument's `import`.

A file name has the form `<Class>-<anything>.yaml`, and the test validates the file against the class before the first hyphen. An example's `type` is a class CURIE, such as `spdx_software:Package`.

## The examples

`tests/data/valid/` holds 41 files and `tests/data/problem/valid/` 13, which cover every concrete class but IndividualElement and IndividualLicensingInfo. `tests/data/invalid/` holds 64 counter-examples and `tests/data/problem/invalid/` 24. A counter-example's name gives its fault: `<Class>-missing-<slot>` for a required slot, `<Class>-<slot>-unknown-value` for a value outside an enum, and a name in `REASONS` for the patterned and bounded types, the license sets' minimum of two members, the identifier, the type designator and the closed classes. `tests/data/spdx-examples/` is the [SPDX examples copy](spdx-examples.md).

## tests/test_data.py

`tests/test_data.py` validates each valid example against its class with closed classes, and requires each counter-example to fail once, with the parts of the message its name or `REASONS` gives.[^test_data.py] Two tests fail when a slot a class makes required, or an enum, has no counter-example. Six more read the SPDX Project's examples, and check that:

- each JSON file parses;
- each SPDX 3 document has a JSON-LD graph;
- each node's type is a class of the schema;
- each required slot is present;
- each vocabulary value is one its enum declares;
- each SPDX 2 document under an `spdx2.*` folder carries `spdxVersion` and `SPDXID`.

## tests/test_rdf.py and tests/test_schema_is_generated.py

`tests/test_rdf.py` writes each example in `tests/data/valid/` as RDF through the LinkML Python runtime, and checks that every node has an SPDX class as its type and every `xsd:dateTimeStamp` keeps its `Z`.[^test_rdf.py] A third test is a strict expected failure: linkml-runtime 1.12.1 writes an `xsd:anyURI` value as an IRI, where SPDX's SHACL wants a literal. `tests/test_schema_is_generated.py` runs the converter with `--check`, so a hand edit of the schema, or a stale regeneration, fails.

## tests/test_schema_rules.py

`tests/test_schema_rules.py` checks `.lokf/spdx.yaml` against `.lokf/lokf.yaml` and three neighbour copies in `tests/neighbours/`, the schema assets of slsa v0.7.0, github-actions v0.2.1 and oscal v0.1.0, each checked against its `.sha256` and its attestation.[^test_schema_rules.py] Its four tests require that:

- no class, enum, type or subset name of the copy is LOKF's, and no key is LOKF's under another IRI;
- the copy shares with a neighbour only the listed class, `Hash` with oscal's copy, and the listed keys, `subject` and `value` with slsa's and `identifier`, `statement`, `subject` and `value` with oscal's;
- every IRI the copy names is a CURIE whose prefix the copy binds, so `lokf convert --schema` warns of no namespace;
- a prefix the copy binds means what `lokf.yaml` and each neighbour bind it to.

## How they run

`just test` runs three recipes.[^justfile] `_test-schema` generates the project into `tmp/`. `_test-python` regenerates the Python models and runs pytest. `_test-examples` runs `linkml-run-examples` over `tests/data/valid/` and `tests/data/invalid/` and writes what it converts into `examples/output/`, which git ignores. [Build and test](../workflows/main.md) runs `just test` on every pull request.

[^data-readme.md]: tests/data/README.md, the whole page
[^test_data.py]: tests/test_data.py, the docstring, `NAMED_REASONS`, `REASONS` and the test functions
[^test_rdf.py]: tests/test_rdf.py, the docstring and the three tests
[^test_schema_rules.py]: tests/test_schema_rules.py, the docstring, the comment above COPY, the shared names and the four tests
[^justfile]: justfile, the `test`, `_test-schema`, `_test-python` and `_test-examples` recipes
