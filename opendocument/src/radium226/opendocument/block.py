from typing import Protocol, runtime_checkable
from lxml.etree import _Element


@runtime_checkable
class Block(Protocol):

    def to_elements(self) -> list[_Element]:
        pass