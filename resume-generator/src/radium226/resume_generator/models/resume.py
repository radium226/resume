from dataclasses import dataclass, field

from .job import Job
from .publication import Publication


@dataclass
class Resume():

    jobs: list[Job] = field(default_factory=list)

    publications: list[Publication] = field(default_factory=list)
