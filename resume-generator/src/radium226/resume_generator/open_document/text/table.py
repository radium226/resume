from lxml.etree import _Element

from ...xml import create_element


def table(
    *,
    name: str,
    style_name: str | None = None,
    **kwargs,
) -> _Element:
    return create_element(
        tag="table:table",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "table:style-name": style_name,
            "table:name": name,
        } },
    )