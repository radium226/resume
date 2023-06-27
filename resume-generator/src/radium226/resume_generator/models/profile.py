from dataclasses import dataclass, field

from mistletoe.block_token import Paragraph


@dataclass
class Profile():
    paragraphs: list[Paragraph] = field(default_factory=list)