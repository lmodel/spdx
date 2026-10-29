---
type: Service
id: https://w3id.org/lmodel/spdx/knowledge/workflows/semantic-release
genre: reference
title: Semantic release (semantic-release.yml)
description: "The Semantic release workflow, .github/workflows/semantic-release.yml: on a pull request into main, its plan job checks that the commits, the changelog and the title would release and previews the release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub Release and dispatches Knowledge Release."
resource: .github/workflows/semantic-release.yml
relatedTo:
  - https://w3id.org/lmodel/spdx/knowledge/playbooks/release
sources:
  - id: semantic-release.yml
    resource: .github/workflows/semantic-release.yml
    title: the header comment, the on key and both jobs
  - resource: .releaserc.json
    title: the release rules and the plugins
  - resource: .github/scripts/changelog-release.mjs
    title: the check, notes and promote commands
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Semantic release (semantic-release.yml)

`.github/workflows/semantic-release.yml` is the workflow named "Semantic release". A header comment says that it computes the next version from Conventional Commits on `main`, promotes `CHANGELOG.md`'s Unreleased section into a dated heading through `.github/scripts/changelog-release.mjs`, tags the commit and publishes a GitHub Release built from the same text.[^semantic-release.yml] It runs on a pull request into `main` that is opened, synchronized, reopened or edited, and on a push to `main`. No file carries the version, so `CHANGELOG.md` is the only file it commits.

## The plan job, on a pull request

The `plan` job has `contents: read` and writes nothing. It installs pinned semantic-release packages with `--ignore-scripts`, and reads whether the commits would release: a `feat`, `fix` or `security` commit, or one marked breaking. When they would, it refuses to go on without a `v*` tag, refuses an empty Unreleased section, and refuses a pull request title without a releasing type, since a squash merge takes its subject from the title. Last, it previews the release with `semantic-release --dry-run`. A comment says that the `edited` type is there so that retitling a pull request runs the title check again.

## The release job, on a push to main

The `release` job runs in the `release` GitHub Environment with `contents: write` and `actions: write`. It refuses to run without a `v*` tag, then runs semantic-release, committing as `github-actions[bot]`. Once a version is released and the repository variable `KNOWLEDGE_RELEASE_ENABLED` is `true`, it dispatches [Knowledge Release](knowledge-release.md) for the new tag. A comment says that GitHub starts no workflow from a release made with the job's `GITHUB_TOKEN`, so a dispatch is how the knowledge release runs.

A header comment asks that required reviewers be configured on the `release` Environment in the repository's own settings, or every qualifying merge to `main` cuts a release with no human step in between. [Release the schema](../playbooks/release.md) gives the whole procedure.

[^semantic-release.yml]: .github/workflows/semantic-release.yml, the header comment, the on key and both jobs
