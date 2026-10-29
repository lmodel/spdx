---
type: Policy
id: https://w3id.org/lmodel/spdx/knowledge/policies/ai-covenant
genre: reference
title: AI covenant
description: "The rules for AI-assisted work in spdx: a contributor owns what they submit; the converter writes every schema element from the SPDX model, so a change goes into the converter with the part of the model it reads cited; the model copy is never edited; and the scheduled librarian works through pull requests a person approves, with least privilege."
resource: AI_COVENANT.md
sources:
  - id: ai_covenant.md
    resource: AI_COVENANT.md
    title: every section
  - resource: CONTRIBUTING.md
    title: the Using AI tools section
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# AI covenant

`AI_COVENANT.md` sets the community norms for AI use in the repository `lmodel/spdx`. Its core principle is that everything a contributor submits is theirs, whatever tools helped make it, so the contributor must understand it, verify it, defend it in review and meet the project's standards.[^ai_covenant.md] CONTRIBUTING.md says that the covenant binds people and the scheduled `knowledge-librarian` agent alike, and that a claim about what SPDX defines must be checked against its model.

## What is specific to this project

The covenant says that the repository models someone else's specification. The SPDX Project defines what an SPDX 3 element, property and vocabulary mean, in the model it publishes with each release, and a script writes the schema from that file. A class, field or rule that a model produced, presented as what SPDX says, is the failure mode it guards against. So:

- **An element says what SPDX says.** `scripts/spdx_to_linkml.py` writes every class, slot and enum under `src/spdx_linkml/schema/` from the SPDX model at the pinned release, and each description is the model's own text. A change goes into the converter, never the schema files, and the pull request cites the part of the model a converter rule reads.
- **The model copy is upstream text.** `src/spdx_linkml/schema/upstream/spdx-model.ttl` is never edited. It is replaced whole from a release, and the upstream watch checks that it still matches.
- **The terms are SPDX's, and the additions are this project's.** Every class, property and vocabulary value keeps its SPDX IRI, and what the schema adds, such as `spdxId` and its datatypes, lives under `spdx_linkml:`.

## Reviews, discussions and disclosure

AI review tools give automated quality checks, not human reviews, and a pull request still needs a person's approval. AI systems must not post comments in issues, discussions, shared channels or mailing lists in their own voice. Disclosure is required for a fix in code the contributor does not fully understand, and for a converter rule drafted by AI, with the part of the SPDX model it reads. AI co-authorship in commit messages is actively discouraged.

## The scheduled agent

The covenant names `knowledge-librarian.yaml` and its `ktl-librarian` skill as repository-owned agent automation. Such an agent:

- commits as a labelled bot identity or as the maintainer who invoked it;
- opens every change as a pull request that a person approves;
- runs in a read-only job beside a privileged job that runs no agent code;
- records a person's verdict only as that person gave it.

[Knowledge Librarian](../workflows/knowledge-librarian.md) describes the workflow.

[^ai_covenant.md]: AI_COVENANT.md, every section
