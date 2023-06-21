from lxml.etree import Element

from ...xml import create_element


def table_row(
    **kwargs,
) -> Element:
    return create_element(
        tag="table:table-row",
        **kwargs,
    )