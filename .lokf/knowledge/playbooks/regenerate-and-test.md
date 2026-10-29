---
type: Playbook
id: https://w3id.org/lmodel/spdx/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test the schema
description: "How to change the spdx schema: set up with uv and just, change scripts/spdx_to_linkml.py rather than the schema files, regenerate with just gen-linkml, gen-project, gen-doc and lokf-adapt, add examples, then run the checks CI runs (just test on Python 3.10 to 3.14, just lint and just lokf-adapt-check on 3.13) and the pre-commit hooks."
resource: CONTRIBUTING.md
relatedTo:
  - https://w3id.org/lmodel/spdx/knowledge/workflows/main
  - https://w3id.org/lmodel/spdx/knowledge/datasets/test-data
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Development setup and Before opening a pull request
  - id: justfile
    resource: justfile
    title: the install, gen-project, gen-doc, lint and test recipes
  - id: project.justfile
    resource: project.justfile
    title: every recipe
  - id: pre-commit-config.yaml
    resource: .pre-commit-config.yaml
    title: the exclude list and the hooks
  - resource: .yamllint.yaml
    title: the files yamllint leaves out
  - resource: config.public.mk
    title: the environment the justfile loads
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Regenerate and test the schema

## Set up

CONTRIBUTING.md asks for Python 3.10 or later, uv and just, then `uv sync --group dev` in a clone of `lmodel/spdx`, and `just --list` to see the recipes.[^contributing.md] `just install` runs the same `uv sync`.[^justfile]

## Change the converter, then regenerate

1. Change `scripts/spdx_to_linkml.py`, never the files under `src/spdx_linkml/schema/`, which the converter writes.
2. Run `just gen-linkml` to rewrite the schema from the vendored model.[^project.justfile] `just gen-linkml-check` fails when the schema differs from a fresh run, as `tests/test_schema_is_generated.py` does.
3. Run `just gen-project` to regenerate `project/` and the Python models, and `just gen-doc` to regenerate `docs/schema/` and the element pages.
4. Run `just lokf-adapt` to rewrite `.lokf/spdx.yaml`, the bundle's domain schema.
5. Commit what the recipes wrote with the change.

## Add examples

Put a valid example in `tests/data/valid/` and a counter-example for each new constraint in `tests/data/invalid/`, named `<Class>-<anything>.yaml`, as [Test data and schema tests](../datasets/test-data.md) describes. An example with a `from` or `import` key goes under `tests/data/problem/`.

## Run the checks

- `just test` generates the project into `tmp/`, regenerates the Python models and runs pytest, and runs `linkml-run-examples` over the examples. `just test-data` runs the data tests alone.
- `just lint` runs `linkml-lint` over the schema, with the rules `.linkmllint.yaml` sets.
- `just lokf-adapt-check` fails when `.lokf/spdx.yaml` is stale against the schema or `.lokf/lokf.yaml`.
- `just upstream-check` compares the vendored model with the SPDX Project's releases.
- `uvx pre-commit run` runs the hooks on what is staged: the file checks, yamllint, codespell, typos, ruff and the `uv.lock` check. `.pre-commit-config.yaml` keeps every hook off the files the repository does not write by hand: the model copy, the SPDX examples, the schema, the generated files, the sidecar's scripts, the adapt copies and the neighbour copies.[^pre-commit-config.yaml]

[Build and test](../workflows/main.md) runs `just test` on Python 3.10 to 3.14, and `just lint` and `just lokf-adapt-check` on Python 3.13, on every pull request.

[^contributing.md]: CONTRIBUTING.md, Development setup and Before opening a pull request
[^justfile]: justfile, the `install`, `gen-project`, `gen-doc`, `lint` and `test` recipes
[^project.justfile]: project.justfile, every recipe
[^pre-commit-config.yaml]: .pre-commit-config.yaml, the exclude list and the hooks
