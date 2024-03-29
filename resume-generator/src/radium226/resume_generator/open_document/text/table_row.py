from lxml.etree import _Element

from ...xml import create_element


def table_row(
    style_name: str | None = None,
    **kwargs,
) -> _Element:
    return create_element(
        tag="table:table-row",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "table:style-name": style_name,
        } },
    )