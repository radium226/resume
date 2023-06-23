from lxml.etree import Element

from ..models import Tool 
from ..open_document import text

from .render_paragraph import render_paragraph


def render_tools(tools: list[Tool]) -> list[Element]:
    def render_tool(tool: Tool) -> list[Element]:
        if len(tool.details) == 0:
            return [
                text.list_item(
                    children=render_paragraph(tool.name),
                )
            ]
        else:
            return [
                text.list_item(
                    children=render_paragraph(tool.name) + render_tools(tool.details),
                ),
            ]
    
    return [
        text.list(
            children=[element for tool in tools for element in render_tool(tool)],
        ),
    ]
