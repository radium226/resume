from lxml.etree import Element

from ..models import Tool 
from ..open_document import text

from .render_paragraph import render_paragraph


def render_tools(tools: list[Tool]) -> Element:
    def render_tool(tool: Tool) -> Element:
        if len(role.details) > 0:
            return render_paragraph(tool.description)
        else:
            return text.list_item(
                children=[
                    render_paragraph(tool.name),
                    render_roles(tool.name),
                ]
            )
    
    return text.list(
        children=[render_tool(tool) for tool in tools],
    )
