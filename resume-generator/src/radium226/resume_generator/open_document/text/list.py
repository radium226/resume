from lxml.etree import Element

from ...xml import create_element


def list(
    *,
    style_name: str | None = None,
    **kwargs,
) -> Element:
    return create_element(
        tag="text:list",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "text:style-name": style_name,
        } },
    )
