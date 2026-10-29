"""Validate the example data against the schema, and the SPDX Project's own examples against it.

Local examples: ``tests/data/valid/`` and ``tests/data/problem/valid/`` hold one
file per class, named ``<Class>-<anything>.yaml``, each validated against that
class with closed classes. ``tests/data/invalid/`` and
``tests/data/problem/invalid/`` hold counter-examples, each failing for the one
reason REASONS names. The ``problem/`` folders hold the files the example runner
cannot load because a key is a Python keyword (a Relationship's ``from``, an
SpdxDocument's ``import``); the validator reads them like the others.

Upstream examples: ``tests/data/spdx-examples/`` is the SPDX Project's example
repository. Its SPDX 3 documents are JSON-LD, whose keys differ from this
schema's in two ways the tests undo: a class or property outside Core carries
its profile as a prefix (``software_Package``, ``software_packageVersion``), and
a blank node's identifier is ``@id``. The tests check that every node's type is
a class of the schema, that every required slot is present, and that every
vocabulary value is one its enum declares.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin
from linkml_runtime.utils.schemaview import SchemaView

TESTS_DIR = Path(__file__).parent
SCHEMA_PATH = TESTS_DIR.parent / "src" / "spdx" / "schema" / "spdx.yaml"
DATA_DIR = TESTS_DIR / "data"
UPSTREAM_DIR = DATA_DIR / "spdx-examples"

VALID_FILES = sorted((DATA_DIR / "valid").glob("*.yaml")) + sorted(
    (DATA_DIR / "problem" / "valid").glob("*.yaml")
)
INVALID_FILES = sorted((DATA_DIR / "invalid").glob("*.yaml")) + sorted(
    (DATA_DIR / "problem" / "invalid").glob("*.yaml")
)
UPSTREAM_JSON_FILES = sorted(UPSTREAM_DIR.rglob("*.json"))
UPSTREAM_SPDX3_JSON_FILES = sorted(
    set(UPSTREAM_DIR.rglob("spdx3.0/*.json")) | set(UPSTREAM_DIR.rglob("*.spdx3.json"))
)

# A closed class reports every unexpected key in one message, so the count of
# results alone cannot tell one reason from another: each counter-example names
# the part of the validator's message it must fail with.
REASONS = {
    "CreationInfo-specVersion-not-semver": "'3' does not match",
    "EnergyConsumptionDescription-missing-energyUnit": "'energyUnit' is a required property",
    "File-contentType-not-a-media-type": "'plaintext' does not match",
    "Hash-missing-hashValue": "'hashValue' is a required property",
    "Organization-spdxId-not-an-iri": "is not a 'uri' in /spdxId",
    "Package-missing-creationInfo": "'creationInfo' is a required property",
    "Package-releaseTime-not-utc": "'2024-10-01T12:00:00+01:00' does not match",
    "Person-undeclared-slot": "('email' was unexpected)",
    "PositiveIntegerRange-begin-zero": "0 is less than the minimum of 1",
    "Relationship-missing-to": "'to' is a required property",
    "Sbom-sbomType-unknown-value": "'bogus' is not one of",
    "Snippet-missing-snippetFromFile": "'snippetFromFile' is a required property",
}


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(
        str(SCHEMA_PATH), validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )


def _target_class(path: Path) -> str:
    return path.stem.split("-", 1)[0]


def _messages(validator: Validator, path: Path) -> list[str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict), f"{path} must hold one object"
    return [
        result.message
        for result in validator.validate(data, _target_class(path)).results
    ]


@pytest.mark.parametrize(
    "path", VALID_FILES, ids=lambda p: str(p.relative_to(DATA_DIR))
)
def test_valid_example_validates(validator: Validator, path: Path) -> None:
    assert _messages(validator, path) == []


@pytest.mark.parametrize(
    "path", INVALID_FILES, ids=lambda p: str(p.relative_to(DATA_DIR))
)
def test_invalid_example_fails_once_for_its_reason(
    validator: Validator, path: Path
) -> None:
    assert path.stem in REASONS, (
        f"{path.name}: add the part of the message it must fail with to REASONS"
    )
    messages = _messages(validator, path)
    assert len(messages) == 1, f"{path.name} should fail for one reason, not {messages}"
    assert REASONS[path.stem] in messages[0]


# -- the SPDX Project's examples -------------------------------------------------


def _strip_profile(name: str, known: set[str]) -> str:
    """software_Package -> Package, security_locator stays: the schema knows that slot."""
    if name in known:
        return name
    if "_" in name:
        tail = name.rsplit("_", 1)[-1]
        if tail in known:
            return tail
    return name


def _nodes(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return [
        node
        for node in payload.get("@graph", [])
        if isinstance(node, dict) and isinstance(node.get("type"), str)
    ]


def _as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else [value]


@pytest.mark.parametrize(
    "path", UPSTREAM_JSON_FILES, ids=lambda p: str(p.relative_to(UPSTREAM_DIR))
)
def test_upstream_examples_are_valid_json(path: Path) -> None:
    assert isinstance(json.loads(path.read_text(encoding="utf-8")), dict)


@pytest.mark.parametrize(
    "path", UPSTREAM_SPDX3_JSON_FILES, ids=lambda p: str(p.relative_to(UPSTREAM_DIR))
)
def test_upstream_spdx3_examples_have_jsonld_graph(path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert "@context" in payload
    assert isinstance(payload.get("@graph"), list) and payload["@graph"]


@pytest.mark.parametrize(
    "path", UPSTREAM_SPDX3_JSON_FILES, ids=lambda p: str(p.relative_to(UPSTREAM_DIR))
)
def test_upstream_spdx3_types_are_classes(path: Path, schema_view: SchemaView) -> None:
    classes = set(schema_view.all_classes())
    unknown = {
        node["type"]
        for node in _nodes(path)
        if _strip_profile(node["type"], classes) not in classes
    }
    assert not unknown, (
        f"types the schema has no class for in {path.name}: {sorted(unknown)}"
    )


@pytest.mark.parametrize(
    "path", UPSTREAM_SPDX3_JSON_FILES, ids=lambda p: str(p.relative_to(UPSTREAM_DIR))
)
def test_upstream_spdx3_required_slots_are_present(
    path: Path, schema_view: SchemaView
) -> None:
    classes = set(schema_view.all_classes())
    missing: list[str] = []
    for index, node in enumerate(_nodes(path)):
        class_name = _strip_profile(node["type"], classes)
        if class_name not in classes:
            continue
        slots = {
            slot.name: slot for slot in schema_view.class_induced_slots(class_name)
        }
        keys = {_strip_profile(key, set(slots)) for key in node}
        for name, slot in slots.items():
            if slot.required and name not in keys:
                missing.append(f"{index}:{class_name}.{name}")
    assert not missing, f"required slots missing in {path.name}: {missing}"


@pytest.mark.parametrize(
    "path", UPSTREAM_SPDX3_JSON_FILES, ids=lambda p: str(p.relative_to(UPSTREAM_DIR))
)
def test_upstream_spdx3_vocabulary_values_are_declared(
    path: Path, schema_view: SchemaView
) -> None:
    classes = set(schema_view.all_classes())
    enums = schema_view.all_enums()
    bad: list[str] = []
    for index, node in enumerate(_nodes(path)):
        class_name = _strip_profile(node["type"], classes)
        if class_name not in classes:
            continue
        slots = {
            slot.name: slot for slot in schema_view.class_induced_slots(class_name)
        }
        for key, value in node.items():
            slot = slots.get(_strip_profile(key, set(slots)))
            if slot is None or slot.range not in enums:
                continue
            allowed = set(enums[slot.range].permissible_values)
            for item in _as_list(value):
                if (
                    isinstance(item, str)
                    and not item.startswith(("http://", "https://", "_:"))
                    and item not in allowed
                ):
                    bad.append(f"{index}:{class_name}.{slot.name}={item}")
    assert not bad, f"values no vocabulary declares in {path.name}: {bad}"


@pytest.mark.parametrize(
    "path",
    [p for p in UPSTREAM_JSON_FILES if "spdx2." in str(p)],
    ids=lambda p: str(p.relative_to(UPSTREAM_DIR)),
)
def test_upstream_spdx2_examples_have_expected_markers(path: Path) -> None:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert "spdxVersion" in payload
    assert "SPDXID" in payload
