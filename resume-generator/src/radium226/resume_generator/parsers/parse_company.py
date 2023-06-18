from ..models import Company

def parse_company(obj: str | dict[str, str]) -> Company:
    match obj:
        case str():
            return Company(
                name=obj,
                website=None,
            )

        case dict():
            return Company(
                name=obj["name"],
                website=obj.get("website", None),
            )