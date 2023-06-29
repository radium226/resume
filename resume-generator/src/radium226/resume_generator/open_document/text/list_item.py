from lxml.etree import _Element

from ...xml import create_element


def list_item(
    **kwargs,
) -> _Element:
    return create_element(
        tag="text:list-item",
        **kwargs,
    )