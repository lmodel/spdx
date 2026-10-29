---
type: Reference
id: https://w3id.org/lmodel/spdx/knowledge/references/spdx-specification
genre: reference
title: SPDX specification 3.0.1
description: "The System Package Data Exchange (SPDX) specification at version 3.0.1, published by the SPDX Project at spdx.github.io/spdx-spec/v3.0.1/ from the model in spdx/spdx-3-model under the Community Specification License 1.0: the authority every schema element renders, with a page per class, property and vocabulary that the schema's see_also links."
resource: https://spdx.github.io/spdx-spec/v3.0.1/
sources:
  - id: about.md
    resource: docs/about.md
    title: the References section and Where the model comes from
  - id: spdx_linkml.yaml
    resource: src/spdx_linkml/schema/spdx_linkml.yaml
    title: the see_also list and the comments
  - id: readme.md
    resource: README.md
    title: What it models
  - resource: https://github.com/spdx/spdx-3-model/blob/3.0.1/License.md
    title: the Community Specification License 1.0 at the 3.0.1 tag
  - resource: scripts/spdx_to_linkml.py
    title: the see_also addresses it writes
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# SPDX specification 3.0.1

The SPDX specification at version 3.0.1 is published at `https://spdx.github.io/spdx-spec/v3.0.1/`, and docs/about.md lists it, the 3.0.1 model in Turtle and spdx-examples as the repository's references.[^about.md] The SPDX Project publishes the model as OWL and SHACL in Turtle at `https://spdx.org/rdf/3.0.1/spdx-model.ttl`, which the [SPDX model copy](../datasets/spdx-model-copy.md) holds.

## What the schema takes from it

The README says that the schema renders the model at version 3.0.1, one module for each of its nine profiles: Core, Software, Security, Simple Licensing, Expanded Licensing, AI, Dataset, Build and Extension.[^readme.md] The umbrella's `see_also` names the specification and `https://spdx.dev/specifications/`, and its comments say that the element descriptions are the model's texts, which the SPDX Project publishes under the Community Specification License 1.0.[^spdx_linkml.yaml] The converter gives every class, property and vocabulary a `see_also` to its page in the specification, such as `model/Core/Classes/Element/`.

The model's sources live in the `spdx/spdx-3-model` repository, whose 3.0.1 tag carries the Community Specification License 1.0. [Upstream watch](../workflows/upstream-watch.md) reads that repository's tags each week for a newer release.

[^about.md]: docs/about.md, the References section and Where the model comes from
[^readme.md]: README.md, What it models
[^spdx_linkml.yaml]: src/spdx_linkml/schema/spdx_linkml.yaml, the see_also list and the comments
