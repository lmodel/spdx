---
type: Service
id: https://w3id.org/lmodel/spdx/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The Upstream watch workflow, .github/workflows/upstream-watch.yaml: every Monday at 07:00 UTC and by hand, it runs scripts/check_upstream_release.py, which compares the vendored SPDX model with the published 3.0.1 file and spdx/spdx-3-model's tags, and on a finding opens or updates the issue titled Upstream watch: the SPDX release has changed."
resource: .github/workflows/upstream-watch.yaml
relatedTo:
  - https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-model-copy
  - https://w3id.org/lmodel/spdx/knowledge/playbooks/move-to-a-new-spdx-release
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
    title: the header comment, the on key and the spdx-release job
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring and the check function
  - id: report-issue.sh
    resource: .github/scripts/report-issue.sh
    title: the header comment and the body it writes
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

`.github/workflows/upstream-watch.yaml` is the workflow named "Upstream watch". A header comment says that it checks weekly what the repository is built from but does not control: the SPDX model the SPDX Project publishes.[^upstream-watch.yaml] Nothing in a pull request can change that model, so it runs on a schedule: every Monday at 07:00 UTC, and by hand.

Its one job, `spdx-release`, named "SPDX model is current and intact", runs on `ubuntu-latest` with `contents: read` and `issues: write`. It runs `scripts/check_upstream_release.py` with the job's token, using only Python's standard library, so the runner's Python is enough.

## What the script checks

The script reads the SPDX version from the vendored model's ontology IRI, downloads the model the SPDX Project publishes for that version, and compares the two byte for byte.[^check_upstream_release.py] It then reads the tags of `spdx/spdx-3-model` to see whether a newer release exists. It fails when the files differ or a newer release exists. A release candidate newer than every release is reported, such as `3.1-rc1` today, and does not fail the check. It sends `GITHUB_TOKEN` to GitHub's API only, and not on to a host the API redirects to.

## The issue

When the check fails, `.github/scripts/report-issue.sh` opens an issue titled "Upstream watch: the SPDX release has changed", or comments on the open issue with that title. The body is the check's report, or a note that the check stopped before writing one, and a link to the run.[^report-issue.sh] So a weekly finding is one issue, and does not depend on anyone reading the run log.

[SPDX model copy](../datasets/spdx-model-copy.md) says what the script compares, and [Move to a new SPDX release](../playbooks/move-to-a-new-spdx-release.md) says what to do about the issue.

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml, the header comment, the on key and the spdx-release job
[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring and the check function
[^report-issue.sh]: .github/scripts/report-issue.sh, the header comment and the body it writes
