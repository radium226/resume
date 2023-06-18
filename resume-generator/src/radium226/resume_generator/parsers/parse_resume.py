from ..models import Resume

from .parse_job import parse_job


def parse_resume(obj: dict) -> Resume:
    jobs = [parse_job(job) for job in obj.get("jobs", [])]
    return Resume(
        jobs=jobs,
    )