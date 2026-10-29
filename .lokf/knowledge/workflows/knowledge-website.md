---
type: Service
id: https://w3id.org/lmodel/spdx/knowledge/workflows/knowledge-website
genre: reference
title: Knowledge website (knowledge-website.yaml)
description: "The Knowledge website workflow, .github/workflows/knowledge-website.yaml: on pushes and pull requests that touch the site's sources, every Monday at 05:23 UTC and by hand, its build job builds website/ and checks its links read-only, and its deploy job publishes the default branch's build to GitHub Pages once KNOWLEDGE_WEBSITE_ENABLED is true."
resource: .github/workflows/knowledge-website.yaml
relatedTo:
  - https://w3id.org/lmodel/spdx/knowledge/services/documentation-site
sources:
  - id: knowledge-website.yaml
    resource: .github/workflows/knowledge-website.yaml
    title: the header comment, the on key and both jobs
  - id: notice
    resource: NOTICE
    title: the Knowledge bundle section
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# Knowledge website (knowledge-website.yaml)

`.github/workflows/knowledge-website.yaml` is the workflow named "Knowledge website". It builds the site in `website/` and publishes the default branch's build to GitHub Pages.[^knowledge-website.yaml] NOTICE says that it derives from the ktl-website templates of the Knowledge Trust Ladder repository.[^notice]

It runs on a push or a pull request that touches the site, the bundle, the README, `docs/`, the changelog, `llms.txt`, `.linkml/`, a justfile, a `pyproject.toml`, a `uv.lock` or the workflow itself. It also runs every Monday at 05:23 UTC and by hand. A header comment says that the weekly run rebuilds the site from the default branch, to catch what no push to those paths brings, such as a schema change elsewhere and the changelog's promotion, whose commit skips CI.

- **`build`**, named "Build the site (read-only)", runs with `contents: read`. A push builds on the default branch only, and a pull request or a dispatch always builds. It installs the lokf toolkit that the sidecar pins and Node.js, installs just when the site builds a folder with it, and then runs `npm run build`, which checks the links between the site's pages.
- **`deploy`**, named "Deploy to GitHub Pages", holds `pages: write` and `id-token: write` in the `github-pages` Environment, and runs only harden-runner and GitHub's own deploy-pages action. It runs for the default branch once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`. Until then the workflow builds but deploys nothing.

A header comment says to tell Pages once to take its site from Actions before setting the variable, and to keep the variable unset while another publisher still deploys Pages, since two publishers overwrite each other's site. [spdx documentation site](../services/documentation-site.md) describes the site.

[^knowledge-website.yaml]: .github/workflows/knowledge-website.yaml, the header comment, the on key and both jobs
[^notice]: NOTICE, the Knowledge bundle section
