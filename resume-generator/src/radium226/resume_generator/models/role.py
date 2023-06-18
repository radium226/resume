from dataclasses import dataclass, field
from typing import NewType

from mistletoe.block_token import Paragraph

from .context import Context


RoleDescription = NewType("RoleDescription", Paragraph)


@dataclass
class Role():

    description: RoleDescription
    context: Context | None = None
    details: list["Role"] = field(default_factory=list)
