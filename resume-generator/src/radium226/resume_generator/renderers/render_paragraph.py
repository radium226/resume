from typing import Union
from lxml.etree import Element
from mistletoe.block_token import Paragraph
from mistletoe.span_token import RawText, Emphasis, SpanToken

from ..open_document import text


def render_span_token(span_token: SpanToken) -> Union[Element, str]:
    match span_token:
        case RawText():
            return span_token.content

        case Emphasis():
            return text.emphasis(
                children=[
                    render_span_token(child) for child in span_token.children
                ],
            )

    return text.emphasis(children=["FIXME"])


def render_paragraph(paragraph: Paragraph) -> Element:
    return text.p(
        children=[
            render_span_token(child) for child in paragraph.children
        ],
    )