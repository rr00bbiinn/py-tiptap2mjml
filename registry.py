import collections.abc as cabc

from .nodes import Bold, Doc, Paragraph, Text, TiptapNode

type RegistryType = cabc.Mapping[str, type[TiptapNode]]

NODES: RegistryType = {
    "doc": Doc,
    "text": Text,
    "paragraph": Paragraph,
}

MARKS: RegistryType = {
    "bold": Bold,
}
