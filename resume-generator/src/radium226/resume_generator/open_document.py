from lxml.etree import Element
from .xml import *


def heading(
    *,
    outline_level: int,
    style_name: str | None,
    **kwargs,
) -> Element:
    return create_element(
        tag="text:h",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "text:outline-level": f"{outline_level}",
            "text:style-name": f"{style_name}",
        } },
    )


def paragraph(
    *,
    style_name: str | None,
    **kwargs,
) -> Element:
    return create_element(
        tag="text:p",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "text:style-name": f"{style_name}",
        } },
    )


def section(
    *,
    name: str,
    style_name: str | None,
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
    style_name: str | None,
    **kwargs,
) -> Element:
    return create_element(
        tag="table:table",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "table:style-name": style_name,
            "table:name": name,
        } },
    )


def table_row(
    **kwargs,
) -> Element:
    return create_element(
        tag="table:table-row",
    )


def table_cell(
    *,
    style_name: str,
    **kwargs,
) -> Element:
    return create_element(
        tag="table:table-cell",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "table:style-name": style_name,
        } },
    )