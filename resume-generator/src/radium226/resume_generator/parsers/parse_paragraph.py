from mistletoe.block_token import Paragraph


def parse_paragraph(obj: str) -> Paragraph:
    return Paragraph(obj.splitlines(keepends=True))