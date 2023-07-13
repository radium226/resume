from typing import Generator
from dataclasses import dataclass, field
from lxml.etree import _Element

from .block import Block

from .xml import create_element


@dataclass
class Span(Block):

    children: list[Block | str] = field(default_factory=list)

    style_name: str | None = None

    def to_elements(self) -> list[_Element]:

        def iter_child_elements() -> Generator[_Element, None, None]:
            for child in self.children:
                match child:
                    case Block():
                        yield from child.to_elements()

                    case str():
                        yield child

        return [
            create_element(
                "text:span",
                attributes={
                    "text:style-name": self.style_name,
                },
                children=list(iter_child_elements()),
            ),
        ]