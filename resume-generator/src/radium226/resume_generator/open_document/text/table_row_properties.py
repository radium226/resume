from lxml.etree import _Element

from ...xml import create_element


def table_row_properties(
    *,
    row_height: str | None = None,
    background_color: str | None = None,
    **kwargs,
) -> _Element:
    return create_element(
        tag="style:table-row-properties",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "style:row-height": row_height,
            "fo:background-color": background_color,
        } },
    )