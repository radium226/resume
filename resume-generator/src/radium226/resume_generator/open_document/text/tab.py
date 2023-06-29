from lxml.etree import _Element

from ...xml import create_element


def tab(
    **kwargs,
) -> _Element:
    return create_element(
        tag="text:tab",
        **kwargs,
    )