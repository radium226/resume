from lxml.etree import Element

from ...xml import create_element


def table_column(
    *,
    number_columns_repeated: int,
    style_name: str | None = None,
    **kwargs,
) -> Element:
    return create_element(
        tag="table:table-column",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "table:number-columns-repeated": f"{number_columns_repeated}",
            "table:style-name": style_name,
        } },
    )