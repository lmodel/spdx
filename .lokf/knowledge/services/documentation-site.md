---
type: Service
id: https://w3id.org/lmodel/spdx/knowledge/services/documentation-site
genre: reference
title: spdx documentation site
description: The Hugo site in website/, built from the README, docs/, the schema's gen-doc pages, the changelog and the knowledge bundle by the Knowledge website workflow, which deploys it to GitHub Pages under lmodel.github.io/spdx when KNOWLEDGE_WEBSITE_ENABLED is true; it sends the retired mkdocs addresses on to the new pages.
resource: website
endpoint: https://lmodel.github.io/spdx/
sources:
  - id: readme.md
    resource: README.md
    title: Documentation Website and the website item of Repository Structure
  - id: website-readme.md
    resource: website/README.md
    title: What the site shows, Preview it and What to edit
  - id: site.toml
    resource: website/site.toml
    title: the site's address, title and redirects
  - id: lychee.toml
    resource: lychee.toml
    title: the comment above the site's address in exclude
  - id: justfile
    resource: justfile
    title: the testdoc and _serve recipes
generated:
  by: process:ktl-librarian
  at: "2026-11-15T03:02:58Z"
status: draft
---

# spdx documentation site

`website/` holds a Hugo site, which the README describes as built from the README, `docs/`, the schema's pages and the knowledge bundle, and whose address it gives as `https://lmodel.github.io/spdx`.[^readme.md] It replaces the mkdocs site that the template set up.

`website/README.md` says that the Knowledge website workflow publishes the site to GitHub Pages at `https://lmodel.github.io/spdx/`.[^website-readme.md] `website/site.toml` gives the address `https://lmodel.github.io/spdx/` and the repository `https://github.com/lmodel/spdx`.[^site.toml] A comment in `lychee.toml` says that the site moves from the mkdocs build to the knowledge website workflow's deploy and may not answer in between, so the link check leaves its address out until the workflow has deployed it.[^lychee.toml]

## What the pages come from

`website/README.md` says that every page comes from a file the repository already holds, so a change to the site is a change to that file:

- each concept in `.lokf/knowledge/` becomes a page under `knowledge/`, with its trust label from `knowledge-report.sh`, its sources and its relations both ways, and the four files `lokf export` writes are served beside them;
- the README becomes the home page, and each page under `docs/` a page under `docs/`;
- `CHANGELOG.md` becomes a page per release under `changelog/`;
- the schema's pages, which LinkML's `gen-doc` writes at build time, become a page each under `schema/`, each also at `elements/<Name>/`.

The site serves no data pages, since `site.toml` sets no `browse`. `site.toml` sends `/about` on to the page built from `docs/about.md`, and each `/schema/<name>/` address on to that element's page. The site itself sends each `/elements/<name>/` address, which the mkdocs site gave a schema page, on to the element's page.

## Previewing it

Previewing needs bash, git and uv. In `website/`, run `scripts/build.sh serve` for a local server, or `scripts/build.sh`, which writes `dist/` and then checks every link between its pages. Hugo and Pagefind come from PyPI. From the repository root, `just testdoc` runs `just gen-doc` and then the same local server.[^justfile]

## Publishing it

[Knowledge website](../workflows/knowledge-website.md) builds the site on pull requests and on the default branch, and deploys it to GitHub Pages only once the repository variable `KNOWLEDGE_WEBSITE_ENABLED` is `true`.

## Editing it

Change a page's words in the file it comes from: the README, a page under `docs/`, the converter that writes the schema, or a concept, which goes through the librarian and the curator like any other change to the bundle. Change the site's own values in `website/site.toml`, and its look in `website/assets/css/custom.css`, which is this repository's own.[^website-readme.md]

[^readme.md]: README.md, Documentation Website and the website item of Repository Structure
[^website-readme.md]: website/README.md, What the site shows, Preview it and What to edit
[^site.toml]: website/site.toml, the site's address, title and redirects
[^lychee.toml]: lychee.toml, the comment above the site's address in exclude
[^justfile]: justfile, the `testdoc` and `_serve` recipes
