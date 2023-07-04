from lxml.etree import _Element

from ..models import Tool 
from ..open_document import text

from .render_paragraph import render_paragraph


def render_tools(tools: list[Tool], level: int = 1) -> list[_Element]:
    def render_tool(tool: Tool, index: int, length: int) -> list[_Element]:

        style_name_suffix = "Cont."
        # if index == 0:
        #     style_name_suffix = "Start"
        # elif index == length - 1:
        #     style_name_suffix = "End"

        if len(tool.details) == 0:
            return [
                text.list_item(
                    children=render_paragraph(tool.name, style_name=f"List_20_{level}_20_{style_name_suffix}"),
                )
            ]
        else:
            return [
                text.list_item(
                    children=render_paragraph(tool.name, style_name=f"List_20_{level}_20_{style_name_suffix}") + render_tools(tool.details, level=level + 1),
                ),
            ]
    
    return [
        text.list(
            style_name="List_20_1",
            children=[element for index, tool in enumerate(tools) for element in render_tool(tool, index, len(tools))],
        ),
    ]
