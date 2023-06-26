from lxml.etree import Element

from ...xml import create_element


def section(
    *,
    name: str,
    style_name: str | None = None,
    **kwargs,
) -> Element:
    return create_element(
        tag="text:section",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "text:style-name": style_name,
            "text:name": name,
        } },
    )