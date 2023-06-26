from ..models import Context

from .parse_paragraph import parse_paragraph

def parse_context(obj: str) -> Context:
    paragraph = parse_paragraph(obj)
    return Context(paragraph)