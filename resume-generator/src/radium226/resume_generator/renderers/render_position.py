from lxml.etree import Element
from pendulum import today

from ..models import Position
from ..open_document import text

from .render_roles import render_roles
from .render_tools import render_tools
from .render_paragraph import render_paragraph


def render_position(position: Position, position_index) -> list[Element]:
    period_from = position.period.start.format("MMMM YYYY", locale="fr")
    period_to = "aujourd'hui" if position.period.end == today().at(0).set(day=1) else position.period.end.format("MMMM YYYY", locale="fr")

    return (
        [
            text.h(
                style_name="First_20_Position" if position_index == 0 else "Following_20_Positions",
                outline_level=3,
                children=(
                    [text.span(children=[position.title])] + 
                    [text.tab()] + 
                    ([text.span(children=[position.client.name])] if position.client else []) +
                    [text.tab()] + 
                    ([text.span(children=[position.project])] if position.project else [])
                ),
            ),
        ] + 
        (render_paragraph(context, style_name="Context_20_of_20_Position") if (context := position.context) else []) +
        [
            text.p(
                style_name="Période",
                children=[
                    text.span(
                        children=[f"De {period_from} à {period_to}"],
                    ), 
                    " ",
                    text.span(
                        style_name="Durée_20_du_20_projet",
                        children=["(" + position.period.start.diff_for_humans(position.period.end, absolute=True, locale="fr") + ")"],
                    ), 
                ]
            ),
            text.table(
                name="Tableau",
                style_name="Tableau1",
                children=[
                    text.table_column(
                        style_name="Tableau1.A",
                        number_columns_repeated=2,
                    ),
                    text.table_row(
                        children=[
                            text.table_cell(
                                number_columns_spanned=2,
                                children=render_paragraph(position.description, style_name="Présentation_20_du_20_projet"),
                            ),
                            text.covered_table_cell(),
                        ]
                    ),
                    text.table_row(
                        style_name="Tableau1.2",
                        children=[
                            text.table_cell(
                                style_name="Tableau1.A2",
                                children=render_roles(position.roles),
                            ),
                            text.table_cell(
                                style_name="Tableau1.B2",
                                children=render_tools(position.technical_stack),
                            ),
                        ],
                    ),
                ],
            ),
        ]
    )