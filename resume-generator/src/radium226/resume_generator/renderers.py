from lxml.etree import Element, SubElement, parse, register_namespace
from typing import Union, Optional
from mistletoe.block_token import Paragraph
from mistletoe.span_token import RawText, Emphasis, SpanToken
from pendulum import today

from .models import *
from .xml import *
from .open_document import *


def render_span_token(span_token: SpanToken) -> Union[Element, str]:
    match span_token:
        case RawText():
            return span_token.content

        case Emphasis():
            return emphasis(
                children=[
                    render_span_token(child) for child in span_token.children
                ],
            )


def render_paragraph(paragraph: Paragraph) -> Element:
    return p(
        children=[
            render_span_token(child) for child in paragraph.children
        ],
    )


def render_tasks(tasks: list[Task]) -> Element:
    def render_task(parent_element: Element, task: Task):
        match task:
            case ComplexTask(description, tasks):
                append_children_to_parent_element(parent_element, [render_paragraph(description), render_tasks(tasks)])

            case Paragraph():
                description = task
                append_children_to_parent_element(parent_element, [render_paragraph(description)])

    list_element = create_element(tag="text:list")
    for task in tasks:
        list_item_element = create_element("text:list-item")
        list_element.append(list_item_element)
        render_task(list_item_element, task)
    return list_element


def render_tool(tool: Tool) -> list[Element]:
    match tool:
        case str():
            return [p(children=[tool])]

        case ComplexTool(name, tools):
            return [p(children=[name]), render_tools(tools)]


def render_tools(tools: list[Tool]) -> Element:
    return list_(children=[list_item(children=render_tool(tool)) for tool in tools])


def render_position(position: Position, position_index=0) -> Element:
    period_from = position.period.start.format("MMMM YYYY", locale="fr")
    period_to = "aujourd'hui" if position.period.end == today().at(0).set(day=1) else position.period.end.format("MMMM YYYY", locale="fr")
    
    return section(
        name=f"Section{position_index}",
        children=[
            h(
                outline_level=3,
                children=[position.name],
            ),
            p(
                children=[
                    span(
                        children=[f"De {period_from} à {period_to}"],
                    )
                ]
            ),
            table(
                name=f"Tableau{position_index}",
                children=[
                    table_column(
                        number_columns_repeated=2,
                    ),
                    table_row(
                        children=[
                            table_cell(
                                number_columns_spanned=2,
                                children=[
                                    render_paragraph(position.description)
                                ],
                            ),
                            covered_table_cell(),
                        ]
                    ),
                    table_row(
                        children=[
                            table_cell(
                                children=[render_tasks(position.tasks)],
                            ),
                            table_cell(
                                children=[render_tools(position.tools)],
                            ),
                        ],
                    ),
                ],
            ),
        ],
    )


def render_experience(experience: Experience) -> Element:
    return section(
        name=experience.company.name,
        children=[
            h(
                outline_level=2,
                children=[
                    experience.company.name,
                    tab(),
                    experience.company.website,
                ],
            ),
        ] + [
            render_position(position) for position in experience.positions
        ],
    )


def render_resume(resume: Resume) -> Element:
    # empty = parse(str(Path(__file__).parent / "empty.fodt"))
    empty = parse(str(Path(__file__).parent.parent.parent.parent.parent / "CV.fodt"))
    body = next(iter(empty.xpath("//table:table-cell[@table:style-name='Tableau6.B2']", namespaces=NAMESPACES_BY_PREFIX)), None)
    section_element = section(
        name="Experience_professionnelle",
        children=[
            h(
                outline_level=1,
                children=["Expérience professionnelle"],
            ),
        ] + [
            render_experience(experience) for experience in resume.experiences
        ],
    )
    
    
    body.append(section_element)

    return empty