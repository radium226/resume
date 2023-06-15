from lxml.etree import Element, SubElement, parse, register_namespace
from typing import Union
from mistletoe.block_token import Paragraph
from mistletoe.span_token import RawText, Emphasis, SpanToken

from .models import *
from .append_child_nodes_to_parent_element import append_child_nodes_to_parent_element


XMLNS_TABLE = "urn:oasis:names:tc:opendocument:xmlns:table:1.0"
XMLNS_TEXT = "urn:oasis:names:tc:opendocument:xmlns:text:1.0"
XMLNS_OFFICE = "urn:oasis:names:tc:opendocument:xmlns:office:1.0"


def attrib(element: Element, namespace: str, name: str, value):
    element.attrib["{" + namespace + "}" + name] = value

def append_to_element(parent_element: Element, child_element_or_text: Union[Element, str]) -> None:
    if isinstance(child_element_or_text, str):
        parent_element.tail = child_element_or_text

    else:
        parent_element.append(child_element_or_text)


def render_span_token(span_token: SpanToken) -> Union[Element, str]:
    print(f"span_token={span_token}")
    match span_token:
        case RawText():
            content = span_token.content
            return content

        case Emphasis():
            element = Element("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}emphasis")
            element.attrib["{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name"] = "Strong_20_Emphasis"
            for child in span_token.children:
                if child:    
                    append_to_element(element, render_span_token(child))
            return element

def render_paragraph(paragraph: Paragraph) -> Element:
    element = Element("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}p")
    element.attrib["{urn:oasis:names:tc:opendocument:xmlns:text:1.0}style-name"] = "P1"
    append_child_nodes_to_parent_element(element, [render_span_token(child) for child in paragraph.children])
    return element


def render_tasks(tasks: list[Task]) -> Element:
    def render_task(parent_element: Element, task: Task):
        match task:
            case ComplexTask(description, tasks):
                append_child_nodes_to_parent_element(parent_element, [render_paragraph(description), render_tasks(tasks)])

            case Paragraph():
                description = task
                append_child_nodes_to_parent_element(parent_element, [render_paragraph(description)])


    ul = Element("{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list")
    for task in tasks:
        li = SubElement(ul, "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}list-item")
        render_task(li, task)
    return ul


def render_position(position: Position) -> Element:
    section = Element("{" + XMLNS_TEXT + "}section")
    
    h = SubElement(section, "{" + XMLNS_TEXT + "}h")
    attrib(h, XMLNS_TEXT, "outline-level", "3")
    h.text = position.name

    table = SubElement(section, "{" + XMLNS_TABLE + "}table")
    table_column = SubElement(table, "{" + XMLNS_TABLE + "}table-column")
    attrib(table_column, XMLNS_TABLE, "number-columns-repeated", "2")
    table_row = SubElement(table_column, "{" + XMLNS_TABLE + "}table-row")
    table_cell = SubElement(table_row, "{" + XMLNS_TABLE + "}table-cell")
    attrib(table_cell, XMLNS_TABLE, "number-columns-spanned", "2")
    table_cell.append(render_paragraph(position.description))
    covered_table_cell = SubElement(table_row, "{" + XMLNS_TABLE + "}covered-table-cell")
    table_row = SubElement(table_column, "{" + XMLNS_TABLE + "}table-row")
    table_cell = SubElement(table_row, "{" + XMLNS_TABLE + "}table-cell")
    table_cell.append(render_tasks(position.tasks))
    table_cell = SubElement(table_row, "{" + XMLNS_TABLE + "}table-cell")
    
    return section


def render_resume(resume: Resume) -> Element:
    empty = parse(str(Path(__file__).parent / "empty.fodt"))
    body = next(iter(empty.xpath("//office:body", namespaces={
        "office": XMLNS_OFFICE,
    })), None)

    for experience in resume.experiences:
        for position in experience.positions:
            body.append(render_position(position))

    return empty