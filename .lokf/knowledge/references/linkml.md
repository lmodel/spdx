---
type: Reference
id: https://w3id.org/lmodel/spdx/knowledge/references/linkml
genre: reference
title: LinkML
description: "What the spdx repository takes from LinkML: the linkml-project-copier template at v0.5.0, LinkML 1.12.1 as uv.lock pins it, the generators gen-project and the recipes run, linkml-lint with the repository's own naming rule, and the runtime limits the tests and docs/about.md record."
resource: https://linkml.io/linkml/
sources:
  - id: copier-answers.yml
    resource: .copier-answers.yml
    title: the template's address and version
  - id: pyproject.toml
    resource: pyproject.toml
    title: the dependencies and the dev group
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the naming rule and its reasons
  - id: about.md
    resource: docs/about.md
    title: Where it differs from SPDX's serialisations, and Examples and tests
  - resource: uv.lock
    title: the locked linkml and linkml-runtime versions
  - resource: tests/test_rdf.py
    title: the strict expected failure
  - resource: justfile
    title: the lint recipe
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# LinkML

The repository was generated from the linkml-project-copier template, and `.copier-answers.yml` records its address, `https://github.com/linkml/linkml-project-copier`, and its version, v0.5.0.[^copier-answers.yml] `pyproject.toml` asks for `linkml-runtime` 1.9.4 or later at run time and `linkml` 1.9.3 or later for development, and `uv.lock` pins both at 1.12.1.[^pyproject.toml] [Generated artefacts](../datasets/generated-artefacts.md) lists the generators the recipes run.

## The linter

`just lint` runs `linkml-lint` over the schema folder, warnings included. `.linkmllint.yaml` takes LinkML's recommended rules and changes one, the naming rule.[^linkmllint.yaml] Slots follow SPDX's lowerCamelCase property names, and permissible values are SPDX's vocabulary entries as the JSON-LD serialisation writes them. `security_locator` keeps its underscore, because it is the JSON-LD key for the Security profile's locator, which Core also defines.

## The limits it records

docs/about.md names two ways in which RDF written from the schema's data differs from SPDX's RDF, both in LinkML 1.12.1.[^about.md] The Python runtime writes an `xsd:anyURI` value as an IRI, where SPDX's SHACL wants a literal, and `tests/test_rdf.py` holds that as a strict expected failure. The JSON-LD context writes `type` as an `xsd:anyURI` literal, which linkml pull request 4058 would map to `@type`. The same page says that a Relationship's `from` key and an SpdxDocument's `import` key are Python keywords, so the example runner cannot load the examples that use them, and they sit under `tests/data/problem/`.

[^copier-answers.yml]: .copier-answers.yml, `_src_path` and `_commit`
[^pyproject.toml]: pyproject.toml, the dependencies and the dev group
[^linkmllint.yaml]: .linkmllint.yaml, the naming rule and its reasons
[^about.md]: docs/about.md, Where it differs from SPDX's serialisations, and Examples and tests
