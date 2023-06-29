from lxml.etree import _Element

from ...xml import create_element


def table_cell_properties(
    *,
    column_width: str | None = None,
    rel_column_width: str | None = None,
    **kwargs,
) -> _Element:
    return create_element(
        tag="table:table",
        **kwargs | { "attributes": kwargs.get("attributes", {}) | { 
            "style:column-width": column_width,
            "style:rel-column-width": rel_column_width,
        } },
    )