from typing import Optional, Union

from lxml.etree import Element


NAMESPACES_BY_PREFIX = {
    "table": "urn:oasis:names:tc:opendocument:xmlns:table:1.0",
    "text": "urn:oasis:names:tc:opendocument:xmlns:text:1.0",
    "office": "urn:oasis:names:tc:opendocument:xmlns:office:1.0",
}


def create_element(tag: str, attributes: dict[str, str] = {}, children: list[Union[Element, str]] = [], parent: Optional[Element] = None, text: str | None = None) -> Element:
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


def set_attribute_to_element(element: Element, name: str, value: str):
    [namespace_prefix, local_name] = name.split(":")
    namespace = NAMESPACES_BY_PREFIX[namespace_prefix]
    element.attrib["{" + namespace + "}" + local_name] = value


def append_children_to_parent_element(parent_element: Element, children: list[Union[Element, str]]) -> None:
    for index, child in enumerate(children):
        match child:
            case str() if index == 0:
                parent_element.text = child

            case str():
                children[index - 1].tail = child

            case _:
                parent_element.append(child)