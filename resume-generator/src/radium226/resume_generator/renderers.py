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


def render_position(position: Position, position_index=0) -> Element:
    section = Element("{" + XMLNS_TEXT + "}section")
    attrib(section, XMLNS_TEXT, "style-name", "Sect1")
    attrib(section, XMLNS_TEXT, "name", f"Section{position_index}")
    section.tail = "\n"
        
    h = SubElement(section, "{" + XMLNS_TEXT + "}h")
    attrib(h, XMLNS_TEXT, "outline-level", "3")
    h.text = position.name
    h.tail = "\n"

    table = SubElement(section, "{" + XMLNS_TABLE + "}table")
    attrib(table, XMLNS_TABLE, "style-name", "Tableau1")
    attrib(table, XMLNS_TABLE, "name", f"Tableau{position_index}")
    table.tail = "\n"
    
    table_column = SubElement(table, "{" + XMLNS_TABLE + "}table-column")
    attrib(table_column, XMLNS_TABLE, "number-columns-repeated", "2")
    attrib(table_column, XMLNS_TABLE, "style-name", "Tableau1.A")
    table_column.tail = "\n"
    
    table_row = SubElement(table, "{" + XMLNS_TABLE + "}table-row")
    table_row.tail = "\n"

    table_cell = SubElement(table_row, "{" + XMLNS_TABLE + "}table-cell")
    attrib(table_cell, XMLNS_TABLE, "number-columns-spanned", "2")
    attrib(table_cell, XMLNS_TABLE, "style-name", "Tableau1.A1")
    table_cell.tail = "\n"

    table_cell.append(render_paragraph(position.description))
    table_cell.tail = "\n"

    covered_table_cell = SubElement(table_row, "{" + XMLNS_TABLE + "}covered-table-cell")
    covered_table_cell.tail = "\n"

    table_row = SubElement(table, "{" + XMLNS_TABLE + "}table-row")
    table_row.tail = "\n"

    table_cell = SubElement(table_row, "{" + XMLNS_TABLE + "}table-cell")
    attrib(table_cell, XMLNS_TABLE, "style-name", "Tableau1.A2")
    table_cell.append(render_tasks(position.tasks))
    table_cell.tail = "\n"

    table_cell = SubElement(table_row, "{" + XMLNS_TABLE + "}table-cell")
    attrib(table_cell, XMLNS_TABLE, "style-name", "Tableau1.B2")
    table_cell.tail = "\n"

    return section


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