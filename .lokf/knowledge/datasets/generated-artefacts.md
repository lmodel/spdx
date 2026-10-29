---
type: Dataset
id: https://w3id.org/lmodel/spdx/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "Files generated from the spdx schema and never edited by hand: project/ (Excel, GraphQL, Java, JSON-LD, JSON Schema, OWL, a prefix map, protobuf, SHACL, ShEx, SQL and TypeScript), the dataclass and Pydantic models in src/spdx_linkml/datamodel/, the merged schema in docs/schema/, the gen-doc pages in docs/elements/ and the domain schema copy .lokf/spdx.yaml."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project, gen-python, gen-doc and _gen-yaml recipes
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: the generators gen-project runs and their arguments
  - id: config.public.mk
    resource: config.public.mk
    title: the schema name, folder and generator arguments
  - resource: project/README.md
    title: the folder's note
  - resource: src/spdx_linkml/datamodel
    title: the dataclass and Pydantic models
  - resource: docs/schema/spdx_linkml.yaml
    title: the merged schema
  - resource: .lokf/spdx.yaml
    title: the adapt copy
  - resource: project.justfile
    title: the lokf-adapt recipe
  - resource: .pre-commit-config.yaml
    title: the exclude list
generated:
  by: process:ktl-librarian
  at: "2026-10-29T20:52:45Z"
status: draft
---

# Generated artefacts

Every file here comes from the schema, and a change goes into the converter, after which the recipes regenerate the files.

## project/

`just gen-project` runs LinkML's `gen-project` with `.linkml/generators.yaml` into `project/`, moves the Python files it writes into `src/spdx_linkml/datamodel/`, and writes the Pydantic model there with `gen-pydantic`.[^justfile] It then runs `gen-java`, `gen-typescript` and `gen-owl` on their own, because those generators ignore the configuration file or cannot make a folder. `.linkml/generators.yaml` turns the Markdown generator off and passes `mergeimports` to the others, and repeats for `gen-project` the OWL choices that `config.public.mk` gives `gen-owl`.[^generators.yaml] `config.public.mk` names the schema `spdx_linkml` in `src/spdx_linkml/schema`, and asks `gen-owl` to skip the vacuous axioms and to consolidate cardinality axioms.[^config.public.mk]

The folder holds `excel/`, `graphql/`, `java/`, `jsonld/` (the schema and its JSON-LD context), `jsonschema/`, `owl/`, `prefixmap/`, `protobuf/`, `shacl/`, `shex/`, `sqlschema/` and `typescript/`.

## The Python models

`src/spdx_linkml/datamodel/` holds `spdx_linkml.py`, the dataclasses, and `spdx_linkml_pydantic.py`, the Pydantic model. `just test` regenerates the dataclasses before it runs pytest.

## The documentation's schema files

`just gen-doc` writes `docs/schema/spdx_linkml.yaml`, the schema with its modules folded in by `gen-yaml`, and the element pages in `docs/elements/`, which git ignores and the website builds when they are missing.

## The adapt copy

`just lokf-adapt` writes `.lokf/spdx.yaml` from the schema with lokf 0.9.0's `adapt`, and `just lokf-adapt-check` holds it to the schema. [spdx LinkML schema](spdx-linkml-schema.md) says what the copy changes. `.pre-commit-config.yaml` keeps every hook off these files, which the next run would rewrite back.

[^justfile]: justfile, the `gen-project`, `gen-python`, `gen-doc` and `_gen-yaml` recipes
[^generators.yaml]: .linkml/generators.yaml, the generators gen-project runs and their arguments
[^config.public.mk]: config.public.mk, the schema name, folder and generator arguments
