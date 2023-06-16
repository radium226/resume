from lxml.etree import Element
from .xml import *


def h(
    *,
    outline_level: int,
    style_name: str | None = None,
    **kwargs,
) -> Element:
    return create_element(
        tag="text:h",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "text:outline-level": f"{outline_level}",
            "text:style-name": style_name,
        } },
    )


def p(
    *,
    style_name: str | None = None,
    **kwargs,
) -> Element:
    return create_element(
        tag="text:p",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "text:style-name": style_name,
        } },
    )


def tab(
    **kwargs,
) -> Element:
    return create_element(
        tag="text:tab",
        **kwargs,
    )


def span(
    *,
    style_name: str | None = None,
    **kwargs,
) -> Element:
    return create_element(
        tag="text:span",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "text:style-name": style_name,
        } },
    )


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


def table(
    *,
    name: str,
    style_name: str | None = None,
    **kwargs,
) -> Element:
    return create_element(
        tag="table:table",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "table:style-name": style_name,
            "table:name": name,
        } },
    )


def emphasis(
    *,
    style_name: str | None = None,
    **kwargs,
) -> Element:
    return create_element(
        tag="text:emphasis",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "text:style-name": style_name,
        } },
    )


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


def table_row(
    **kwargs,
) -> Element:
    return create_element(
        tag="table:table-row",
        **kwargs,
    )


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


def covered_table_cell(
    **kwargs,
) -> Element:
    return create_element(
        tag="table:covered-table-cell",
        **kwargs,
    )


def list_(
    **kwargs,
) -> Element:
    return create_element(
        tag="text:list",
        **kwargs,
    )


def list_item(
    **kwargs,
) -> Element:
    return create_element(
        tag="text:list-item",
        **kwargs,
    )