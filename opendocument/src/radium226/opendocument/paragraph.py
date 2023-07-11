from dataclasses import dataclass
from lxml.etree import _Element

from .block import Block

from .xml import create_element

@dataclass
class Paragraph(Block):

    text: str

    def to_elements(self) -> list[_Element]:
        return [
            create_element(
                "text:p",
                children=[self.text],
            ),
        ]