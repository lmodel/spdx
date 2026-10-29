# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change bumps the minor version. See [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers).

## [Unreleased]

## [0.1.0] - 2026-10-29

### Added

- **A LinkML schema of the SPDX 3.0.1 model, one module for each of its nine profiles.** `scripts/spdx_to_linkml.py` writes it from a copy of the model the SPDX Project publishes, and a weekly upstream watch compares that copy with the release.
- **`.lokf/spdx.yaml`, the schema's `lokf adapt` copy, rooted on Element**, which the knowledge release attaches as `schema-<tag>-spdx.yaml`. Tests hold its names apart from `lokf.yaml` and pin the class and four keys it shares with oscal's and slsa's copies.
- **A counter-example for each constraint the schema states**, and two tests that fail when a required slot or an enum has none.
- **The repository's KTL knowledge bundle and its sidecar automation**, from the KTL v0.59.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.

### Changed

- **Every SPDX property is a top-level slot.** A property that one class used was an attribute of it, which `lokf adapt` never renames; the data the schema validates is unchanged.

### Fixed

- **The schema binds the root of SPDX 3.0.1's terms as `spdx3`.** LOKF binds `spdx` to SPDX 2's namespace, so a composite that imported both could not merge them.
