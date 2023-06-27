from typing import NewType
from dataclasses import dataclass
from enum import StrEnum, auto


class ContactType(StrEnum):

    PHONE = auto()

    GITHUB = auto()

    LINKEDIN = auto()

    EMAIL = auto()


ContactValue = NewType("ContactValue", str)


@dataclass
class Contact():

    type: ContactType

    value: ContactValue