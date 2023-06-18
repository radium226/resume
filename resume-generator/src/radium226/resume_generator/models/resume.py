from dataclasses import dataclass, field

from .job import Job


@dataclass
class Resume():

    jobs: list[Job] = field(default_factory=list)