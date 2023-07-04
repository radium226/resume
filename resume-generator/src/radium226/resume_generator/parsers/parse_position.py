from ..models import Position, PositionTitle, PositionDescription, PositionProject

from .parse_period import parse_period
from .parse_context import parse_context
from .parse_paragraph import parse_paragraph
from .parse_company import parse_company
from .parse_role import parse_role
from .parse_tool import parse_tool


def parse_position(position_obj: dict) -> Position:
    try:
        # title = PositionTitle(title_obj) if (title_obj := position_obj.get("title", None)) else None
        title = PositionTitle(position_obj["title"])
        description = PositionDescription(parse_paragraph(position_obj["description"]))
        client = parse_company(client_obj) if (client_obj := position_obj.get("client", None)) else None
        project = PositionProject(project_obj) if (project_obj := position_obj.get("project", None)) else None
        period = parse_period(position_obj["period"])
        context = parse_context(context_obj) if (context_obj := position_obj.get("context", None)) else None
        roles = [parse_role(role_obj) for role_obj in position_obj.get("roles", [])]
        technical_stack = [parse_tool(tool_obj) for tool_obj in position_obj.get("technical_stack", [])]
        return Position(
            title=title,
            description=description,
            period=period,
            client=client,
            project=project,
            context=context,
            roles=roles,
            technical_stack=technical_stack,
        )
    except Exception as e:
        print("Unable to parse")
        print(position_obj)
        raise e