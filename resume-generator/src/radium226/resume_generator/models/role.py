from dataclasses import dataclass, field
from typing import NewType

from mistletoe.block_token import Paragraph

from .context import Context


RoleDescription = NewType("RoleDescription", Paragraph) # type: ignore


@dataclass
class Role():

    description: RoleDescription
    details: list["Role"] = field(default_factory=list)
