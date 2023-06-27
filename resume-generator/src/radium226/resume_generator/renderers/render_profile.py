from lxml.etree import Element

from ..models import Profile
from ..open_document import text

from .render_paragraph import render_paragraph


def render_profile(profile: Profile) -> list[Element]:
    return (
        [
            text.h(
                outline_level=1,
                children=["Profil"],
            )
        ] + 
        [
            element
            for paragraph in profile.paragraphs
            for element in render_paragraph(paragraph, style_name="Profile")
        ]
    )