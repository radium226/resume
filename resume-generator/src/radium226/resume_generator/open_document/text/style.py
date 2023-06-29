from lxml.etree import _Element

from ...xml import create_element


def style(
    *,
    name: str,
    family: str,
    **kwargs,
) -> _Element:
    return create_element(
        tag="table:table",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "style:name": name,
            "style:family": family,
        } },
    )