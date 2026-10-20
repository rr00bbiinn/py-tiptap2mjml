from typing import Any, Protocol, Self


class TiptapNode(Protocol):
    def to_mjml(self) -> str: ...

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self: ...
