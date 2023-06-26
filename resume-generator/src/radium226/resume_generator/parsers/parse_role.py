from ..models import Role, RoleDescription

from .parse_paragraph import parse_paragraph


def parse_role(role_obj) -> Role:
    match role_obj:
        case str():
            description = RoleDescription(parse_paragraph(role_obj))
            return Role(
                description=description,
            )
        case dict():
            description = RoleDescription(parse_paragraph(role_obj["description"]))
            details = [parse_role(detail_obj) for detail_obj in role_obj.get("details", [])]
            return Role(
                description=description,
                details=details,
            )