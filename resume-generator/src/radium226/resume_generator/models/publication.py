from typing import NewType
from dataclasses import dataclass, field
from pendulum import Date

from mistletoe.block_token import Paragraph

from .medium import Medium


PublicationTitle = NewType("PublicationTitle", Paragraph) # type: ignore


PublicationLink = NewType("PublicationLink", str)


@dataclass
class Publication():

    title: PublicationTitle | None = None
    
    medium: Medium | None = None

    link: PublicationLink | None = None

    date: Date | None = None

    details: list["Publication"] = field(default_factory=list)

