from lxml.etree import Element

from ...xml import create_element


def covered_table_cell(
    **kwargs,
) -> Element:
    return create_element(
        tag="table:covered-table-cell",
        **kwargs,
    )
