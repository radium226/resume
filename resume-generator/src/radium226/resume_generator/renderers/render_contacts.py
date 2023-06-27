from dataclasses import dataclass
from lxml.etree import Element
from itertools import groupby
from copy import deepcopy
from pathlib import Path

from ..models import Contact, ContactType
from ..open_document import text
from .context import get_current_render_context


def _render_contact_as_table_row(contact: Contact) -> Element:
    return text.table_row(
        children=[
            text.table_cell(
                children=[
                    text.p(
                        children=[
                            get_current_render_context().embedded_image(
                                width="0.33cm",
                                height="0.33cm",
                                file_path=Path(__file__).parent.parent / "data" / f"{contact.type}.png",
                            )
                        ],
                    )
                ],
            ),
            text.table_cell(
                children=[
                    text.p(
                        children=[contact.value],
                    )
                ],
            ),
        ],
    )


def render_contacts(contacts: list[Contact]) -> list[Element]:
    return [
        text.h(outline_level=1, children=["Contacts"]),
        text.table(
            name="Compétences",
            children=(
                [
                    text.table_column(),
                    text.table_column(),
                ] + 
                [
                    _render_contact_as_table_row(contact) 
                    for contact in contacts 
                ]
            ),
        ),
    ]