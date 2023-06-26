from lxml.etree import Element

from .namespaces_by_prefix import NAMESPACES_BY_PREFIX


def set_attribute_to_element(element: Element, name: str, value: str) -> None:
    [namespace_prefix, local_name] = name.split(":")
    namespace = NAMESPACES_BY_PREFIX[namespace_prefix]
    element.attrib["{" + namespace + "}" + local_name] = value