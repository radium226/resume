from typing import Union
from lxml.etree import _Element


def append_children_to_parent_element(parent_element: _Element, children: list[Union[_Element, str]]) -> None:
    for index, child in enumerate(children):
        match child:
            case str() if index == 0:
                parent_element.text = child

            case str():
                match children[index - 1]:
                    case str():
                        parent_element.text = (parent_element.text or "") + child
                        
                    case _Element():
                        previous_child = children[index - 1]
                        match previous_child:
                            case _Element():
                                previous_child.tail = child
                            case _:
                                raise Exception("We should not be here! ")

            case _:
                parent_element.append(child)