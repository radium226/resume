from typing import Protocol
from lxml.etree import _Element


class Block(Protocol):

    def to_elements(self) -> list[_Element]:
        pass