<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# spdx

System Package Data Exchange (SPDX): LinkML Schema

## Documentation Website

[https://lmodel.github.io/spdx](https://lmodel.github.io/spdx)

## Repository Structure

* [docs/](docs/) - mkdocs-managed documentation
  * [elements/](docs/elements/) - generated schema documentation
* [examples/](examples/) - Examples of using the schema
* [project/](project/) - project files (these files are auto-generated, do not edit)
* [scripts/](scripts/) - the converter that writes the schema from the SPDX model, and the upstream check
* [src/](src/) - source files (edit these)
  * [spdx](src/spdx)
    * [schema/](src/spdx/schema) -- LinkML schema, one module per SPDX
      profile, written by `scripts/spdx_to_linkml.py`
      * [upstream/](src/spdx/schema/upstream) -- the SPDX model this
        schema is generated from
    * [datamodel/](src/spdx/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests
  * [data/](tests/data) - Example data

## Upstream model

The schema is generated from the SPDX model the SPDX Project publishes,
vendored at `src/spdx/schema/upstream/spdx-model.ttl`. `just gen-linkml`
rewrites the schema from it, `just gen-linkml-check` fails when a schema file
was edited by hand, and `just upstream-check` says whether the vendored copy
still matches the published model and whether a newer SPDX release exists.
[docs/about.md](docs/about.md) says what the rendering adds to the model.

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
