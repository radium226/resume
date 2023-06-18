from dataclasses import dataclass, field

from .company import Company
from .context import Context
from .position import Position


@dataclass
class Job():

    employer: Company
    context: Context | None = None
    positions: list[Position] = field(default_factory=list)
