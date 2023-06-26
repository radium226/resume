from typing import Union
from lxml.etree import Element


def append_children_to_parent_element(parent_element: Element, children: list[Union[Element, str]]) -> None:
    for index, child in enumerate(children):
        match child:
            case str() if index == 0:
                parent_element.text = child

            case str():
                match children[index - 1]:
                    case str():
                        parent_element.text = parent_element.text + child
                    case _:
                        children[index - 1].tail = child

            case _:
                parent_element.append(child)