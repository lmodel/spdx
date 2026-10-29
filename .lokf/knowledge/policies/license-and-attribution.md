---
type: Policy
id: https://w3id.org/lmodel/spdx/knowledge/policies/license-and-attribution
genre: reference
title: License and attribution
description: "Which licence covers what in the spdx repository: Apache-2.0 for the schema, the generated models and the code; the SPDX 3.0.1 model copy under the Community Specification License 1.0, with the attribution it asks for; the SPDX examples under GPL-3.0; the linkml-project-copier scaffolding under MIT; the KTL sidecar and site templates under Apache-2.0; and the bundle under CC BY 4.0."
resource: NOTICE
relatedTo:
  - https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-model-copy
  - https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-examples
sources:
  - id: notice
    resource: NOTICE
    title: every section
  - id: readme.md
    resource: README.md
    title: the License and Credits sections
  - id: website-notice
    resource: website/NOTICE
    title: the graph explorer's notice
  - resource: LICENSE
    title: the Apache License, Version 2.0
  - resource: CONTRIBUTING.md
    title: the License section
  - resource: tests/data/spdx-examples/COPYING
    title: the GNU General Public License, version 3
  - resource: website/README.md
    title: the typefaces paragraph
  - resource: .lokf/knowledge/index.md
    title: the license key
  - resource: pyproject.toml
    title: the license and license-files keys
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# License and attribution

`NOTICE` names the project "System Package Data Exchange (SPDX) LinkML Schema (spdx)", copyright 2026 Noel McLoughlin. It says that the code in the repository is licensed under the Apache License, Version 2.0, which `LICENSE` holds, and that some of the content the repository carries is third-party work under its own terms.[^notice] The README says that the schema and the code are under the Apache License 2.0, and that this is not an official SPDX release and its use implies no endorsement by the SPDX Project or the Linux Foundation.[^readme.md] CONTRIBUTING.md says that a contribution is licensed under the Apache License 2.0, and asks that NOTICE be updated when something new comes from elsewhere. `pyproject.toml` lists NOTICE beside LICENSE as the package's licence files.

## What NOTICE lists

- **The schema's rendering of SPDX.** `src/spdx_linkml/schema/*.yaml`, `src/spdx_linkml/datamodel/` and `project/` render the SPDX 3.0.1 model as a LinkML schema. `scripts/spdx_to_linkml.py` writes them from the model, and their element descriptions are the model's own texts. They are not the SPDX Project's, and SPDX and System Package Data Exchange are trademarks of the Linux Foundation.
- **The SPDX 3.0.1 model, by the SPDX Project.** `src/spdx_linkml/schema/upstream/spdx-model.ttl` is the "System Package Data Exchange (SPDX) Ontology", version 3.0.1, copyright 2024 SPDX Project, retrieved from `https://spdx.org/rdf/3.0.1/spdx-model.ttl`. It is licensed under the Community Specification License 1.0, which the `spdx/spdx-3-model` repository's 3.0.1 tag carries. That licence asks a derived work to attribute the working group with the material's name, version number and source, and NOTICE does so. See [SPDX model copy](../datasets/spdx-model-copy.md).
- **SPDX examples.** `tests/data/spdx-examples/` is a copy of the SPDX Project's spdx-examples repository, licensed under the GNU General Public License, version 3, whose text is `tests/data/spdx-examples/COPYING`. Some example contents carry a licence file of their own, and the tests only read these files. See [SPDX examples copy](../datasets/spdx-examples.md).
- **linkml-project-copier.** The project was generated from this template, and its justfile, configuration and documentation scaffolding derive from it, under the MIT License, copyright 2025 David Linke. The README credits the template by its DOI, `10.5281/zenodo.15163584`.
- **The knowledge bundle's tooling.** The scripts under `.lokf/scripts/` and `.lokf/m365/` and the knowledge-librarian, knowledge-registrar, knowledge-release and knowledge-sync workflows are copies of the ktl-sidecar templates in knowledge-trust-ladder. `website/` and the knowledge-website workflow derive from its ktl-website templates. All of them are licensed under the Apache License, Version 2.0.

`website/NOTICE` says that `src/components/KnowledgeGraph.astro` is adapted from the LOKF toolkit's site, copyright 2026 Nolan Nichols, under the Apache License, Version 2.0, and that the file's header comment lists the changes.[^website-notice] `website/README.md` says that the site's two typefaces are self-hosted from Fontsource under the SIL Open Font License 1.1. The bundle's root `index.md` declares the licence CC BY 4.0 for the knowledge bundle itself.

[^notice]: NOTICE, every section
[^readme.md]: README.md, the License and Credits sections
[^website-notice]: website/NOTICE, the whole file
