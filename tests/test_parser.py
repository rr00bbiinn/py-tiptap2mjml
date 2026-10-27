import pytest

from tiptap2mjml import parse, to_mjml


def _mjml(inner: str) -> str:
    return (
        "<mjml><mj-body><mj-section><mj-column>"
        f"{inner}"
        "</mj-column></mj-section></mj-body></mjml>"
    )


def test_empty_doc():
    assert to_mjml({"type": "doc"}) == _mjml("")
