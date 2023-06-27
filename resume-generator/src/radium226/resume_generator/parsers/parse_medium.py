from ..models import Medium, MediumType, MediumName


def parse_medium(obj: dict) -> Medium:
    return Medium(
        name=MediumName(obj["name"]),
        type=MediumType(obj["type"]),
    )