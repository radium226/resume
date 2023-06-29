from lxml.etree import _Element

from ...xml import create_element


def h(
    *,
    outline_level: int,
    style_name: str | None = None,
    **kwargs,
) -> _Element:
    return create_element(
        tag="text:h",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "text:outline-level": f"{outline_level}",
            "text:style-name": style_name,
        } },
    )