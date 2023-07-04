from typing import Union, Callable, Protocol
from lxml.etree import _Element, tostring
from mistletoe.block_token import Paragraph
from mistletoe.span_token import RawText, Emphasis, SpanToken

from ..open_document import text


def render_span_token(span_token: SpanToken) -> list[Union[_Element, str]]:
    match span_token:
        case RawText(): # type: ignore
            return [
                span_token.content,
            ]

        case Emphasis(): # type: ignore
            return [
                text.span(
                    style_name="Strong_20_Emphasis",
                    children=[
                        element for child in span_token.children for element in render_span_token(child)
                    ],
                ),
            ]

    return []


class CreateElementCallable(Protocol):

    def __call__(self, style_name: str | None, children: list[_Element | str]) -> _Element:
        pass


def render_paragraph(
    paragraph: Paragraph, 
    style_name: str | None = None, 
    create_element: CreateElementCallable = lambda style_name, children: text.p(style_name=style_name, children=children),
) -> list[_Element]:
    return [
        create_element(
            style_name=style_name,
            children=[
                element for child in paragraph.children for element in render_span_token(child)
            ],
        ),
    ]