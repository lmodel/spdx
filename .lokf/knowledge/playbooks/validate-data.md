---
type: Playbook
id: https://w3id.org/lmodel/spdx/knowledge/playbooks/validate-data
genre: how-to
title: Validate data against the schema
description: How to check a YAML or JSON file against the spdx schema with linkml-validate (for example with -C Package), why each object's type is a class CURIE such as spdx_software:Package, why a document in SPDX's own JSON-LD does not validate as it stands, and why the example runner cannot load an example with a from or import key.
resource: docs/about.md
relatedTo:
  - https://w3id.org/lmodel/spdx/knowledge/datasets/test-data
sources:
  - id: about.md
    resource: docs/about.md
    title: What the rendering adds, Where it differs from SPDX's serialisations, and Examples and tests
  - id: data-readme.md
    resource: tests/data/README.md
    title: the naming rule and the type CURIE
  - resource: tests/test_data.py
    title: the validator with closed classes
  - resource: src/spdx_linkml/schema/spdx_linkml.yaml
    title: the umbrella to validate against
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Validate data against the schema

## With linkml-validate

Validate a file against one class of the umbrella schema:

```bash
uv run linkml-validate -s src/spdx_linkml/schema/spdx_linkml.yaml -C Package package.yaml
```

`-C` names the class the file's object is an instance of. The tool reports a missing required slot, a value outside an enum or a pattern, and a key the class does not declare, as `tests/test_data.py` does with closed classes.

## What the data looks like

Each object's `type` is the class's CURIE, such as `spdx_software:Package`, or its full IRI, and an inlined object, such as a Hash under `verifiedUsing`, says which class it is the same way.[^about.md] An Element's identifier is its `spdxId`, an IRI, and a reference to an Element from any slot is that IRI. CreationInfo is inlined in each Element. `tests/data/README.md` names the examples after their classes, and `tests/data/valid/` holds one or more for each concrete class to copy from.[^data-readme.md]

## What does not validate as it stands

docs/about.md says that a document in SPDX's JSON-LD serialisation does not validate as it stands. Its keys outside Core carry their profile as a prefix, as in `software_packageVersion`, and its Elements refer to a CreationInfo by a blank-node identifier, where the schema takes the bare names and inlines CreationInfo. A Relationship's `from` key and an SpdxDocument's `import` key are Python keywords, so the example runner cannot load an object that holds them, though the validator checks it.

[^about.md]: docs/about.md, What the rendering adds, Where it differs from SPDX's serialisations, and Examples and tests
[^data-readme.md]: tests/data/README.md, the naming rule and the type CURIE
