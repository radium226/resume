from typing import NewType
from dataclasses import dataclass, field

from mistletoe.block_token import Paragraph


ToolName = NewType("ToolName", Paragraph)


@dataclass
class Tool():

    name: ToolName
    details: list["Tool"] = field(default_factory=list)
