from typing import Optional, Union
from lxml.etree import Element, _Element

from .namespaces_by_prefix import NAMESPACES_BY_PREFIX
from .set_attribute_to_element import set_attribute_to_element
from .append_children_to_parent_element import append_children_to_parent_element


def create_element(tag: str, attributes: dict[str, str] = {}, children: list[Union[_Element, str]] = [], parent: Optional[_Element] = None, text: str | None = None) -> _Element:
    [namespace_prefix, local_tag] = tag.split(":")
    namespace = NAMESPACES_BY_PREFIX[namespace_prefix]
    element = Element(
        "{" + namespace + "}" + local_tag,
    )

    if parent is not None:
        parent.append(element)

    if text:
        element.text = text

    for attribute_name, attribute_value in attributes.items():
        if attribute_value is not None:
            set_attribute_to_element(element, attribute_name, attribute_value)

    append_children_to_parent_element(element, children)

    return element