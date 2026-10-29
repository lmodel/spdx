<a href="https://github.com/dalito/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# spdx

System Package Data Exchange (SPDX): LinkML Schema

## Documentation Website

[https://lmodel.github.io/spdx](https://lmodel.github.io/spdx)

## Repository Structure

* [docs/](docs/): mkdocs-managed documentation
  * [elements/](docs/elements/): generated schema documentation
* [examples/](examples/): examples of using the schema
* [project/](project/): project files, generated, so do not edit them
* [scripts/](scripts/): the converter that writes the schema from the SPDX model, and the upstream check
* [src/](src/): source files
  * [spdx](src/spdx)
    * [schema/](src/spdx/schema): the LinkML schema, one module per SPDX
      profile, written by `scripts/spdx_to_linkml.py`, so do not edit it
      * [upstream/](src/spdx/schema/upstream): the SPDX model the schema
        is generated from
    * [datamodel/](src/spdx/datamodel): the generated
      Python datamodel
* [tests/](tests/): Python tests
  * [data/](tests/data): example data

## Upstream model

`scripts/spdx_to_linkml.py` writes the schema from the SPDX model the SPDX
Project publishes, vendored at `src/spdx/schema/upstream/spdx-model.ttl`.
[docs/about.md](docs/about.md) gives the recipes that regenerate and check the
schema, says what the rendering adds to the model, and says where it differs
from SPDX's serialisations.

## Developer Tools

There are several pre-defined command-recipes available.
They are written for the command runner [just](https://github.com/casey/just/). To list all pre-defined commands, run `just` or `just --list`.

## Credits

This project uses the template [linkml-project-copier](https://github.com/dalito/linkml-project-copier) published as [doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584).
