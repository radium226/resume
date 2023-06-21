from lxml.etree import Element

from ..models import Job
from ..open_document import text

from .render_position import render_position


def render_job(job: Job) -> Element:
    return text.section(
        name=job.employer.name,
        children=[
            text.h(
                outline_level=2,
                style_name="Heading_20_2",
                children=[
                    job.employer.name,
                    text.tab(),
                    text.span(
                        style_name="Lien",
                        children=[
                            f"{job.employer.website}",
                        ],
                    ),
                ],
            ),
            *[render_position(position) for position in job.positions]
        ],
    )