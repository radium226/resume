from ..models import Contact, ContactType, ContactValue


def parse_contact(obj: dict) -> Contact:
    return Contact(
        type=ContactType(obj["type"]),
        value=ContactValue(obj["value"]),
    )