from ..models import Resume

from .parse_job import parse_job
from .parse_publication import parse_publication


def parse_resume(obj: dict) -> Resume:
    jobs = [parse_job(job) for job in obj.get("jobs", [])]
    publications = [parse_publication(publication) for publication in obj.get("publications", [])]
    return Resume(
        jobs=jobs,
        publications=publications,
    )