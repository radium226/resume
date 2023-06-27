from typing import NewType
from dataclasses import dataclass, field
from pendulum import Date

from mistletoe.block_token import Paragraph

from .medium import Medium


PublicationTitle = NewType("PublicationTitle", Paragraph)


PublicationLink = NewType("PublicationLink", str)


@dataclass
class Publication():

    title: PublicationTitle
    
    medium: Medium | None = None

    link: PublicationLink | None = None

    date: Date | None = None

    details: list["Publication"] = field(default_factory=list)

