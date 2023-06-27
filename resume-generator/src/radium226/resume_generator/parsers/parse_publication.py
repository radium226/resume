from pendulum import parse as parse, Period

from ..models import Publication, PublicationLink, PublicationTitle
from ..models import Medium, MediumName, MediumType

from .parse_medium import parse_medium
from .parse_paragraph import parse_paragraph


DATE_PARSE_FORMAT = "YYYY[-]MM[-]DD"


def parse_publication(obj: dict) -> Publication:
    title = PublicationTitle(parse_paragraph(title_str)) if (title_str := obj.get("title", None)) else None
    link = PublicationLink(link_str) if (link_str := obj.get("link", None)) else None
    medium = parse_medium(medium_obj) if (medium_obj := obj.get("medium", None)) else None
    details = [parse_publication(publication_obj) for publication_obj in obj.get("details", [])]

    date = parse(date_str.strip(), format=DATE_PARSE_FORMAT) if (date_str := obj.get("date", None)) else None

    return Publication(
        title=title,
        link=link,
        medium=medium,
        details=details,
        date=date,
    )