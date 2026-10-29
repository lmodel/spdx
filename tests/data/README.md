# Example data for spdx_linkml

This folder holds the examples the tests validate against the schema:

- `valid/` holds data that conforms to the schema, one or more files for each
  concrete class.
- `invalid/` holds counter-examples, one for each constraint the schema states.
  Each fails for one reason, and its name says which.
- `problem/valid/` and `problem/invalid/` hold the examples the example runner
  cannot load, because a key is a Python keyword: a Relationship's `from` and an
  SpdxDocument's `import`. `tests/test_data.py` validates them like the others.
- `spdx-examples/` is a copy of the SPDX Project's example repository.

A file's name is `<Class>-<anything>.yaml`, and the test validates the file
against the class before the first `-`. A counter-example's name gives its
fault: `<Class>-missing-<slot>` for a required slot, `<Class>-<slot>-unknown-value`
for a value outside an enum, and a name in `REASONS` in `tests/test_data.py`
for any other. An example's `type` is a class CURIE, such as
`spdx_software:Package`.
