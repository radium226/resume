from lxml.etree import Element

from ..models import Role
from ..open_document import text

from .render_paragraph import render_paragraph


def render_roles(roles: list[Role]) -> Element:
    def render_role(role: Role):
        if len(role.details) > 0:
            return render_paragraph(role.description)
        else:
            return text.list_item(
                children=[
                    render_paragraph(role.description),
                    render_roles(role.details),
                ]
            )

    return text.list(
        children=[render_role(role) for role in roles],
    )