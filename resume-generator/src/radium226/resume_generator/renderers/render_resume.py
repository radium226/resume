from lxml.etree import Element

from ..models import Resume
from ..open_document import text

from .render_job import render_job
from .render_publications import render_publications


def render_resume(
    resume: Resume
) -> list[Element]:
    return (
        [text.h(outline_level=1, children=["Expérience professionnelle"])] + 
        [element for job_index, job in enumerate(resume.jobs) for element in render_job(job, job_index)] +
        [text.h(outline_level=1, children=["Publications"])] + 
        render_publications(resume.publications)
    )
        