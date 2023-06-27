from dataclasses import dataclass


@dataclass
class EmbeddedImage():

    name: str
    content: bytes
    mime_type: str