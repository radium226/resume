from lxml.etree import _Element

from ...xml import create_element


def covered_table_cell(
    **kwargs,
) -> _Element:
    return create_element(
        tag="table:covered-table-cell",
        **kwargs,
    )
