from typing import Any

import collections.abc as cabc

from .nodes import TiptapNode
from .registry import MARKS, NODES, RegistryType


def _node_from_dict(
    data: cabc.Mapping[str, Any], nodes: RegistryType, marks: RegistryType
) -> TiptapNode:
    node_type = data.get("type")
    if not isinstance(node_type, str) or node_type not in nodes:
        raise ValueError(f"Node not found in registry: {node_type}")

    children = [
        _node_from_dict(child, nodes, marks) for child in data.get("content", [])
    ]
    node = nodes[node_type].from_dict({**data, "children": children})

    for mark in data.get("marks", []):
        mark_type = mark.get("type")
        if not isinstance(mark_type, str) or mark_type not in marks:
            raise ValueError(f"Mark not found in registry: {mark_type}")

        node = marks[mark_type].from_dict({**mark, "children": [node]})

    return node


def parse(
    doc: cabc.Mapping[str, Any],
    *,
    nodes: RegistryType = NODES,
    marks: RegistryType = MARKS,
) -> TiptapNode:
    if doc.get("type") != "doc":
        raise ValueError(f"Root node must be of type 'doc', got: {doc.get('type')}")

    return _node_from_dict(doc, nodes, marks)


def to_mjml(
    doc: cabc.Mapping[str, Any],
    *,
    nodes: RegistryType = NODES,
    marks: RegistryType = MARKS,
) -> str:
    return parse(doc, nodes=nodes, marks=marks).to_mjml()
