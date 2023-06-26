from lxml.etree import Element

from ..models import Job
from ..open_document import text

from .render_position import render_position
from .render_paragraph import render_paragraph


def render_job(job: Job, job_index: int) -> list[Element]:
    return (
        [
            text.h(
                outline_level=2,
                style_name="Première_20_société" if job_index == 0 else "Sociétés_20_suivantes",
                children=
                    [text.span(children=[job.employer.name])] +
                    [text.tab()] + 
                    ([text.span(style_name="Lien", children=[website])] if (website := job.employer.website) else []),
            ),
        ] + 
        (render_paragraph(context, style_name="Présentation_20_de_20_l_27_entreprise") if (context := job.context) else []) +
        [
            element 
            for position_index, position in enumerate(job.positions) 
            for element in render_position(position, position_index)
        ]
    )