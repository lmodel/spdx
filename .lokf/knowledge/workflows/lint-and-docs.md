---
type: Service
id: https://w3id.org/lmodel/spdx/knowledge/workflows/lint-and-docs
genre: reference
title: Lint & docs (lint-and-docs.yaml)
description: "The Lint & docs workflow, .github/workflows/lint-and-docs.yaml: on a push to main, every pull request, a Monday 06:00 UTC schedule and by hand, four jobs run ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), and markdownlint, lychee and codespell over the Markdown."
resource: .github/workflows/lint-and-docs.yaml
sources:
  - id: lint-and-docs.yaml
    resource: .github/workflows/lint-and-docs.yaml
    title: the header comment, the on key and the four jobs
  - id: lychee.toml
    resource: lychee.toml
    title: hidden, the exclude list and the excluded paths
  - resource: .markdownlint-cli2.jsonc
    title: the ignored folders and the rules turned off
  - resource: pyproject.toml
    title: the codespell and typos settings
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Lint & docs (lint-and-docs.yaml)

`.github/workflows/lint-and-docs.yaml` is the workflow named "Lint & docs". It runs static checks on the shell scripts, the workflows and the prose. A header comment says that it never touches the schema or the Python test suite, which [Build and test](main.md) checks, or the knowledge bundle's own semantics, which [Knowledge Registrar](knowledge-registrar.md) checks.[^lint-and-docs.yaml] It runs on a push to `main`, on every pull request, every Monday at 06:00 UTC to catch link rot without a pull request, and by hand.

Each of its four jobs runs on `ubuntu-latest` with `contents: read`, after harden-runner in audit mode and a checkout without persisted credentials:

- **`lint-scripts`**, named "Lint shell scripts", runs ShellCheck over the whole repository.
- **`lint-workflows`**, named "Lint GitHub Actions workflows", runs actionlint 1.7.12 from its container image, told to ignore the `copilot-requests` scope. A comment says that actionlint 1.7.12 predates that scope, which [Knowledge Librarian](knowledge-librarian.md) requests.
- **`word-budgets`**, named "Hold the governance files to their word budgets", fails when `CONTRIBUTING.md` has more than 1000 words or `SECURITY.md` more than 900. A comment says that the first is a checklist and the second a policy, not design logs.
- **`validate-markdown`**, named "Lint Markdown & check links", runs markdownlint-cli2 on every Markdown file against `.markdownlint-cli2.jsonc`, checks links with lychee, and runs codespell 2.4.2 on the Markdown files git tracks, with the settings in `pyproject.toml`. The lychee step maps the repository's own links on `main` to the checkout, so a pull request that moves a linked file fails here rather than after merge.

`lychee.toml` reads hidden folders too, so the links in `.lokf/knowledge/` are checked like the README's.[^lychee.toml] It leaves out this schema's namespace under `https://w3id.org/lmodel/spdx/` and SPDX's term namespace under `https://spdx.org/rdf/3.0.1/terms/`, because a term IRI is an identifier that need not resolve. It also leaves out the documentation site's address while the site moves from the mkdocs build to the knowledge website, and the SPDX examples, whose links are upstream's.

[^lint-and-docs.yaml]: .github/workflows/lint-and-docs.yaml, the header comment, the on key and the four jobs
[^lychee.toml]: lychee.toml, hidden, the exclude list and the excluded paths
