---
type: Playbook
id: https://w3id.org/lmodel/spdx/knowledge/playbooks/release
genre: how-to
title: Release the schema
description: How a releasing commit merged to main makes semantic-release promote the changelog's Unreleased section, tag vX.Y.Z and publish a GitHub Release, then dispatch the Knowledge Release workflow once KNOWLEDGE_RELEASE_ENABLED is true; below 1.0.0 from a v0.0.0 baseline tag, with a breaking change as a minor bump and nothing published to PyPI.
resource: CONTRIBUTING.md
relatedTo:
  - https://w3id.org/lmodel/spdx/knowledge/workflows/semantic-release
  - https://w3id.org/lmodel/spdx/knowledge/workflows/knowledge-release
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Releasing (maintainers)
  - id: changelog.md
    resource: CHANGELOG.md
    title: the opening note and the Unreleased section
  - id: releaserc.json
    resource: .releaserc.json
    title: the release rules and the plugins
  - resource: .github/scripts/changelog-release.mjs
    title: the check, notes and promote commands
  - resource: .copier-answers.yml
    title: the gh_action_pypi answer
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Release the schema

## As you work

Write each change that alters behaviour under `## [Unreleased]` in `CHANGELOG.md`; the release job refuses an empty section, which `.github/scripts/changelog-release.mjs check` tests.[^contributing.md] Type each commit as a Conventional Commit for what the change is. Only `feat:`, `fix:`, `security:` and a breaking `!` start a release, and other types leave their entries for the next release that does. A pull request that would release carries a releasing type in its title too, since a squash merge takes its subject from it.

## On merge

[Semantic release](../workflows/semantic-release.md) retitles the Unreleased section to `## [X.Y.Z] - YYYY-MM-DD`, commits `CHANGELOG.md`, tags `vX.Y.Z` and publishes the GitHub Release. No file is bumped. Once `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches [Knowledge Release](../workflows/knowledge-release.md), which attaches the schema copy and the bundle when the bundle changed. Run that workflow by hand with `force` when only the schema changed. The release step runs behind the `release` GitHub Environment, and CONTRIBUTING.md asks that required reviewers be set on it, or every qualifying merge releases unattended.

## Below 1.0.0

Push the `v0.0.0` baseline tag on `main` before the first releasing merge, which then releases 0.1.0. Both release jobs refuse to run without a `v*` tag, since semantic-release would otherwise start at 1.0.0. `CHANGELOG.md` says that `v0.0.0` is a baseline, not a release.[^changelog.md] `.releaserc.json` uses the conventionalcommits preset, maps a breaking change to a minor release and a `security` commit to a patch, and lets semantic-release commit only `CHANGELOG.md`.[^releaserc.json] Reaching 1.0.0 means removing the breaking rule in a pull request of its own.

## What it does not do

PyPI publishing is off: the template's `gh_action_pypi` answer is `false`, and the distribution would be `spdx-linkml`. A branch rule that requires pull requests, status checks or signed commits would reject the release job's own push to `main`, so CONTRIBUTING.md asks that they stay off and points to SECURITY.md for what holds `main` instead.

[^contributing.md]: CONTRIBUTING.md, Releasing (maintainers)
[^changelog.md]: CHANGELOG.md, the opening note and the Unreleased section
[^releaserc.json]: .releaserc.json, the release rules and the plugins
