from lxml.etree import Element

from ...xml import create_element


def list_item(
    **kwargs,
) -> Element:
    return create_element(
        tag="text:list-item",
        **kwargs,
    )