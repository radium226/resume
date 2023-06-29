from lxml.etree import _Element

from ...xml import create_element


def table_cell(
    *,
    style_name: str | None = None,
    number_columns_spanned: int | None = None,
    number_rows_spanned: int | None = None,
    **kwargs,
) -> _Element:
    return create_element(
        tag="table:table-cell",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "table:style-name": style_name,
            "table:number-columns-spanned": None if number_columns_spanned is None else f"{number_columns_spanned}",
            "table:number-rows-spanned": None if number_rows_spanned is None else f"{number_rows_spanned}",
        } },
    )