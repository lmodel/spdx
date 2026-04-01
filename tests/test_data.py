"""Schema-driven tests for local fixtures and upstream SPDX examples."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import yaml
from linkml_runtime.utils.schemaview import SchemaView

TESTS_DIR = Path(__file__).parent
SCHEMA_PATH = TESTS_DIR.parent / "src" / "spdx" / "schema" / "spdx.yaml"

DATA_DIR = TESTS_DIR / "data"
DATA_DIR_VALID = DATA_DIR / "valid"
DATA_DIR_INVALID = DATA_DIR / "invalid"
DATA_DIR_UPSTREAM = DATA_DIR / "spdx-examples"

VALID_EXAMPLE_FILES = sorted(DATA_DIR_VALID.glob("*.yaml"))
INVALID_EXAMPLE_FILES = sorted(DATA_DIR_INVALID.glob("*.yaml"))
UPSTREAM_JSON_FILES = sorted(DATA_DIR_UPSTREAM.rglob("*.json"))
UPSTREAM_SPDX3_JSON_FILES = sorted(
    set(DATA_DIR_UPSTREAM.rglob("spdx3.0/*.json"))
    | set(DATA_DIR_UPSTREAM.rglob("*.spdx3.json"))
)

# Known upstream SPDX 3.0 example mismatches against this LinkML schema.
# Keep this list intentionally small and explicit.
UPSTREAM_SPDX3_ALLOWED_MISSING_REQUIRED: set[tuple[str, str]] = {
    ("LicenseExpression", "licenseExpression"),
    ("DatasetPackage", "datasetType"),
    ("CustomLicense", "licenseText"),
}


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


def _class_names(schema_view: SchemaView) -> set[str]:
    return set(schema_view.all_classes().keys())


def _normalize_type_name(type_name: str, classes: set[str]) -> str:
    if type_name in classes:
        return type_name
    # SPDX JSON-LD examples often use module-prefixed type names like
    # "software_Package" or "simplelicensing_LicenseExpression".
    if "_" in type_name:
        tail = type_name.rsplit("_", 1)[-1]
        if tail in classes:
            return tail
    return type_name


def _required_slot_names(schema_view: SchemaView, class_name: str) -> set[str]:
    return {slot.name for slot in schema_view.class_induced_slots(class_name) if slot.required}


def _missing_required_slots(
    schema_view: SchemaView,
    class_name: str,
    payload: dict[str, Any],
) -> list[str]:
    return sorted(slot for slot in _required_slot_names(schema_view, class_name) if slot not in payload)


def _load_yaml_dict(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise AssertionError(f"Expected top-level mapping in {path}, got {type(data)!r}")
    return data


def _fixture_target_class(path: Path) -> str:
    return path.stem.split("-", 1)[0]


def _spdx2_json_files() -> list[Path]:
    return [path for path in UPSTREAM_JSON_FILES if "spdx2." in str(path)]


def _as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    return [value]


def _enum_range_for_slot(schema_view: SchemaView, slot_name: str) -> tuple[str | None, bool]:
    slot = schema_view.induced_slot(slot_name)
    enums = schema_view.all_enums()

    if slot.any_of:
        ranges = [choice.range for choice in slot.any_of if getattr(choice, "range", None)]
        enum_ranges = [range_name for range_name in ranges if range_name in enums]
        if enum_ranges:
            return enum_ranges[0], "string" in ranges

    if slot.range in enums:
        return slot.range, False
    return None, False


def _enum_allowed_values(schema_view: SchemaView, enum_name: str) -> set[str]:
    enum = schema_view.all_enums()[enum_name]
    allowed = set(enum.permissible_values.keys())
    for permissible in enum.permissible_values.values():
        meaning = getattr(permissible, "meaning", None)
        if isinstance(meaning, str):
            allowed.add(meaning.rstrip("/").rsplit("/", 1)[-1])
    return allowed


@pytest.mark.parametrize("path", VALID_EXAMPLE_FILES, ids=lambda p: str(p.relative_to(TESTS_DIR)))
def test_valid_data_files_conform_required_slots(path: Path, schema_view: SchemaView) -> None:
    """All local valid fixtures should map to a known class and satisfy required slots."""
    payload = _load_yaml_dict(path)
    class_name = _fixture_target_class(path)
    classes = _class_names(schema_view)
    assert class_name in classes, f"Unknown class in filename: {class_name} ({path})"

    missing = _missing_required_slots(schema_view, class_name, payload)
    assert not missing, f"Missing required slots for {class_name} in {path}: {missing}"


@pytest.mark.parametrize("path", INVALID_EXAMPLE_FILES, ids=lambda p: str(p.relative_to(TESTS_DIR)))
def test_invalid_data_files_break_required_slots(path: Path, schema_view: SchemaView) -> None:
    """All local invalid fixtures should fail required-slot checks or class resolution."""
    payload = _load_yaml_dict(path)
    class_name = _fixture_target_class(path)
    classes = _class_names(schema_view)
    if class_name not in classes:
        return

    missing = _missing_required_slots(schema_view, class_name, payload)
    assert missing, f"Invalid fixture unexpectedly satisfies required slots: {path}"


@pytest.mark.parametrize("path", UPSTREAM_JSON_FILES, ids=lambda p: str(p.relative_to(TESTS_DIR)))
def test_upstream_examples_are_valid_json(path: Path) -> None:
    """Every upstream file tracked as JSON must be parseable."""
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)
    assert isinstance(payload, dict)


@pytest.mark.parametrize("path", UPSTREAM_SPDX3_JSON_FILES, ids=lambda p: str(p.relative_to(TESTS_DIR)))
def test_upstream_spdx3_examples_have_jsonld_graph(path: Path) -> None:
    """SPDX 3.0 examples should be JSON-LD graph payloads."""
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    assert "@context" in payload
    assert isinstance(payload.get("@graph"), list)
    assert payload["@graph"], f"Expected non-empty @graph in {path}"


@pytest.mark.parametrize("path", UPSTREAM_SPDX3_JSON_FILES, ids=lambda p: str(p.relative_to(TESTS_DIR)))
def test_upstream_spdx3_types_exist_in_schema(path: Path, schema_view: SchemaView) -> None:
    """Every SPDX 3.0 graph node type should resolve to a known class."""
    classes = _class_names(schema_view)
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    graph = payload.get("@graph", [])
    unknown_types: set[str] = set()
    for node in graph:
        if not isinstance(node, dict):
            continue
        raw_type = node.get("type")
        if not isinstance(raw_type, str):
            continue
        normalized = _normalize_type_name(raw_type, classes)
        if normalized not in classes:
            unknown_types.add(raw_type)

    assert not unknown_types, f"Unknown types in {path}: {sorted(unknown_types)}"


@pytest.mark.parametrize("path", UPSTREAM_SPDX3_JSON_FILES, ids=lambda p: str(p.relative_to(TESTS_DIR)))
def test_upstream_spdx3_required_slots_with_allowlist(path: Path, schema_view: SchemaView) -> None:
    """SPDX 3.0 examples should satisfy required slots except known upstream/schema deltas."""
    classes = _class_names(schema_view)
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    violations: list[str] = []
    for index, node in enumerate(payload.get("@graph", [])):
        if not isinstance(node, dict):
            continue
        raw_type = node.get("type")
        if not isinstance(raw_type, str):
            continue
        class_name = _normalize_type_name(raw_type, classes)
        if class_name not in classes:
            continue

        missing = _missing_required_slots(schema_view, class_name, node)
        for slot_name in missing:
            if (class_name, slot_name) not in UPSTREAM_SPDX3_ALLOWED_MISSING_REQUIRED:
                violations.append(f"{index}:{class_name}.{slot_name}")

    assert not violations, f"Unexpected missing required slots in {path}: {violations}"


@pytest.mark.parametrize("path", UPSTREAM_SPDX3_JSON_FILES, ids=lambda p: str(p.relative_to(TESTS_DIR)))
def test_upstream_spdx3_enum_values(path: Path, schema_view: SchemaView) -> None:
    """SPDX 3.0 examples should use valid enum values for closed enums."""
    classes = _class_names(schema_view)
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    violations: list[str] = []
    for index, node in enumerate(payload.get("@graph", [])):
        if not isinstance(node, dict):
            continue
        raw_type = node.get("type")
        if not isinstance(raw_type, str):
            continue
        class_name = _normalize_type_name(raw_type, classes)
        if class_name not in classes:
            continue

        for slot in schema_view.class_induced_slots(class_name):
            if slot.name not in node:
                continue
            enum_name, open_enum = _enum_range_for_slot(schema_view, slot.name)
            if enum_name is None:
                continue

            allowed = _enum_allowed_values(schema_view, enum_name)
            for value in _as_list(node[slot.name]):
                if not isinstance(value, str):
                    continue
                # URIs and blank nodes are references, not enum literals.
                if value.startswith("http://") or value.startswith("https://") or value.startswith("_:"):
                    continue
                if value in allowed:
                    continue
                if open_enum:
                    continue
                violations.append(f"{index}:{class_name}.{slot.name}={value}")

    assert not violations, f"Invalid closed-enum values in {path}: {violations}"


@pytest.mark.parametrize("path", _spdx2_json_files(), ids=lambda p: str(p.relative_to(TESTS_DIR)))
def test_upstream_spdx2_examples_have_expected_markers(path: Path) -> None:
    """SPDX 2.x examples should expose canonical SPDX JSON markers."""
    with path.open("r", encoding="utf-8") as handle:
        payload = json.load(handle)

    assert "spdxVersion" in payload
    assert "SPDXID" in payload
