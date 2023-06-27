from typing import NewType
from dataclasses import dataclass


SkillTitle = NewType("SkillTitle", str)


SkillCategory = NewType("SkillCategory", str)


SkillRating = NewType("SkillRating", int)


@dataclass
class Skill():

    title: SkillTitle

    category: SkillCategory

    rating: SkillRating