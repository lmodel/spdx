---
type: Service
id: https://w3id.org/lmodel/spdx/knowledge/workflows/main
genre: reference
title: Build and test (main.yaml)
description: "The Build and test workflow, .github/workflows/main.yaml: on a push to main and on every pull request, its test job runs just test on Python 3.10 to 3.14, and on 3.13 also just lint and just lokf-adapt-check, the check that .lokf/spdx.yaml is current."
resource: .github/workflows/main.yaml
relatedTo:
  - https://w3id.org/lmodel/spdx/knowledge/datasets/test-data
  - https://w3id.org/lmodel/spdx/knowledge/playbooks/regenerate-and-test
sources:
  - id: main.yaml
    resource: .github/workflows/main.yaml
    title: the on key, the concurrency group and the test job
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Build and test (main.yaml)

`.github/workflows/main.yaml` is the workflow named "Build and test". It runs on a push to `main` and on every pull request, and a newer run on the same ref cancels an older one.[^main.yaml] The file sets `permissions: {}` at the top, and its one job asks for `contents: read`. A comment says that it was built from GitHub's guide to building and testing Python.

## The test job

The `test` job runs on `ubuntu-latest` once for each Python version from 3.10 to 3.14, and a failure on one version does not stop the others. It hardens the runner with harden-runner in audit mode, checks the repository out without persisting credentials, installs uv, Python and just, and installs the project with `uv sync --locked --group dev`. It then runs:

- `just lint`, on Python 3.13 only, which reports warnings as well as errors;
- `just test`, on every version;
- `uv sync --locked --project .lokf` and `just lokf-adapt-check`, on Python 3.13 only. A comment says that `.lokf/spdx.yaml` is the copy the knowledge bundle validates against and the release attaches, so it must match the schema and `lokf.yaml`.

[Regenerate and test the schema](../playbooks/regenerate-and-test.md) says what each recipe runs, and [Test data and schema tests](../datasets/test-data.md) what `just test` checks.

[^main.yaml]: .github/workflows/main.yaml, the on key, the concurrency group and the test job
