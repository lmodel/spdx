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
