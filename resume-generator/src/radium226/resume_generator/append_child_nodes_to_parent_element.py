from typing import TypeAlias, Union
from lxml.etree import Element

Node: TypeAlias = Union[Element, str]

def append_child_nodes_to_parent_element(parent_element: Element, child_nodes: list[Node]) -> None:
    pass