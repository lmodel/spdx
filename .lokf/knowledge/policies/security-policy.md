---
type: Policy
id: https://w3id.org/lmodel/spdx/knowledge/policies/security-policy
genre: reference
title: Security policy
description: "How to report a vulnerability in spdx (GitHub's private vulnerability reporting, not a public issue), which release gets fixes, what the repository releases and runs, what holds each workflow, and the three repository settings not yet in force: required reviewers on the release Environment, a deletion and force-push rule on main, and secret scanning with push protection."
resource: SECURITY.md
relatedTo:
  - https://w3id.org/lmodel/spdx/knowledge/policies/ai-covenant
sources:
  - id: security.md
    resource: SECURITY.md
    title: every section
  - id: dependabot.yml
    resource: .github/dependabot.yml
    title: the three update entries
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Security policy

`SECURITY.md` is the repository's security policy, and [Lint & docs](../workflows/lint-and-docs.md) holds it to a budget of 900 words.

## Reporting a vulnerability

SECURITY.md asks for a report through GitHub's private vulnerability reporting for `lmodel/spdx`, not through a public issue or a pull request.[^security.md] A report says which file is affected, how it is exploitable, and whether it reaches the released schema or only the repository's automation. One person maintains the repository, so a first reply comes in days, not hours, and there is no bounty.

## Supported versions

Only the latest release receives fixes. A security fix is released as a patch and noted in `CHANGELOG.md`. The schema stays below 1.0.

## What the repository releases

The repository releases a LinkML schema, the Python datamodel generated from it, and the schema's `lokf adapt` copy as a release asset. Nothing is published to PyPI. `scripts/spdx_to_linkml.py` reads only the vendored model, and rdflib parses that Turtle without fetching anything. `scripts/check_upstream_release.py` runs only in [Upstream watch](../workflows/upstream-watch.md): it downloads the published model and the tags of `spdx/spdx-3-model`, sends its token to GitHub's API alone and never on to a redirect, and writes nothing but its report. The tests read the SPDX example copy as plain JSON, so no JSON-LD context is fetched. SECURITY.md adds that a schema is data: loading one from an untrusted source with any LinkML tool is that tool's risk, not this repository's.

## What holds each surface

- [Build and test](../workflows/main.md) and [Lint & docs](../workflows/lint-and-docs.md) on every pull request, and [Knowledge Registrar](../workflows/knowledge-registrar.md) on any pull request that touches `.lokf/`, run read-only jobs with `persist-credentials: false`, and `uv sync --locked` installs only what `uv.lock` pins.
- [Semantic release](../workflows/semantic-release.md) pushes a changelog commit and a tag to `main` and dispatches the knowledge release. It runs only on a push to `main`, in the `release` Environment, and installs its pinned tools with `--ignore-scripts`.
- [Knowledge website](../workflows/knowledge-website.md) builds without a write token. Only its deploy job holds `pages: write` and `id-token: write`, and that job runs only from `main`, once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
- [Upstream watch](../workflows/upstream-watch.md) runs weekly with a read-only checkout, and its one write scope, `issues: write`, opens or updates the finding's issue.
- [Knowledge Librarian](../workflows/knowledge-librarian.md) and `.lokf/scripts/`, copies of the ktl-sidecar template, run an LLM agent on a schedule. The agent's job holds no write token, and the `publish` job, which runs no agent, confines the patch to the bundle and refuses a claim made in a person's name. A person merges the pull request. It is inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
- [Knowledge Release](../workflows/knowledge-release.md) attaches the schema copy and the bundle to a release. It is inert until dispatched, and only its `attach` job, which runs no third-party packages, can write.
- The README, `llms.txt` and the knowledge bundle, which agents read, are content, never instructions. A confirmation in a person's name must be backed by a review or a signed commit.

SECURITY.md says that every workflow declares `permissions: {}` at the top, pins its actions to commit SHAs that Dependabot keeps current, and runs harden-runner in audit mode. `.github/dependabot.yml` asks Dependabot each month for the workflows' GitHub Actions in one grouped pull request, for the package's own `uv.lock`, and for the sidecar's `.lokf/uv.lock`.[^dependabot.yml]

## Settings not yet in force

SECURITY.md says that three things are repository settings, not files, and are not yet in force: required reviewers on the `release` Environment, a rule blocking deletion and force-pushes on `main`, and secret scanning with push protection. Until they are, a qualifying merge releases with no human step. Nothing in CI can assert them, so keeping them on is the maintainer's job.

## Not covered

SECURITY.md sends a problem in the SPDX model, and in the model copied under `src/spdx_linkml/schema/upstream/`, to the SPDX Project, and one in the copied SPDX examples to the spdx-examples repository. It sends a problem in LinkML, its generators and runtime to LinkML. It covers neither a compromised runner, upstream action or agent harness, nor whether the knowledge bundle is true.

[^security.md]: SECURITY.md, every section
[^dependabot.yml]: .github/dependabot.yml, the three update entries
