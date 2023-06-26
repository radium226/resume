from ..models import Job

from .parse_company import parse_company
from .parse_context import parse_context
from .parse_position import parse_position


def parse_job(job_obj) -> Job:
    employer = parse_company(job_obj["employer"])
    context = parse_context(context_obj) if (context_obj := job_obj.get("context", None)) else None
    positions = [parse_position(position_obj) for position_obj in job_obj.get("positions", [])]
    return Job(
        employer=employer,
        context=context,
        positions=positions,
    )