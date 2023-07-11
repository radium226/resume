from dataclasses import dataclass, field

from lxml.etree import _Element

from .block import Block
from .xml import create_element


@dataclass
class Content(Block):

    child_blocks: list[Block] = field(default_factory=list)

    def __iadd__(self, block: Block) -> "Body":
        self.child_blocks.append(block)
        return self

    
    def to_elements(self) -> list[_Element]:
        return [
            create_element(
                "office:body",
                children=[element for child_block in self.child_blocks for element in child_block.to_elements()]
            ),
        ]