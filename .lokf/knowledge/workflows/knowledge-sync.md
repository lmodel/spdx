---
type: Service
id: https://w3id.org/lmodel/spdx/knowledge/workflows/knowledge-sync
genre: reference
title: Knowledge sync (knowledge-sync.yaml)
description: "The Knowledge sync workflow, .github/workflows/knowledge-sync.yaml: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request from the knowledge-sync branch, opened with the KNOWLEDGE_SYNC_TOKEN secret, and holds the workflow changes for a person to apply."
resource: .github/workflows/knowledge-sync.yaml
relatedTo:
  - https://w3id.org/lmodel/spdx/knowledge/workflows/knowledge-librarian
sources:
  - id: knowledge-sync.yaml
    resource: .github/workflows/knowledge-sync.yaml
    title: the header comment, the on key and the five jobs
  - id: notice
    resource: NOTICE
    title: the Knowledge bundle section
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: the item on the skills pin
  - resource: .github/PULL_REQUEST_TEMPLATE/knowledge-sync.md
    title: the sync pull request's template
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Knowledge sync (knowledge-sync.yaml)

`.github/workflows/knowledge-sync.yaml` is the workflow named "Knowledge sync". A header comment says that it keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, the repository that publishes the skills.[^knowledge-sync.yaml] NOTICE says that it is a copy of a ktl-sidecar template from that repository.[^notice] It runs by hand and every Monday at 04:10 UTC, so that the librarian's Monday run follows a current pin once the pull request is merged. It runs no LLM or agent and no code from the release, and it never pushes to the default branch or merges.

## Its jobs

- **`earlier`** reads the pin in `knowledge-librarian.yaml`, the newest Knowledge Trust Ladder release, and the state of the workflow's branch and last pull request, with `contents: read` and `pull-requests: read`. It is skipped in the Knowledge Trust Ladder repository itself.
- **`sync`** runs when the pin is behind, under a read-only token. It runs this repository's own `.lokf/scripts/knowledge-sync.sh`, which clones the release, reads its `knowledge-sync.manifest`, copies the templates over the repository's copies, moves the pin and writes the changelog entry.
- **`publish`** applies the change with the default branch's copy of the script, which refuses any path or change a sync may not make, and opens or refreshes one pull request from the `knowledge-sync` branch. It runs in the `knowledge-sync` Environment and pushes with the `KNOWLEDGE_SYNC_TOKEN` secret, because the pin is under `.github/workflows/`, which the job's own token may not push. Without the secret it attaches the patch to the run and opens nothing.
- **`review`** and **`push-workflows`** are optional. The workflow changes a release brings are held, not pushed, and a person applies them after reading them. With `KNOWLEDGE_SYNC_REVIEW_ENVIRONMENT` naming an Environment with required reviewers, `review` waits for a reviewer and `push-workflows` then pushes the changes as a second commit.

CONTRIBUTING.md says that when `TRUST_LADDER_SKILLS_REF` moves in `knowledge-librarian.yaml`, the other `knowledge-*.yaml` workflows, `.lokf/scripts/` and `.lokf/m365/` move with it, copied from that release's `skills/ktl-sidecar/templates/` in the same pull request.[^contributing.md] [Knowledge Librarian](knowledge-librarian.md) holds the pin.

[^knowledge-sync.yaml]: .github/workflows/knowledge-sync.yaml, the header comment, the on key and the five jobs
[^notice]: NOTICE, the Knowledge bundle section
[^contributing.md]: CONTRIBUTING.md, the item on the skills pin
