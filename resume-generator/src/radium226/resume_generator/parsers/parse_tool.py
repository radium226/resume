from ..models import Tool, ToolName

from .parse_paragraph import parse_paragraph


def parse_tool(tool_obj) -> Tool:
    match tool_obj:
        case str():
            name = ToolName(parse_paragraph(tool_obj))
            return Tool(
                name=name,
            )
        case dict():
            name = ToolName(parse_paragraph(tool_obj["name"]))
            details = [parse_tool(detail_obj) for detail_obj in tool_obj.get("details", [])]
            return Tool(
                name=name,
                details=details,
            )