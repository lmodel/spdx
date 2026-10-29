## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ The upstream model and the generated schema ============

# src/spdx_linkml/schema/upstream/spdx-model.ttl is the SPDX model as the SPDX
# Project publishes it, and scripts/spdx_to_linkml.py writes every YAML file in
# src/spdx_linkml/schema/ from that copy. These recipes regenerate the schema,
# tell a hand edit from a regeneration, and compare the vendored model with the
# published releases.

# Rewrite src/spdx_linkml/schema/*.yaml from the vendored SPDX model
[group('model development')]
gen-linkml:
  uv run python scripts/spdx_to_linkml.py

# Fail when src/spdx_linkml/schema/*.yaml differs from a fresh gen-linkml
[group('model development')]
gen-linkml-check:
  uv run python scripts/spdx_to_linkml.py --check

# Compare the vendored model with the SPDX Project's published releases
[group('model development')]
upstream-check:
  uv run python scripts/check_upstream_release.py

# Run the data tests alone: the local examples and the upstream SPDX examples
[group('model development')]
test-data:
  uv run python -m pytest tests/test_data.py

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/spdx.yaml` is the copy `lokf adapt` writes from the schema so that it
# can sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the moves). The
# root is Element, the one class SPDX gives an identifier: every class a
# knowledge concept may name as its `type` descends from it, and the copy puts
# LOKF's `id` in place of `spdxId`. Re-rooting a subclass such as Package on
# `Concept` would cut it off from the fields it inherits, and `lokf adapt`
# refuses a copy in which Element lists `id` but does not descend from
# `Concept`. A name the copy shares with lokf.yaml takes the prefix `spdx`
# and keeps its SPDX IRI. The recipes run the `lokf` the sidecar's floor pins
# (0.9.0 or later); LOKF_CMD runs another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root Element"

# Rewrite .lokf/spdx.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --prefix spdx --lokf .lokf/lokf.yaml -o .lokf/spdx.yaml

# Fail when .lokf/spdx.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --prefix spdx --lokf .lokf/lokf.yaml -o .lokf/spdx.yaml --check
