---
type: Explanation
id: https://w3id.org/lmodel/spdx/knowledge/explanations/scope-and-influences
genre: explanation
title: Scope, influences and mappings
description: "What the spdx schema renders and leaves out, and why: the SPDX 3.0.1 model alone, with no influences beyond it and no mappings; the five things the rendering adds; the model's individuals and the extension rule it leaves out; and where a document in SPDX's JSON-LD, or RDF written from the schema's data, differs from SPDX's own."
resource: README.md
about:
  - https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-linkml-schema
sources:
  - id: readme.md
    resource: README.md
    title: What it models, Influences, Mappings and Not modelled here
  - id: about.md
    resource: docs/about.md
    title: What the rendering adds, and Where it differs from SPDX's serialisations
  - resource: docs/index.md
    title: the docs' opening page
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Scope, influences and mappings

The README says that the schema models the SPDX model at version 3.0.1, one module for each of its nine profiles.[^readme.md] `scripts/spdx_to_linkml.py` writes the modules from a copy of the published model, and every class, property and vocabulary value keeps its SPDX IRI. It names no influence beyond that model: the schema renders one specification, and its release asset and governance files follow lmodel/slsa. It names no mappings either, since each element is SPDX's own term under its SPDX IRI and no element names a term of another vocabulary.

## What the rendering adds

docs/about.md lists five things the schema adds to the model:[^about.md]

- `spdxId`, the identifier of an Element, which SPDX's JSON-LD writes as a key and the model has no property for;
- `type`, the type designator every root class carries, whose value is the class's CURIE;
- five types for the datatypes SPDX constrains: `date_time_stamp`, `media_type`, `semver`, `positive_integer` and `non_negative_integer`;
- one module per profile, with Extension and AnyLicenseInfo declared in the core module;
- one subset per profile, so the documentation can be read a profile at a time.

## What it leaves out

The model's individuals, NoAssertionElement, NoneElement, NoAssertionLicense, NoneLicense and SpdxOrganization, are instance data and are not in the schema, so a reference to one is an IRI like any other Element reference. SPDX's SHACL says that an Element's `extension` must not be an instance of a class of the model, and the schema has no such rule.

## Where it differs from SPDX's serialisations

A document in SPDX's JSON-LD serialisation does not validate against the schema as it stands. SPDX's JSON-LD prefixes the name of a class or property outside Core with its profile, as in `software_Package`, and the schema uses the bare name and the class's CURIE as the value of `type`. SPDX's JSON-LD also gives CreationInfo a blank-node identifier that each Element refers to, and the schema inlines CreationInfo in each Element. RDF written from the schema's data differs from SPDX's RDF in two ways, both in LinkML 1.12.1, which [LinkML](../references/linkml.md) names.

[^readme.md]: README.md, What it models, Influences, Mappings and Not modelled here
[^about.md]: docs/about.md, What the rendering adds, and Where it differs from SPDX's serialisations
