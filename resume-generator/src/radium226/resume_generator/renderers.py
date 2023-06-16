from lxml.etree import Element, SubElement, parse, register_namespace
from typing import Union, Optional
from mistletoe.block_token import Paragraph
from mistletoe.span_token import RawText, Emphasis, SpanToken

from .models import *
from .xml import *
from .open_document import *


def render_span_token(span_token: SpanToken) -> Union[Element, str]:
    match span_token:
        case RawText():
            return span_token.content

        case Emphasis():
            return create_element(
                tag="text:emphasis", 
                attributes={
                    "text:style_name": "Strong_20_Emphasis",
                },
                children=[
                    render_span_token(child) for child in span_token.children
                ],
            )


def render_paragraph(paragraph: Paragraph) -> Element:
    return create_element(
        tag="text:p", 
        attributes={
            "text:style-name": "P1",
        },
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


def render_position(position: Position, position_index=0) -> Element:
    section(
        name=f"Section{position_index}",
        children=[
            heading(
                outline_level=3,
                parent=section_element,
                children=[position.name],
            ),
            table(
                name=f"Tableau{position_index}"
            )
        ],
    )

    section_element = create_element(
        tag="text:section",
        attributes={
            "text:style-name": "Sect1",
            "text:name": f"Section{position_index}",
        },
    )

    heading_element = 
     
    table_element = create_element(
        parent=section_element,
        tag="table:table",
        attributes={
            "table:style-name": "Tableau1",
            "table:name": f"Tableau{position_index}"
        },
    )

    table_column_element = create_element(
        parent=table_element,
        tag="table:table-column",
        attributes={
            "table:number-columns-repeated": "2",
            "table:style-name": "Tableau1.A",
        },
    )
    
    table_row_element = create_element(
        parent=table_element,
        tag="table:table-row"
    )

    table_cell_element = create_element(
        parent=table_row_element,
        tag="table:table-cell",
        attributes={
            "table:number-columns-spanned": "2",
            "table:style-name": "Tableau1.A1",
        },
        children=[render_paragraph(position.description)]
    )

    covered_table_cell_element = create_element(
        parent=table_row_element,
        tag="table:covered-table-cell",
    )

    table_row_element = create_element(
        parent=table_element,
        tag="table:table-row",
        children=[
            create_element(
                tag="table:table-cell",
                attributes={
                    "table:style-name": "Tableau1.A2"
                },
                children=[render_tasks(position.tasks)]
            ),
            create_element(
                tag="table:table-cell",
                attributes={
                    "table:style-name": "Tableau1.B2",
                }
            )
        ],
    )

    return section_element


def render_resume(resume: Resume) -> Element:
    empty = parse(str(Path(__file__).parent / "empty.fodt"))
    body = next(iter(empty.xpath("//office:body", namespaces=NAMESPACES_BY_PREFIX)), None)
    i = 1
    for experience in resume.experiences:
        for position in experience.positions:
            body.append(render_position(position, i))
            i += 1

    return empty