from lxml.etree import _Element

from ...xml import create_element


def span(
    *,
    style_name: str | None = None,
    **kwargs,
) -> _Element:
    return create_element(
        tag="text:span",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "text:style-name": style_name,
        } },
    )