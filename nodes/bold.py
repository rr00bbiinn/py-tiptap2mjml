from dataclasses import dataclass, field
from typing import Any, Self

from .tiptap_node import TiptapNode


@dataclass
class Bold:
    children: list[TiptapNode] = field(default_factory=list)

    def to_mjml(self) -> str:
        inner = "".join(child.to_mjml() for child in self.children)
        return f"<b>{inner}</b>"

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(children=data.get("children", []))
