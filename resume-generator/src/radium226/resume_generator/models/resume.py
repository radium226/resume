from dataclasses import dataclass, field

from .job import Job
from .publication import Publication
from .skill import Skill
from .profile import Profile
from .contact import Contact


@dataclass
class Resume():

    profile: Profile

    jobs: list[Job] = field(default_factory=list)

    skills: list[Skill] = field(default_factory=list)

    publications: list[Publication] = field(default_factory=list)

    contacts: list[Contact] = field(default_factory=list) 
