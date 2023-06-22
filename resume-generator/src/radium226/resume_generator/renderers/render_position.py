from lxml.etree import Element
from pendulum import today

from ..models import Position
from ..open_document import text

from .render_roles import render_roles
from .render_tools import render_tools
from .render_paragraph import render_paragraph


def render_position(position: Position, position_index=0) -> list[Element]:
    period_from = position.period.start.format("MMMM YYYY", locale="fr")
    period_to = "aujourd'hui" if position.period.end == today().at(0).set(day=1) else position.period.end.format("MMMM YYYY", locale="fr")

    return [
        text.h(
            outline_level=3,
            children=[position.title or "Coucou"],
        ),
        text.p(
            children=[
                text.span(
                    children=[f"De {period_from} à {period_to}"],
                )
            ]
        ),
        text.table(
            name=f"Tableau{position_index}",
            children=[
                text.table_column(
                    number_columns_repeated=2,
                ),
                text.table_row(
                    children=[
                        text.table_cell(
                            number_columns_spanned=2,
                            children=[
                                render_paragraph(position.description)
                            ],
                        ),
                        text.covered_table_cell(),
                    ]
                ),
                text.table_row(
                    children=[
                        text.table_cell(
                            children=[render_roles(position.roles)],
                        ),
                        text.table_cell(
                            children=[render_tools(position.technical_stack)],
                        ),
                    ],
                ),
            ],
        ),
    ]