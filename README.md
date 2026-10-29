<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# spdx

System Package Data Exchange (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/spdx](https://lmodel.github.io/spdx)

## What it models

The [System Package Data Exchange (SPDX)](https://spdx.github.io/spdx-spec/v3.0.1/) model at version 3.0.1, one module for each of its nine profiles:

* **Core** (`spdx_core`): the Element every SPDX object descends from, agents and tools, relationships and annotations, bundles and documents, creation information, integrity methods and external references.
* **Software** (`spdx_software`): packages, files and snippets, their purposes and content identifiers, and the software bill of materials (SBOM).
* **Security** (`spdx_security`): vulnerabilities and the assessments made of them, as Common Vulnerability Scoring System (CVSS) scores, Exploit Prediction Scoring System (EPSS) probabilities, Stakeholder-Specific Vulnerability Categorization (SSVC) decisions, exploit catalogue entries and Vulnerability Exploitability eXchange (VEX) statements.
* **Simple Licensing** and **Expanded Licensing** (`spdx_simple_licensing`, `spdx_expanded_licensing`): license expressions and texts, listed and custom licenses and additions, and the sets that compose them.
* **AI** and **Dataset** (`spdx_ai`, `spdx_dataset`): AI and dataset packages, with their model, training, energy, safety, collection and sensitivity details.
* **Build** (`spdx_build`): a build, with its type, configuration source, parameters and environment.
* **Extension** (`spdx_extension`): the extension point on every Element, and the CycloneDX properties extension.

`scripts/spdx_to_linkml.py` writes every module from a copy of the [published model](https://spdx.org/rdf/3.0.1/spdx-model.ttl) in [src/spdx_linkml/schema/upstream/](src/spdx_linkml/schema/upstream), and every class, property and vocabulary value keeps its SPDX Internationalized Resource Identifier (IRI). The schema's `version` is 3.0.1. A weekly workflow opens an issue when the copy differs from the published model or the SPDX Project tags a newer release. Release tags number the schema's versions.

## Influences

None beyond the SPDX 3.0.1 model: the schema renders one specification, and its release asset and governance files follow [lmodel/slsa](https://github.com/lmodel/slsa).

## Mappings

None: each element is SPDX's own term under its SPDX IRI, and no element names a term of another vocabulary.

## Not modelled here

The model's individuals, such as NoneElement, are instance data and not part of the schema, and the schema does not check SPDX's rule against using a class of the model as an extension. A document in SPDX's JSON-LD serialisation does not validate as it stands, because SPDX writes profile-prefixed keys and blank-node references to its creation information. [docs/about.md](docs/about.md) says what the rendering adds and where it differs from SPDX's serialisations.

## Repository Structure

* [docs/](docs/): the website's pages, with the generated schema pages in [elements/](docs/elements/)
* [examples/](examples/): usage examples
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the converter that writes the schema, and the upstream watch
* [src/spdx_linkml/schema/](src/spdx_linkml/schema): the LinkML schema, `spdx_linkml.yaml` and one module per profile, as the converter writes them (do not edit them), and the model copy
* [src/spdx_linkml/datamodel/](src/spdx_linkml/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data and the SPDX Project's examples in [data/](tests/data)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle, written in the Linked Open Knowledge Format (LOKF). Its domain schema is `.lokf/spdx.yaml`, which `lokf adapt` writes from `src/spdx_linkml/schema/spdx_linkml.yaml`. Change the converter, never the copy. A release carries the copy as `schema-<tag>-spdx.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

`just lokf-adapt` rewrites the copy, and `just lokf-adapt-check` says when it is stale. The copy roots Element on `Concept`, because SPDX gives Element alone an identifier and every other element class descends from it. A concept may name any concrete subclass as its `type`. In Obsidian, add these classes to the KTL Registrar and KTL Curator plugins' *Known LOKF types* setting:

```text
Package, File, Sbom, Build, AIPackage, DatasetPackage, Vulnerability, SpdxAgent, SpdxPerson, SpdxOrganization, SoftwareAgent, Tool
```

In the copy, LOKF's `id` replaces `spdxId`, and LOKF's `type` replaces the `type` designator, so an inlined object names its class as `type: Hash` rather than by a compact URI (CURIE). A concept of an SPDX class carries the `creationInfo` that SPDX requires of every Element.

A host imports the copy beside `lokf.yaml`, and LinkML merges the two into one namespace, where the last definition of a name wins silently. So the copy gives each name that LOKF also defines an `spdx` prefix, and keeps its SPDX IRI. The classes `Agent`, `Organization` and `Person` become `SpdxAgent`, `SpdxOrganization` and `SpdxPerson`, the type `media_type` becomes `spdx_media_type`, and the keys `algorithm`, `context`, `created`, `description`, `from`, `name` and `to` take an `spdx_` prefix.

Four keys are SPDX's and also slsa's or oscal's under another IRI: `subject` and `value` in slsa's copy, and `identifier`, `statement`, `subject` and `value` in oscal's. A host that imports this copy beside either projects each of those keys under one vocabulary's IRI. The class `Hash` is SPDX's and oscal's, so a host cannot import this copy beside oscal's until one of the two copies renames it. `tests/test_schema_rules.py` checks the copy against all four schemas and fails on a new shared name.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)).

The SPDX 3.0.1 model in [src/spdx_linkml/schema/upstream/](src/spdx_linkml/schema/upstream) is the SPDX Project's, under the Community Specification License 1.0, and the element descriptions are its texts. The SPDX Project's examples in [tests/data/spdx-examples/](tests/data/spdx-examples) keep their own license: see [NOTICE](NOTICE).

This is not an official SPDX release, and its use implies no endorsement by the SPDX Project or the Linux Foundation.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
