from lxml.etree import Element

from ...xml import create_element


def style(
    *,
    name: str,
    family: str,
    **kwargs,
) -> Element:
    return create_element(
        tag="table:table",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "style:name": name,
            "style:family": family,
        } },
    )