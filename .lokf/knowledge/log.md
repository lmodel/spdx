# Change Log

## 2026-10-29

* **Added**: Build and test (main.yaml), from `.github/workflows/main.yaml`.
* **Added**: Lint & docs (lint-and-docs.yaml), from `.github/workflows/lint-and-docs.yaml`.
* **Added**: Semantic release (semantic-release.yml), from `.github/workflows/semantic-release.yml`.
* **Added**: Upstream watch (upstream-watch.yaml), from `.github/workflows/upstream-watch.yaml`.
* **Added**: Knowledge website (knowledge-website.yaml), from `.github/workflows/knowledge-website.yaml`.
* **Added**: Knowledge Registrar (knowledge-registrar.yaml), from `.github/workflows/knowledge-registrar.yaml`.
* **Added**: Knowledge Librarian (knowledge-librarian.yaml), from `.github/workflows/knowledge-librarian.yaml`.
* **Added**: Knowledge Release (knowledge-release.yaml), from `.github/workflows/knowledge-release.yaml`.
* **Added**: Knowledge sync (knowledge-sync.yaml), from `.github/workflows/knowledge-sync.yaml`.
* **Added**: Security policy, from `SECURITY.md`.
* **Added**: AI covenant, from `AI_COVENANT.md`.
* **Added**: License and attribution, from `NOTICE`.
* **Added**: spdx documentation site, from `website/` and the README.
* **Removal**: the sidecar's two example services, which the real concepts replace.
* **Added**: spdx LinkML schema, from `src/spdx_linkml/schema/` and `scripts/spdx_to_linkml.py`.
* **Added**: SPDX model copy, from `src/spdx_linkml/schema/upstream/spdx-model.ttl` and NOTICE.
* **Added**: Generated artefacts, from the justfile, `config.yaml` and `config.public.mk`.
* **Added**: Test data and schema tests, from `tests/`.
* **Added**: SPDX examples copy, from `tests/data/spdx-examples/`.
* **Added**: SPDX specification 3.0.1, from docs/about.md, the README and the schema header.
* **Added**: LinkML, from the repository's own files.
* **Added**: Element names and the shared namespace, from the converter, `.linkmllint.yaml` and the README.
* **Added**: Scope, influences and mappings, from the README and docs/about.md.
* **Added**: Regenerate and test the schema, from CONTRIBUTING.md and the justfiles.
* **Added**: Release the schema, from CONTRIBUTING.md, CHANGELOG.md and `.releaserc.json`.
* **Added**: Move to a new SPDX release, from docs/about.md and the converter.
* **Added**: Validate data against the schema, from docs/about.md and tests/data/README.md.
* **Source map**: the map names every repository path the bundle derives from, the concepts each yields and how to re-check it, and the paths left out with the reason for each.
* **Initialization**: Scaffolded the LOKF bundle for spdx with placeholder
  services. Real concepts to follow.
