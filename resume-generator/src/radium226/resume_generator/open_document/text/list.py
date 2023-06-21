from lxml.etree import Element

from ...xml import create_element


def list(
    **kwargs,
) -> Element:
    return create_element(
        tag="text:list",
        **kwargs,
    )
