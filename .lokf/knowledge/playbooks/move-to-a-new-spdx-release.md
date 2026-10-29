---
type: Playbook
id: https://w3id.org/lmodel/spdx/knowledge/playbooks/move-to-a-new-spdx-release
genre: how-to
title: Move to a new SPDX release
description: "What to do when the upstream watch opens its issue: replace src/spdx_linkml/schema/upstream/spdx-model.ttl whole with the model the SPDX Project publishes for the new release, run just gen-linkml, then just lint, gen-project, gen-doc, lokf-adapt and test, and move the release's number and addresses in NOTICE, the README and lychee.toml."
resource: docs/about.md
relatedTo:
  - https://w3id.org/lmodel/spdx/knowledge/workflows/upstream-watch
  - https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-model-copy
sources:
  - id: about.md
    resource: docs/about.md
    title: Where the model comes from and the steps to a new release
  - id: spdx_to_linkml.py
    resource: scripts/spdx_to_linkml.py
    title: the version read from the ontology IRI
  - id: notice
    resource: NOTICE
    title: The SPDX 3.0.1 model, by the SPDX Project
  - resource: README.md
    title: What it models
  - resource: lychee.toml
    title: the SPDX term namespace in exclude
  - resource: CONTRIBUTING.md
    title: the item on the upstream copy
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Move to a new SPDX release

[Upstream watch](../workflows/upstream-watch.md) opens an issue when the vendored model differs from the published one, or when the SPDX Project tags a newer release. A release candidate is reported and opens no issue.

## The steps

docs/about.md gives three steps to move to a new SPDX release:[^about.md]

1. Replace the vendored file, `src/spdx_linkml/schema/upstream/spdx-model.ttl`, with the one the SPDX Project publishes for the release.
2. Run `just gen-linkml`.
3. Run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`.

`scripts/spdx_to_linkml.py` reads the SPDX version from the model's ontology IRI, and writes it into each module's `version`, `source` and `see_also` and into the profile prefixes, so the schema follows the new file without a change to the script.[^spdx_to_linkml.py] A model the converter cannot read, such as a datatype it has no range for, stops the run with a message that names the element.

## What else names the release

NOTICE names version 3.0.1 and the address the model was retrieved from, the README says that the schema models 3.0.1, and `lychee.toml` leaves out the 3.0.1 term namespace.[^notice] Move each to the new release in the same pull request, and say in `CHANGELOG.md` what the new release changes. CONTRIBUTING.md asks that the copy be replaced whole from one release, never edited.

[^about.md]: docs/about.md, Where the model comes from and the steps to a new release
[^spdx_to_linkml.py]: scripts/spdx_to_linkml.py, the version read from the ontology IRI
[^notice]: NOTICE, The SPDX 3.0.1 model, by the SPDX Project
