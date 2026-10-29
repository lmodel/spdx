---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/spdx/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: spdx Knowledge Bundle
description: System Package Data Exchange (LinkML)
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/spdx/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# spdx Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for spdx. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [spdx documentation site](services/documentation-site.md) - The Astro Starlight site in website/, built from the README, docs/, the schema's gen-doc pages, the changelog and the knowledge bundle by the Knowledge website workflow, which deploys it to GitHub Pages under lmodel.github.io/spdx when KNOWLEDGE_WEBSITE_ENABLED is true; its REDIRECTS send the retired mkdocs addresses on to the new pages.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow, .github/workflows/main.yaml: on a push to main and on every pull request, its test job runs just test on Python 3.10 to 3.14, and on 3.13 also just lint and just lokf-adapt-check, the check that .lokf/spdx.yaml is current.
* [Lint & docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The Lint & docs workflow, .github/workflows/lint-and-docs.yaml: on a push to main, every pull request, a Monday 06:00 UTC schedule and by hand, four jobs run ShellCheck, actionlint, the word budgets of CONTRIBUTING.md (1000) and SECURITY.md (900), and markdownlint, lychee and codespell over the Markdown.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The Semantic release workflow, .github/workflows/semantic-release.yml: on a pull request into main, its plan job checks that the commits, the changelog and the title would release and previews the release; on a push to main, its release job in the release Environment tags vX.Y.Z, publishes the GitHub Release and dispatches Knowledge Release.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The Upstream watch workflow, .github/workflows/upstream-watch.yaml: every Monday at 07:00 UTC and by hand, it runs scripts/check_upstream_release.py, which compares the vendored SPDX model with the published 3.0.1 file and spdx/spdx-3-model's tags, and on a finding opens or updates the issue titled Upstream watch: the SPDX release has changed.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The Knowledge website workflow, .github/workflows/knowledge-website.yaml: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds website/ and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once KNOWLEDGE_WEBSITE_ENABLED is true.
* [Knowledge Registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The Knowledge Registrar workflow, .github/workflows/knowledge-registrar.yaml: the gate on the knowledge bundle, run on pull requests that touch .lokf/, every Monday at 06:00 UTC and by hand; it validates the bundle and its relation targets against the domain schema, runs the conventions script, and checks that each new confirmation by a person is backed by an approval or a signed commit.
* [Knowledge Librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The Knowledge Librarian workflow, .github/workflows/knowledge-librarian.yaml: every Monday at 05:00 UTC and by hand, once KNOWLEDGE_LIBRARIAN_ENABLED is true, it runs an LLM agent with the ktl-librarian skill (pinned by TRUST_LADDER_SKILLS_REF at v0.59.0) in a read-only job and opens a review pull request with the bundle change from a separate privileged job.
* [Knowledge Release (knowledge-release.yaml)](workflows/knowledge-release.md) - The Knowledge Release workflow, .github/workflows/knowledge-release.yaml: dispatched with a release's tag, or started by a published release once KNOWLEDGE_RELEASE_ENABLED is true, it attaches `knowledge-<tag>-<name>.zip`, the domain schema as `schema-<tag>-spdx.yaml` and the Copilot skills to the release, but only when the bundle changed since the last release that carries one, or when force is set.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The Knowledge sync workflow, .github/workflows/knowledge-sync.yaml: every Monday at 04:10 UTC and by hand, it moves the sidecar's copies and the skills pin to the newest Knowledge Trust Ladder release through one pull request from the knowledge-sync branch, opened with the KNOWLEDGE_SYNC_TOKEN secret, and holds the workflow changes for a person to apply.

# Policies

* [Security policy](policies/security-policy.md) - How to report a vulnerability in spdx (GitHub's private vulnerability reporting, not a public issue), which release gets fixes, what the repository releases and runs, what holds each workflow, and the three repository settings not yet in force: required reviewers on the release Environment, a deletion and force-push rule on main, and secret scanning with push protection.
* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work in spdx: a contributor owns what they submit; the converter writes every schema element from the SPDX model, so a change goes into the converter with the part of the model it reads cited; the model copy is never edited; and the scheduled librarian works through pull requests a person approves, with least privilege.
* [License and attribution](policies/license-and-attribution.md) - Which licence covers what in the spdx repository: Apache-2.0 for the schema, the generated models and the code; the SPDX 3.0.1 model copy under the Community Specification License 1.0, with the attribution it asks for; the SPDX examples under GPL-3.0; the linkml-project-copier scaffolding under MIT; the KTL sidecar and site templates under Apache-2.0; and the bundle under CC BY 4.0.

# Datasets

* [spdx LinkML schema](datasets/spdx-linkml-schema.md) - The LinkML schema of the SPDX 3.0.1 model (schema id `https://w3id.org/lmodel/spdx`, version 3.0.1): `spdx_linkml.yaml` imports one module per SPDX profile, 67 classes, 160 slots, 23 enums and 5 types in all, which scripts/spdx_to_linkml.py writes from the vendored model; its `lokf adapt` copy in `.lokf/spdx.yaml`, rooted on Element, is the bundle's domain schema.
* [SPDX model copy](datasets/spdx-model-copy.md) - `src/spdx_linkml/schema/upstream/spdx-model.ttl`, the SPDX Project's 3.0.1 model in OWL and SHACL as Turtle, retrieved from spdx.org under the Community Specification License 1.0; never edited here, the converter's only input, and compared byte for byte with the published file every week.
* [Generated artefacts](datasets/generated-artefacts.md) - Files generated from the spdx schema and never edited by hand: project/ (Excel, GraphQL, Java, JSON-LD, JSON Schema, OWL, a prefix map, protobuf, SHACL, ShEx, SQL and TypeScript), the dataclass and Pydantic models in src/spdx_linkml/datamodel/, the merged schema in docs/schema/, the gen-doc pages in docs/elements/ and the domain schema copy .lokf/spdx.yaml.
* [Test data and schema tests](datasets/test-data.md) - Example instances of the spdx schema in tests/data/: 54 valid files and 88 counter-examples, one for each constraint the schema states, each named after its class (Package-with-hash.yaml, Hash-missing-hashValue.yaml), which tests/test_data.py holds to the validator; beside them, tests/test_rdf.py writes the valid examples as RDF, tests/test_schema_is_generated.py fails on a hand-edited schema, and tests/test_schema_rules.py checks the adapt copy's names against LOKF's and three neighbour copies.
* [SPDX examples copy](datasets/spdx-examples.md) - tests/data/spdx-examples/, a copy of the SPDX Project's spdx-examples repository under GPL-3.0: 44 JSON files, 26 of them SPDX 3 documents in JSON-LD, which tests/test_data.py reads for class names, required fields and vocabulary values; the copy's links and spelling are upstream's, so the linters leave it alone.

# References

* [SPDX specification 3.0.1](references/spdx-specification.md) - The System Package Data Exchange (SPDX) specification at version 3.0.1, published by the SPDX Project at spdx.github.io/spdx-spec/v3.0.1/ from the model in spdx/spdx-3-model under the Community Specification License 1.0: the authority every schema element renders, with a page per class, property and vocabulary that the schema's see_also links.
* [LinkML](references/linkml.md) - What the spdx repository takes from LinkML: the linkml-project-copier template at v0.5.0, LinkML 1.12.1 as uv.lock pins it, the generators gen-project and the recipes run, linkml-lint with the repository's own naming rule, and the runtime limits the tests and docs/about.md record.

# Explanations

* [Element names and the shared namespace](explanations/element-names.md) - Why the spdx schema names its elements as it does: SPDX's own names, lowerCamelCase slots and vocabulary values as SPDX's JSON-LD writes them, security_locator for the Security profile's locator, spdxId and a class CURIE as the type, the spdx_linkml package and the spdx3 prefix; and why the adapt copy renames Agent, Organization, Person, media_type and seven keys, and shares Hash and four keys with neighbour copies.
* [Scope, influences and mappings](explanations/scope-and-influences.md) - What the spdx schema renders and leaves out, and why: the SPDX 3.0.1 model alone, with no influences beyond it and no mappings; the five things the rendering adds; the model's individuals and the extension rule it leaves out; and where a document in SPDX's JSON-LD, or RDF written from the schema's data, differs from SPDX's own.

# Playbooks

* [Regenerate and test the schema](playbooks/regenerate-and-test.md) - How to change the spdx schema: set up with uv and just, change scripts/spdx_to_linkml.py rather than the schema files, regenerate with just gen-linkml, gen-project, gen-doc and lokf-adapt, add examples, then run the checks CI runs (just test on Python 3.10 to 3.14, just lint and just lokf-adapt-check on 3.13) and the pre-commit hooks.
* [Release the schema](playbooks/release.md) - How a releasing commit merged to main makes semantic-release promote the changelog's Unreleased section, tag vX.Y.Z and publish a GitHub Release, then dispatch the Knowledge Release workflow once KNOWLEDGE_RELEASE_ENABLED is true; below 1.0.0 from a v0.0.0 baseline tag, with a breaking change as a minor bump and nothing published to PyPI.
* [Move to a new SPDX release](playbooks/move-to-a-new-spdx-release.md) - What to do when the upstream watch opens its issue: replace src/spdx_linkml/schema/upstream/spdx-model.ttl whole with the model the SPDX Project publishes for the new release, run just gen-linkml, then just lint, gen-project, gen-doc, lokf-adapt and test, and move the release's number and addresses in NOTICE, the README and lychee.toml.
* [Validate data against the schema](playbooks/validate-data.md) - How to check a YAML or JSON file against the spdx schema with linkml-validate (for example with -C Package), why each object's type is a class CURIE such as spdx_software:Package, why a document in SPDX's own JSON-LD does not validate as it stands, and why the example runner cannot load an example with a from or import key.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external page this bundle derives concepts from, the concepts each yields, how to re-check each on a refresh run, and the paths left out on purpose.
