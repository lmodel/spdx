---
type: Dataset
id: https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-model-copy
genre: reference
title: SPDX model copy
description: "`src/spdx_linkml/schema/upstream/spdx-model.ttl`, the SPDX Project's 3.0.1 model in OWL and SHACL as Turtle, retrieved from spdx.org under the Community Specification License 1.0; never edited here, the converter's only input, and compared byte for byte with the published file every week."
resource: src/spdx_linkml/schema/upstream/spdx-model.ttl
source:
  - https://spdx.org/rdf/3.0.1/spdx-model.ttl
references:
  - https://w3id.org/lmodel/spdx/knowledge/references/spdx-specification
sources:
  - id: spdx-model.ttl
    resource: src/spdx_linkml/schema/upstream/spdx-model.ttl
    title: the ontology header
  - id: notice
    resource: NOTICE
    title: The SPDX 3.0.1 model, by the SPDX Project
  - id: check_upstream_release.py
    resource: scripts/check_upstream_release.py
    title: the docstring and the check function
  - resource: docs/about.md
    title: Where the model comes from
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# SPDX model copy

`src/spdx_linkml/schema/upstream/spdx-model.ttl` is the SPDX Project's model of SPDX 3.0.1, in OWL and SHACL as Turtle. Its ontology header names it "System Package Data Exchange (SPDX) Ontology", created on 2024-04-05 by the SPDX Project, with the term namespace `https://spdx.org/rdf/3.0.1/terms/` and the licence `https://spdx.org/licenses/Community-Spec-1.0.html`.[^spdx-model.ttl] It carries the copyright "Copyright (C) 2024 SPDX Project".

NOTICE says that the file was retrieved from `https://spdx.org/rdf/3.0.1/spdx-model.ttl`, that the SPDX Project generates it from the model sources in the `spdx/spdx-3-model` repository, and that it is identical to the published one.[^notice] It is licensed under the Community Specification License 1.0, which the repository's 3.0.1 tag carries. That licence asks a derived work to attribute the working group with the material's name, version number and source, and NOTICE does so.

## How the repository uses it

`scripts/spdx_to_linkml.py` reads this file, and nothing else, to write every module of the [spdx LinkML schema](spdx-linkml-schema.md). It reads the SPDX version from the ontology IRI, and leaves out the model's individuals, such as NoneElement and SpdxOrganization, as instance data. Nothing in the repository edits the file: a new SPDX release replaces it whole, as [Move to a new SPDX release](../playbooks/move-to-a-new-spdx-release.md) says.

`scripts/check_upstream_release.py` downloads the published model for the version the file names and compares the two byte for byte, and reads the tags of `spdx/spdx-3-model` for a newer release.[^check_upstream_release.py] [Upstream watch](../workflows/upstream-watch.md) runs it every week.

[^spdx-model.ttl]: src/spdx_linkml/schema/upstream/spdx-model.ttl, the ontology header
[^notice]: NOTICE, The SPDX 3.0.1 model, by the SPDX Project
[^check_upstream_release.py]: scripts/check_upstream_release.py, the docstring and the check function
