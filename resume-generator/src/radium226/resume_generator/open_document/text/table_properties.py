from lxml.etree import Element

from ...xml import create_element


"""
style:width="10.6951in" fo:margin-left="0in" fo:margin-right="0in" table:align="margins" fo:background-color="transparent"
"""

def table_properties(
    *,
    background_color: str | None = None
    align: str | None = None
    margin_right: str | None = None
    margin_left: str | None = None
    width: str | None = None,
    **kwargs,
) -> Element:
    return create_element(
        tag="table:table",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "fo:background-color": background_color,
            "table:align": align,
            "fo:margin-right": margin_right,
            "fo:margin-left": margin_left,
            "style:width": width,
        } },
    )