from lxml.etree import Element

from ..models import Job
from ..open_document import text

from .render_position import render_position


def render_job(job: Job) -> list[Element]:
    return [
        text.h(
            outline_level=2,
            children=[
                job.employer.name,
                text.tab(),
                text.span(
                    children=[
                        f"{job.employer.website}",
                    ],
                ),
            ],
        ),
        *[element for position in job.positions for element in render_position(position)]
    ]