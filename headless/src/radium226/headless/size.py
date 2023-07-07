from dataclasses import dataclass
from typing import TypeAlias


Width: TypeAlias = int


Height: TypeAlias = int


@dataclass
class Size():

    width: Width

    height: Height