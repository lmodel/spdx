---
type: Explanation
id: https://w3id.org/lmodel/spdx/knowledge/explanations/element-names
genre: explanation
title: Element names and the shared namespace
description: "Why the spdx schema names its elements as it does: SPDX's own names, lowerCamelCase slots and vocabulary values as SPDX's JSON-LD writes them, security_locator for the Security profile's locator, spdxId and a class CURIE as the type, the spdx_linkml package and the spdx3 prefix; and why the adapt copy renames Agent, Organization, Person, media_type and seven keys, and shares Hash and four keys with neighbour copies."
resource: scripts/spdx_to_linkml.py
about:
  - https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-linkml-schema
sources:
  - id: spdx_to_linkml.py
    resource: scripts/spdx_to_linkml.py
    title: the docstring's rules, TERMS_PREFIX and TYPE_SLOT
  - id: linkmllint.yaml
    resource: .linkmllint.yaml
    title: the naming rule and its reasons
  - id: pyproject.toml
    resource: pyproject.toml
    title: the comment above the distribution's name
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: SHARED_KEYS, SHARED_CLASSES and the four tests
  - resource: docs/about.md
    title: What the rendering adds
  - resource: .lokf/spdx.yaml
    title: the notes lokf adapt wrote
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Element names and the shared namespace

The schema's names are SPDX's. `scripts/spdx_to_linkml.py` names every class, property and vocabulary as the SPDX model does, and keeps each element's SPDX IRI beside its name.[^spdx_to_linkml.py] Its one exception is a property whose local name another profile also uses: it takes the key that SPDX's JSON-LD context gives it, so the Security profile's `locator` is the slot `security_locator`, since Core has a `locator` too.

## Case

`.linkmllint.yaml` relaxes LinkML's naming rule to fit SPDX's names.[^linkmllint.yaml] Slots are SPDX property names, which are lowerCamelCase, such as `hashValue` and `packageVersion`. Permissible values are SPDX's vocabulary entries as the JSON-LD serialisation writes them, such as `kilowattHour` and `sha3_256`, so a document compares with the schema without translation. `security_locator` is the one slot with an underscore.

## What the schema adds

SPDX's JSON-LD writes an Element's IRI as the `spdxId` key, and the model has no property for it, so the schema declares `spdxId` in its own namespace as Element's identifier. `type`, the `rdf:type` designator, takes the class's CURIE, such as `spdx_software:Package`, rather than its name, because the LinkML runtime writes the designator's value as the node's `rdf:type`, and a name would be a literal there. The root of SPDX 3.0.1's terms is bound as `spdx3`, because LOKF binds `spdx` to SPDX 2's namespace, and a copy beside `lokf.yaml` must bind no prefix twice.

The Python package and the umbrella schema are `spdx_linkml`. A comment in `pyproject.toml` says that the distribution is named `spdx-linkml`, like gist-linkml and slsa-linkml, and that the import package is `spdx_linkml` because the PyPI package spdx and spdx-tools before 0.8 both install `spdx`.[^pyproject.toml]

## In the adapt copy

A host imports `.lokf/spdx.yaml` beside `lokf.yaml`, and LinkML merges the two into one namespace, where the last definition of a name wins silently. The README says that the copy gives each name LOKF also defines an `spdx` prefix and keeps its SPDX IRI.[^readme.md] The classes `Agent`, `Organization` and `Person` become `SpdxAgent`, `SpdxOrganization` and `SpdxPerson`, and the type `media_type` becomes `spdx_media_type`. The keys `algorithm`, `context`, `created`, `description`, `from`, `name` and `to` take an `spdx_` prefix. `lokf adapt` renames only top-level slots, never a class attribute, which is why the converter makes every property a top-level slot. In the copy, LOKF's `id` replaces `spdxId`, and LOKF's `type` replaces the designator, so an inlined object names its class as `type: Hash`.

`lokf adapt` keeps a copy apart from `lokf.yaml` only. `tests/test_schema_rules.py` pins what the copy shares with the copies other lmodel repositories release: the keys `subject` and `value` with slsa's, the keys `identifier`, `statement`, `subject` and `value` with oscal's, and the class `Hash` with oscal's.[^test_schema_rules.py] A host that imports the copy beside slsa's or oscal's projects each shared key under one vocabulary's IRI, and cannot import it beside oscal's until one of the two copies renames `Hash`.

[^spdx_to_linkml.py]: scripts/spdx_to_linkml.py, the docstring's rules, `TERMS_PREFIX` and `TYPE_SLOT`
[^linkmllint.yaml]: .linkmllint.yaml, the naming rule and its reasons
[^pyproject.toml]: pyproject.toml, the comment above the distribution's name
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^test_schema_rules.py]: tests/test_schema_rules.py, `SHARED_KEYS`, `SHARED_CLASSES` and the four tests
