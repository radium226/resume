from ..models import Resume

from .parse_job import parse_job
from .parse_publication import parse_publication
from .parse_skill import parse_skill


def parse_resume(obj: dict) -> Resume:
    jobs = [parse_job(job) for job in obj.get("jobs", [])]
    publications = [parse_publication(publication) for publication in obj.get("publications", [])]
    skills = [parse_skill(skill_obj) for skill_obj in obj.get("skills", [])]
    return Resume(
        jobs=jobs,
        publications=publications,
        skills=skills,
    )