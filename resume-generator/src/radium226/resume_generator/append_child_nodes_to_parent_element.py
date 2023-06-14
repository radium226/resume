from typing import TypeAlias, Union
from lxml.etree import Element

Node: TypeAlias = Union[Element, str]

def append_child_nodes_to_parent_element(parent_element: Element, child_nodes: list[Node]) -> None:
    for index, child_node in enumerate(child_nodes):
        match child_node:
            case str() if index == 0:
                parent_element.text = child_node

            case str():
                child_nodes[index - 1].tail = child_node

            case _:
                parent_element.append(child_node)