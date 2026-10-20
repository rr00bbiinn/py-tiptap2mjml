import html
from dataclasses import dataclass
from typing import Any, Self


@dataclass
class Text:
    text: str

    def to_mjml(self) -> str:
        return html.escape(self.text)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        return cls(text=data["text"])
