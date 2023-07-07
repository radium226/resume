from dataclasses import dataclass, field
from typing import TypeAlias

from .size import Size


DisplayNumber: TypeAlias = int


@dataclass
class Display():

    number: DisplayNumber = 9

    size: Size = field(default_factory=lambda: Size(1920, 1080))