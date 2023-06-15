from lxml.etree import Element, SubElement, parse, register_namespace
from typing import Union, Optional
from mistletoe.block_token import Paragraph
from mistletoe.span_token import RawText, Emphasis, SpanToken

from .models import *
from .append_child_nodes_to_parent_element import append_child_nodes_to_parent_element


XMLNS_TABLE = "urn:oasis:names:tc:opendocument:xmlns:table:1.0"
XMLNS_TEXT = "urn:oasis:names:tc:opendocument:xmlns:text:1.0"
XMLNS_OFFICE = "urn:oasis:names:tc:opendocument:xmlns:office:1.0"

NAMESPACES_BY_PREFIX = {
    "table": XMLNS_TABLE,
    "text": XMLNS_TEXT,
    "office": XMLNS_OFFICE,
}

def table()


def create_element(tag: str, attributes: dict[str, str] = {}, children: list[Union[Element, str]] = [], parent: Optional[Element] = None, text: str | None = None) -> Element:
    [namespace_prefix, local_tag] = tag.split(":")
    namespace = NAMESPACES_BY_PREFIX[namespace_prefix]
    element = Element(
        "{" + namespace + "}" + local_tag,
    )

    if parent is not None:
        parent.append(element)

    if text:
        element.text = text

    for attribute_name, attribute_value in attributes.items():
        set_attribute_to_element(element, attribute_name, attribute_value)

    append_child_nodes_to_parent_element(element, children)

    element.tail = "\n"

    return element

def set_attribute_to_element(element: Element, name: str, value: str):
    [namespace_prefix, local_name] = name.split(":")
    namespace = NAMESPACES_BY_PREFIX[namespace_prefix]
    element.attrib["{" + namespace + "}" + local_name] = value


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
                append_child_nodes_to_parent_element(parent_element, [render_paragraph(description), render_tasks(tasks)])

            case Paragraph():
                description = task
                append_child_nodes_to_parent_element(parent_element, [render_paragraph(description)])

    list_element = create_element(tag="text:list")
    for task in tasks:
        list_item_element = create_element("text:list-item")
        list_element.append(list_item_element)
        render_task(list_item_element, task)
    return list_element


def render_position(position: Position, position_index=0) -> Element:
    section_element = create_element(
        tag="text:section",
        attributes={
            "text:style-name": "Sect1",
            "text:name": f"Section{position_index}",
        },
    )

    heading_element = create_element(
        parent=section_element,
        tag="text:h",
        attributes={
            "text:outline-level": "3",
        },
        text=position.name,
    )
        
 
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
        tag="table:cell",
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
    body = next(iter(empty.xpath("//office:body", namespaces={
        "office": XMLNS_OFFICE,
    })), None)
    i = 1
    for experience in resume.experiences:
        for position in experience.positions:
            body.append(render_position(position, i))
            i += 1

    return empty