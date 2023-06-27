from dataclasses import dataclass, field

from .job import Job
from .publication import Publication
from .skill import Skill


@dataclass
class Resume():

    jobs: list[Job] = field(default_factory=list)

    skills: list[Skill] = field(default_factory=list)

    publications: list[Publication] = field(default_factory=list)
