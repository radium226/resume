from lxml.etree import _Element

from ...xml import create_element


def s(
) -> _Element:
    return create_element(
        tag="text:s",
    )