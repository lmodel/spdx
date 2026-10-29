"""Write each valid example as RDF through the LinkML Python runtime, as SPDX's SHACL reads it.

SPDX's shapes find a node by its ``rdf:type``, and hold each timestamp to a
pattern that ends in ``Z``. So every node must have an SPDX class as its type,
and every ``xsd:dateTimeStamp`` must keep the ``Z`` it was written with. The
examples under ``tests/data/problem/`` are left out, because the runtime cannot
load a ``from`` or an ``import`` key.
"""

from __future__ import annotations

from pathlib import Path

import pytest
from linkml_runtime.dumpers import rdflib_dumper
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView
from rdflib import RDF, XSD, Graph, Literal, URIRef

from spdx_linkml.datamodel import spdx_linkml as datamodel

TESTS_DIR = Path(__file__).parent
SCHEMA_PATH = TESTS_DIR.parent / "src" / "spdx_linkml" / "schema" / "spdx_linkml.yaml"
VALID_FILES = sorted((TESTS_DIR / "data" / "valid").glob("*.yaml"))


@pytest.fixture(scope="module")
def schema_view() -> SchemaView:
    return SchemaView(str(SCHEMA_PATH))


@pytest.fixture(scope="module")
def spdx_terms(schema_view: SchemaView) -> str:
    return schema_view.namespaces()["spdx3"]


def _graph(path: Path, schema_view: SchemaView) -> Graph:
    target = getattr(datamodel, path.stem.split("-", 1)[0])
    instance = yaml_loader.load(str(path), target_class=target)
    return rdflib_dumper.as_rdf_graph(instance, schemaview=schema_view)


@pytest.mark.parametrize("path", VALID_FILES, ids=lambda p: p.name)
def test_every_node_has_an_spdx_class(
    path: Path, schema_view: SchemaView, spdx_terms: str
) -> None:
    graph = _graph(path, schema_view)
    for node in set(graph.subjects()):
        types = list(graph.objects(node, RDF.type))
        assert types, f"{node} has no rdf:type"
        for t in types:
            assert isinstance(t, URIRef) and str(t).startswith(spdx_terms), (
                f"{node} has the type {t!r}"
            )


@pytest.mark.parametrize("path", VALID_FILES, ids=lambda p: p.name)
def test_timestamps_keep_their_z(path: Path, schema_view: SchemaView) -> None:
    stamps = [
        o
        for o in _graph(path, schema_view).objects()
        if isinstance(o, Literal) and o.datatype == XSD.dateTimeStamp
    ]
    assert all(str(o).endswith("Z") for o in stamps), stamps


# When this passes, drop the strict xfail and the matching paragraph in
# docs/about.md.
@pytest.mark.xfail(
    strict=True,
    reason="linkml-runtime 1.12.1 writes an xsd:anyURI value as an IRI, "
    "and SPDX's SHACL wants a literal",
)
def test_any_uri_values_are_literals(schema_view: SchemaView, spdx_terms: str) -> None:
    graph = _graph(TESTS_DIR / "data" / "valid" / "Package-with-hash.yaml", schema_view)
    values = list(graph.objects(None, URIRef(spdx_terms + "Software/downloadLocation")))
    assert values
    assert all(isinstance(v, Literal) and v.datatype == XSD.anyURI for v in values)
