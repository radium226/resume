from lxml.etree import _Element

from ...xml import create_element


def table_column(
    *,
    number_columns_repeated: int | None = None,
    style_name: str | None = None,
    **kwargs,
) -> _Element:
    return create_element(
        tag="table:table-column",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "table:number-columns-repeated": f"{number_columns_repeated}" if number_columns_repeated else None,
            "table:style-name": style_name,
        } },
    )