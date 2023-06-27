from dataclasses import dataclass
from lxml.etree import Element
from itertools import groupby
from copy import deepcopy

from ..models import Skill, SkillCategory, SkillRating
from ..open_document import text

from .render_paragraph import render_paragraph


@dataclass
class CategoryAndSkills():

    category: SkillCategory
    skills: list[Skill]


def render_rating(rating: SkillRating) -> list[Element]:
    def filled_square_element() -> Element:
        return text.frame(
            width="0.0591in",
            height="0.0591in",
            style_name="fr1",
            children=[
                text.image(
                    href="Pictures/1000067500003505000035051046D2E1734B0441.svg",
                    mime_type="image/svg+xml",
                ),
            ]
        )

    def empty_square_element() -> Element:
        return text.frame(
            width="0.0591in",
            height="0.0591in",
            style_name="fr1",
            children=[
                text.image(
                    href="Pictures/100000FF0000350500003505CAD4341EDB328597.svg",
                    mime_type="image/svg+xml",
                ),
            ]
        )

    max_rating = 3

    return [
        text.p(
            children=(
                [
                    element
                    for i in range(1, max_rating + 1)
                    for element in [filled_square_element() if i <= rating else empty_square_element(), text.s()]
                ][:-1]
            ),
        ),
    ]



def render_category_and_skills_to_table_rows(category_and_skills: CategoryAndSkills) -> list[Element]:
    return [
        text.table_row(
            children=[
                text.table_cell(number_rows_spanned=len(category_and_skills.skills), children=[text.h(outline_level=2, style_name="Category_20_of_20_Skill", children=[category_and_skills.category])]) if skill_index == 0 else text.covered_table_cell(),
                text.table_cell(children=[text.p(style_name="Title_20_of_20_Skill", children=[skill.title])]),
                text.table_cell(children=render_rating(skill.rating)),
            ],
        )
        for skill_index, skill in enumerate(category_and_skills.skills)
    ]


def render_skills(skills: list[Skill]) -> list[Element]:
    skills_by_category = list(
        map(
            lambda entry: CategoryAndSkills(category=entry[0], skills=list(entry[1])),
            groupby(
                skills,
                key=lambda skill: skill.category,
            ),
        )
    )

    return [
        text.h(outline_level=1, children=["Compétences"]),
        text.table(
            name="Compétences",
            children=(
                [
                    text.table_column(),
                    text.table_column(),
                    text.table_column(),
                ] + 
                [
                    element 
                    for category_and_skills in skills_by_category
                    for element in render_category_and_skills_to_table_rows(category_and_skills) 
                ]
            ),
        ),
    ]