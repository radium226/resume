from ..models import Tool, ToolName

from .parse_paragraph import parse_paragraph


def parse_tool(tool_obj_or_str: str | dict) -> Tool:
    match tool_obj_or_str:
        case str():
            tool_str = tool_obj_or_str
            name = ToolName(parse_paragraph(tool_str))
            return Tool(
                name=name,
            )
        case dict():
            tool_obj = tool_obj_or_str
            name = ToolName(parse_paragraph(tool_obj["name"]))
            details = [parse_tool(detail_obj) for detail_obj in tool_obj.get("details", [])]
            return Tool(
                name=name,
                details=details,
            )