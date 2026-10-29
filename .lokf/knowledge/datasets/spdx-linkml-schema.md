---
type: Dataset
id: https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-linkml-schema
genre: reference
title: spdx LinkML schema
description: "The LinkML schema of the SPDX 3.0.1 model (schema id `https://w3id.org/lmodel/spdx`, version 3.0.1): `spdx_linkml.yaml` imports one module per SPDX profile, 67 classes, 160 slots, 23 enums and 5 types in all, which scripts/spdx_to_linkml.py writes from the vendored model; its `lokf adapt` copy in `.lokf/spdx.yaml`, rooted on Element, is the bundle's domain schema."
resource: src/spdx_linkml/schema/spdx_linkml.yaml
derivedFrom:
  - https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-model-copy
references:
  - https://w3id.org/lmodel/spdx/knowledge/references/spdx-specification
sources:
  - id: spdx_linkml.yaml
    resource: src/spdx_linkml/schema/spdx_linkml.yaml
    title: the header, the prefixes and the imports
  - id: spdx_to_linkml.py
    resource: scripts/spdx_to_linkml.py
    title: the docstring, the constants and the summary it prints
  - id: about.md
    resource: docs/about.md
    title: Where the model comes from and What the rendering adds
  - id: project.justfile
    resource: project.justfile
    title: the gen-linkml, gen-linkml-check, lokf-adapt and lokf-adapt-check recipes
  - resource: src/spdx_linkml/schema
    title: the nine module files
  - resource: .lokf/spdx.yaml
    title: the header lokf adapt wrote and its notes
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the tool.lokf table
  - resource: src/spdx_linkml/__init__.py
    title: the package's import name
  - resource: src/spdx_linkml/schema/README.md
    title: the template's note on the folder
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# spdx LinkML schema

`src/spdx_linkml/schema/spdx_linkml.yaml` is the umbrella of the schema. Its header gives the id `https://w3id.org/lmodel/spdx`, the name `spdx_linkml`, the title "System Package Data Exchange (SPDX)", the version 3.0.1, the source `https://spdx.org/rdf/3.0.1/spdx-model.ttl` and the licence Apache-2.0.[^spdx_linkml.yaml] It adds nothing of its own: it imports the LinkML types and nine modules, one per SPDX profile, so an importer can import one profile alone.

## The modules

`scripts/spdx_to_linkml.py` writes every YAML file in the folder from the vendored model, so a change goes into the script or the model, never into the files.[^spdx_to_linkml.py] Its run prints 9 modules, 67 classes, 160 slots, 1 attribute and 23 enums. The modules are:

- `spdx_core`: 27 classes, 57 slots, 10 enums and the schema's 5 types. It imports only the LinkML types, and declares Extension and AnyLicenseInfo because Core's fields range over them.
- `spdx_software`: 6 classes, 17 slots and 4 enums, such as Package, File, Snippet and Sbom.
- `spdx_security`: 13 classes, 20 slots and 4 enums: Vulnerability and the assessment relationships.
- `spdx_simple_licensing` and `spdx_expanded_licensing`: 2 and 12 classes, the licence expressions, texts, licences, additions and sets.
- `spdx_ai` and `spdx_dataset`: AIPackage and DatasetPackage, with 3 and 1 classes, 20 and 13 slots, and 2 and 3 enums.
- `spdx_build`: the one class Build, with 9 slots.
- `spdx_extension`: 2 classes, the CycloneDX properties extension and its entry. Extension itself, the extension point on every Element, sits in `spdx_core`.

Each module imports the modules it references, and every class, slot, enum and permissible value keeps its SPDX IRI as `class_uri`, `slot_uri`, `enum_uri` or `meaning`, under a prefix per profile, such as `spdx_core` for `https://spdx.org/rdf/3.0.1/terms/Core/`. The root of SPDX 3.0.1's terms is bound as `spdx3`, because LOKF binds `spdx` to SPDX 2's namespace. What the schema adds lives under `spdx_linkml:`, `https://w3id.org/lmodel/spdx/`.

## The converter's rules

The script reads an OWL class whose individuals carry labels as an enum, and every other OWL class as a class. A class's SHACL property shapes are its fields, and every property is a top-level slot in the module of its namespace, with `slot_usage` where a class's use differs. Element carries the identifier `spdxId`, so a reference to an Element is its IRI, and the other classes are inlined where they are used. `type` is the type designator of every class without a parent, and its value is the class's CURIE, such as `spdx_core:Hash`. [Element names and the shared namespace](../explanations/element-names.md) says why the names are as they are.

docs/about.md lists what the rendering adds to the model: `spdxId`, `type`, the five patterned or bounded types, one module per profile and one subset per profile.[^about.md] It also says where the schema differs from SPDX's serialisations, which [Scope, influences and mappings](../explanations/scope-and-influences.md) sums up.

## Recipes and the adapt copy

`just gen-linkml` rewrites the schema from the vendored model, and `just gen-linkml-check` fails when a schema file differs from a fresh run.[^project.justfile] `just lokf-adapt` writes `.lokf/spdx.yaml`, the copy `lokf adapt` makes so the bundle can validate against the schema beside `lokf.yaml`, rooted on Element with the prefix `spdx` for the names it renames. `just lokf-adapt-check` fails when the copy is stale. `.lokf/justfile` names the copy on its `schema :=` line, and `.lokf/pyproject.toml` names it as `[tool.lokf] schema`. The Python package that holds the schema is `spdx_linkml`, and its distribution would be `spdx-linkml`.

[^spdx_linkml.yaml]: src/spdx_linkml/schema/spdx_linkml.yaml, the header, the prefixes and the imports
[^spdx_to_linkml.py]: scripts/spdx_to_linkml.py, the docstring, the constants and the summary it prints
[^about.md]: docs/about.md, Where the model comes from and What the rendering adds
[^project.justfile]: project.justfile, the `gen-linkml`, `gen-linkml-check`, `lokf-adapt` and `lokf-adapt-check` recipes
