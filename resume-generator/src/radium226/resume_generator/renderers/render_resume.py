from lxml.etree import Element

from ..models import Resume
from ..open_document import text

from .render_job import render_job


def render_resume(resume: Resume) -> Element:
    return text.section(
        name="Experience_professionnelle",
        children=[
            text.h(
                outline_level=1,
                children=["Expérience professionnelle"],
            ),
            *[render_job(job) for job in resume.jobs]
        ]
    )