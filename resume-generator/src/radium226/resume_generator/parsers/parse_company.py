from ..models import Company, CompanyName, CompanyWebsite

def parse_company(obj: str | dict[str, str]) -> Company:
    match obj:
        case str():
            return Company(
                name=CompanyName(obj),
                website=None,
            )

        case dict():
            return Company(
                name=CompanyName(obj["name"]),
                website=CompanyWebsite(website) if (website := obj.get("website", None)) else None,
            )