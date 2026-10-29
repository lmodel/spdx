---
type: Playbook
id: https://w3id.org/lmodel/spdx/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose."
resource: .
sources:
  - resource: README.md
  - resource: docs/about.md
  - resource: docs/index.md
  - resource: src/spdx_linkml
  - resource: scripts
  - resource: tests
  - resource: project
  - resource: docs/schema
  - resource: docs/elements
  - resource: examples/README.md
  - resource: .github/workflows
  - resource: .github/scripts
  - resource: .github/dependabot.yml
  - resource: .github/PULL_REQUEST_TEMPLATE/knowledge-sync.md
  - resource: justfile
  - resource: project.justfile
  - resource: config.yaml
  - resource: config.public.mk
  - resource: .linkmllint.yaml
  - resource: pyproject.toml
  - resource: uv.lock
  - resource: .copier-answers.yml
  - resource: .pre-commit-config.yaml
  - resource: .yamllint.yaml
  - resource: lychee.toml
  - resource: .markdownlint-cli2.jsonc
  - resource: NOTICE
  - resource: LICENSE
  - resource: SECURITY.md
  - resource: AI_COVENANT.md
  - resource: CONTRIBUTING.md
  - resource: CHANGELOG.md
  - resource: .releaserc.json
  - resource: website
  - resource: .lokf/spdx.yaml
  - resource: .lokf/lokf.yaml
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: https://spdx.github.io/spdx-spec/v3.0.1/
  - resource: https://linkml.io/linkml/
exclusions:
  - resource: CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, with only the maintainer's address filled in; it states nothing about the schema or the repository's tooling.
  - resource: .editorconfig
    reason: Editor settings for indentation and line endings, which no concept needs.
  - resource: .gitignore
    reason: What git leaves out; the concepts that cite the generated folders already say which are committed.
  - resource: docs/templates-linkml
    reason: The template's note on gen-doc's own templates, which the website leaves out.
  - resource: src/README.md
    reason: The template's one-line note on the source folder.
  - resource: .github/ISSUE_TEMPLATE
    reason: Forms for bug reports and feature requests, which restate CONTRIBUTING.md and the AI covenant.
  - resource: .github/pull_request_template.md
    reason: The pull request form, whose checklist restates CONTRIBUTING.md.
  - resource: llms.txt
    reason: A pointer for agents to this bundle and the docent skill; it says nothing the bundle does not.
  - resource: knowledge_bundle
    reason: A link to .lokf/knowledge, the bundle itself.
  - resource: .lokf/scripts
    reason: Copies of the ktl-sidecar templates, which NOTICE credits and the knowledge workflows' concepts describe by what runs them.
  - resource: .lokf/m365
    reason: Copies of the ktl-sidecar templates for the Microsoft 365 Copilot skills, which Knowledge Release packs.
  - resource: .lokf/README.md
    reason: The sidecar template's guide to the bundle's own folder.
  - resource: .lokf/queries.http
    reason: Sample SPARQL queries from the sidecar template.
  - resource: .lokf/ingest.yaml.sample
    reason: The sidecar template's example manifest for the ingest, which this repository does not use.
  - resource: .lokf/uv.lock
    reason: The lock of the sidecar's toolkit, whose floor .lokf/pyproject.toml states.
  - resource: .lokf/.gitignore
    reason: What git leaves out of the sidecar folder, from the template.
  - resource: .lokf/.gitattributes
    reason: The line-ending rule for the sidecar folder, from the template.
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Knowledge sources map

This map lists where the bundle's concepts come from, in this repository and outside it, and how to re-check each source on a refresh run. Each path is written from the repository root.

## In the repository

| Source | Concepts it yields | How to re-check it |
| --- | --- | --- |
| `README.md` | Scope, influences and mappings; spdx documentation site; SPDX specification 3.0.1; License and attribution; Knowledge Release; Element names and the shared namespace | Read What it models, Influences, Mappings, Not modelled here and the Knowledge Trust Ladder (KTL) section. |
| `docs/about.md`, `docs/index.md` | spdx LinkML schema; Scope, influences and mappings; LinkML; Validate data against the schema; Move to a new SPDX release | Read What the rendering adds, Where it differs from SPDX's serialisations, the steps to a new release and Examples and tests. |
| `src/spdx_linkml/` | spdx LinkML schema; SPDX model copy; Generated artefacts | Run `just gen-linkml-check`, and read the umbrella's header and each module's counts. |
| `scripts/` | spdx LinkML schema; Element names and the shared namespace; Upstream watch; Move to a new SPDX release | Read the converter's docstring and constants, and run `just upstream-check`. |
| `tests/` | Test data and schema tests; SPDX examples copy | Count the files in each `tests/data/` folder and read each test file's functions. |
| `project/`, `docs/schema/`, `docs/elements/` | Generated artefacts | Compare the folders with what `just gen-project` and `just gen-doc` write. |
| `.github/workflows/`, `.github/scripts/`, `.github/dependabot.yml`, `.github/PULL_REQUEST_TEMPLATE/knowledge-sync.md` | one concept per workflow; Security policy | Read each workflow's header comment, its `on` key and its jobs. |
| `justfile`, `project.justfile`, `config.yaml`, `config.public.mk` | Regenerate and test the schema; Generated artefacts; spdx LinkML schema | Read the recipes and the generator settings. |
| `.linkmllint.yaml`, `pyproject.toml`, `uv.lock`, `.copier-answers.yml` | LinkML; Element names and the shared namespace; License and attribution | Read the naming rule, the dependencies, the locked versions and the template's version. |
| `.pre-commit-config.yaml`, `.yamllint.yaml`, `lychee.toml`, `.markdownlint-cli2.jsonc` | Regenerate and test the schema; Lint & docs | Read each file's exclusions and their comments. |
| `NOTICE`, `LICENSE`, `SECURITY.md`, `AI_COVENANT.md`, `CONTRIBUTING.md` | License and attribution; Security policy; AI covenant; Regenerate and test the schema; Release the schema | Read each section. |
| `CHANGELOG.md`, `.releaserc.json` | Release the schema | Read the opening note, the Unreleased section and the release rules. |
| `website/` | spdx documentation site | Read `website/README.md` and `website/site.config.mjs`. |
| `.lokf/spdx.yaml`, `.lokf/lokf.yaml`, `.lokf/justfile`, `.lokf/pyproject.toml` | spdx LinkML schema; Element names and the shared namespace | Run `just lokf-adapt-check`, and read the `schema :=` line and the `[tool.lokf]` table. |

## Outside the repository

| Source | Concepts it yields | How to re-check it |
| --- | --- | --- |
| `https://spdx.github.io/spdx-spec/v3.0.1/` | SPDX specification 3.0.1 | Open the specification's pages that the schema's `see_also` links. |
| `https://linkml.io/linkml/` | LinkML | Compare what the repository's files say about LinkML with LinkML's documentation for the locked version. |

The exclusions in the frontmatter name the paths looked at and left out, each with its reason.
