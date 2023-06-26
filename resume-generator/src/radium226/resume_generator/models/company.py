from dataclasses import dataclass
from typing import NewType


CompanyName = NewType("CompanyName", str)


CompanyWebsite = NewType("CompanyWebsite", str)


@dataclass
class Company():

    name: CompanyName
    website: CompanyWebsite | None = None