from lxml.etree import Element

from ..models import Role
from ..open_document import text

from .render_paragraph import render_paragraph


def render_roles(roles: list[Role], level: int = 1) -> list[Element]:
    def render_role(role: Role) -> list[Element]:
        if len(role.details) == 0:
            return [
                text.list_item(
                    children=render_paragraph(role.description, style_name=f"List_20_{level}_20_Cont."),
                ),
            ]
        else:
            return [
                text.list_item(
                    children=render_paragraph(role.description, style_name=f"List_20_{level}_20_Cont.") + render_roles(role.details, level=level + 1),
                ),
            ]

    return [
        text.list(
            style_name=f"List_20_1",
            children=[element for role in roles for element in render_role(role)],
        ),
    ]