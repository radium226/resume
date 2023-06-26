from dataclasses import dataclass, field
from pendulum import Period
from typing import NewType

from mistletoe.block_token import Paragraph

from .role import Role
from .context import Context
from .company import Company
from .tool import Tool


PositionTitle = NewType("PositionTitle", str)


PositionProject = NewType("PositionProject", str)


PositionDescription = NewType("PositionDescription", Paragraph)


@dataclass
class Position():

    title: PositionTitle
    description: PositionDescription
    period: Period
    context: Context | None = None
    client: Company | None = None
    project: PositionProject | None = None
    roles: list[Role] = field(default_factory=list)
    technical_stack: list[Tool] = field(default_factory=list)