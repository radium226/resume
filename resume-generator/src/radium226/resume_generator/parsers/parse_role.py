from ..models import Role, RoleDescription

from .parse_paragraph import parse_paragraph


def parse_role(role_str_or_obj: str | dict) -> Role:
    match role_str_or_obj:
        case str():
            role_str = role_str_or_obj
            description = RoleDescription(parse_paragraph(role_str))
            return Role(
                description=description,
            )
        case dict():
            role_obj = role_str_or_obj
            description = RoleDescription(parse_paragraph(role_obj["description"]))
            details = [parse_role(detail_obj) for detail_obj in role_obj.get("details", [])]
            return Role(
                description=description,
                details=details,
            )