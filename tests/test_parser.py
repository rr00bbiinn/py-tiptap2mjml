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


def test_root_wrong_type():
    with pytest.raises(ValueError, match="Root node must be of type 'doc'"):
        to_mjml({"type": "paragraph"})


def test_root_missing_type():
    with pytest.raises(ValueError, match="Root node must be of type 'doc'"):
        to_mjml({})


def test_paragraph_with_text():
    doc = {
        "type": "doc",
        "content": [
            {"type": "paragraph", "content": [{"type": "text", "text": "Hello"}]},
        ],
    }
    assert to_mjml(doc) == _mjml("<mj-text>Hello</mj-text>")
