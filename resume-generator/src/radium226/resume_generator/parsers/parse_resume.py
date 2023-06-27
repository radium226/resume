from ..models import Resume

from .parse_job import parse_job
from .parse_publication import parse_publication
from .parse_skill import parse_skill
from .parse_profile import parse_profile
from .parse_contact import parse_contact


def parse_resume(obj: dict) -> Resume:
    jobs = [parse_job(job) for job in obj.get("jobs", [])]
    publications = [parse_publication(publication) for publication in obj.get("publications", [])]
    skills = [parse_skill(skill_obj) for skill_obj in obj.get("skills", [])]
    profile = parse_profile(obj["profile"])
    contacts = [parse_contact(contact_obj) for contact_obj in obj.get("contacts", [])]
    return Resume(
        jobs=jobs,
        publications=publications,
        skills=skills,
        profile=profile,
        contacts=contacts,
    )