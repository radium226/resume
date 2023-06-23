from typing import Union
from lxml.etree import Element, tostring
from mistletoe.block_token import Paragraph
from mistletoe.span_token import RawText, Emphasis, SpanToken

from ..open_document import text


def render_span_token(span_token: SpanToken) -> list[Union[Element, str]]:
    match span_token:
        case RawText():
            return [
                span_token.content,
            ]

        case Emphasis():
            print(f"We are here! {span_token}")
            t = [
                text.span(
                    style_name="Strong_20_Emphasis",
                    children=[
                        element for child in span_token.children for element in render_span_token(child)
                    ],
                ),
            ]
            print(tostring(t[0]))
            return t

    return text.span(children=["FIXME"])


def render_paragraph(paragraph: Paragraph) -> list[Element]:
    return [
        text.p(
            children=[
                element for child in paragraph.children for element in render_span_token(child)
            ],
        )
    ]