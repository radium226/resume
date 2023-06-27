from ..models import Skill, SkillTitle, SkillRating, SkillCategory


def parse_skill(obj: dict) -> Skill:
    return Skill(
        title=SkillTitle(obj["title"]),
        category=SkillCategory(obj["category"]),
        rating=SkillRating(obj["rating"]),
    )