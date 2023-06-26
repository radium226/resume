from lxml.etree import Element

from ...xml import create_element


def table_cell(
    *,
    style_name: str | None = None,
    number_columns_spanned: int | None = None,
    **kwargs,
) -> Element:
    return create_element(
        tag="table:table-cell",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "table:style-name": style_name,
            "table:number-columns-spanned": None if number_columns_spanned is None else f"{number_columns_spanned}"
        } },
    )