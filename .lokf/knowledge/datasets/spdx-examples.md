---
type: Dataset
id: https://w3id.org/lmodel/spdx/knowledge/datasets/spdx-examples
genre: reference
title: SPDX examples copy
description: "tests/data/spdx-examples/, a copy of the SPDX Project's spdx-examples repository under GPL-3.0: 44 JSON files, 26 of them SPDX 3 documents in JSON-LD, which tests/test_data.py reads for class names, required fields and vocabulary values; the copy's links and spelling are upstream's, so the linters leave it alone."
resource: tests/data/spdx-examples
source:
  - https://github.com/spdx/spdx-examples
sources:
  - id: spdx-examples-readme.md
    resource: tests/data/spdx-examples/README.md
    title: the profiles the examples are sorted by
  - id: copying
    resource: tests/data/spdx-examples/COPYING
    title: the GNU General Public License, version 3
  - id: test_data.py
    resource: tests/test_data.py
    title: the docstring and the upstream tests
  - resource: NOTICE
    title: the SPDX examples section
  - resource: lychee.toml
    title: the excluded paths
generated:
  by: process:ktl-librarian
  at: "2026-10-29T19:19:54Z"
status: draft
---

# SPDX examples copy

`tests/data/spdx-examples/` is a copy of the SPDX Project's spdx-examples repository. Its README says that the repository demonstrates SPDX for various scenarios and use cases, sorted by profile: AI, Dataset, Hardware, Regulatory Conformance and Software, with presentations beside them.[^spdx-examples-readme.md] It is licensed under the GNU General Public License, version 3, whose text is `COPYING`, and some example contents carry a licence file of their own.[^copying]

## What the tests read

The copy holds 44 JSON files. 26 of them are SPDX 3 documents, the files in an `spdx3.0/` folder or named `*.spdx3.json`, and the other 18 are SPDX 2.2 and 2.3 documents. `tests/test_data.py` reads them as plain JSON.[^test_data.py] Its docstring says that SPDX JSON-LD differs from the schema's keys in two ways that the tests undo: a class or property outside Core carries its profile as a prefix, such as `software_Package`, and a blank node's identifier is `@id`. The tests check that each document parses and that each SPDX 3 document has a JSON-LD graph. They also check that every node's type is a class of the schema, that every required slot is present, and that every vocabulary value is one its enum declares. The 11 SPDX 2 documents under an `spdx2.2/` or `spdx2.3/` folder need only carry `spdxVersion` and `SPDXID`.

## What the repository leaves alone

The files are copied as published, so `lychee.toml`, `.markdownlint-cli2.jsonc`, codespell, typos, ruff and the pre-commit hooks leave the copy out. Its links and its spelling are upstream's to keep. [Test data and schema tests](test-data.md) describes the tests.

[^spdx-examples-readme.md]: tests/data/spdx-examples/README.md, the profiles the examples are sorted by
[^copying]: tests/data/spdx-examples/COPYING, the GNU General Public License, version 3
[^test_data.py]: tests/test_data.py, the docstring and the upstream tests
