from lxml.etree import Element
from typing import Union
from mistletoe.block_token import Paragraph
from mistletoe.span_token import RawText, Emphasis, SpanToken

from .models import Task



"""
   <text:list text:style-name="L1">
    <text:list-item>
     <text:p text:style-name="P1">Coucou <text:span text:style-name="Strong_20_Emphasis">les</text:span> amis</text:p>
     <text:list>
      <text:list-item>
       <text:p text:style-name="P1">Je suis là</text:p>
      </text:list-item>
     </text:list>
    </text:list-item>
   </text:list>
"""

def append_to_element(parent_element: Element, child_element_or_text: Union[Element, str]) -> None:
    if isinstance(child_element_or_text, str):
        parent_element.tail = child_element_or_text

    else:
        parent_element.append(child_element_or_text)


def render_span_token(span_token: SpanToken) -> Union[Element, str]:
    match span_token:
        case RawText():
            content = span_token.content
            return content

        case Emphasis():
            element = Element("emphasis")
            for child in span_token.children:
                if child:    
                    append_to_element(element, render_span_token(child))
            return element

def render_paragraph(paragraph: Paragraph) -> Element:
    element = Element("p")
    last_element = element
    for child in paragraph.children:
        if child:
            append_to_element(element, render_span_token(child))
    return element



def render_task(task: Task) -> Element:
    pass