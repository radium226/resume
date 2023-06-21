from lxml.etree import Element

from ...xml import create_element


def tab(
    **kwargs,
) -> Element:
    return create_element(
        tag="text:tab",
        **kwargs,
    )