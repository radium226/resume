from typing import NewType
from enum import StrEnum, auto
from dataclasses import dataclass


MediumName = NewType("MediumName", str)


class MediumType(StrEnum):

    ARTICLE = auto()

    TALK = auto()


@dataclass
class Medium():

    name: MediumName

    type: MediumType