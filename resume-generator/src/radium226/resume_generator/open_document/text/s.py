from lxml.etree import Element

from ...xml import create_element


def s(
) -> Element:
    return create_element(
        tag="text:s",
    )