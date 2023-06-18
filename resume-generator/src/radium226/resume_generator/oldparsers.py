from ruamel.yaml import YAML
from pathlib import Path
from io import StringIO, BufferedReader

from mistletoe import markdown
from mistletoe.block_token import Paragraph, Document, tokenize

from pendulum import parse

from .models import *


# def parse_file(file_path: Path) -> Resume:
#     yaml = YAML()
#     obj = yaml.load(file_path)
#     return parse_resume(obj)



def parse_resume(obj: dict) -> Resume:
    experiences = [parse_experience(experience_obj) for experience_obj in obj["experiences"]]
    return Resume(
        experiences=experiences,
    )


def parse_experience(obj: dict) -> Experience:
    positions = [parse_position(position_obj) for position_obj in obj["positions"]]
    return Experience(
        company=Company(
            name=obj["company"]["name"],
            website=obj["company"]["website"],
        ),
        positions=positions,
    )


def parse_position(obj: dict) -> Position:
    name = obj["name"]

    period_from = parse(obj["period"]["from"]).at(0).set(day=1)
    period_to = (parse(text, format="YYYY[-]MM") if (text := obj["period"].get("to", None)) else today()).at(0).set(day=1)

    period = period_to - period_from


    client = Client(text) if (text := obj.get("client", None)) else None
    project = Project(project) if (text := obj.get("client", None)) else None

    tools = [parse_tool(tool_obj) for tool_obj in obj_tools] if (obj_tools := obj.get("tools", None)) else []


    description = Description(parse_paragraph(description_text)) if (description_text := obj.get("description", None)) else None
    tasks = [parse_task(task_obj) for task_obj in obj["tasks"]]
    return Position(
        name=name,
        period=period,
        description=description,
        tasks=tasks,
        client=client,
        project=project,
        tools=tools,
    )


def parse_tool(obj_or_text: dict | str) -> Tool:
    match obj_or_text:
        case str():
            text = obj_or_text
            return SimpleTool(text)

        case dict():
            obj = obj_or_text
            name = obj["name"]
            tools = [parse_tool(tool_obj) for tool_obj in obj["tools"]]
            return ComplexTool(
                name=name,
                tools=tools,
            )



def parse_task(obj_or_text: dict | str) -> Task:
    match obj_or_text:
        case str():
            text = obj_or_text
            return SimpleTask(parse_paragraph(text))

        case dict():
            obj = obj_or_text
            description = Description(parse_paragraph(obj["description"]))
            tasks = [parse_task(task_obj) for task_obj in obj["tasks"]]
            return ComplexTask(
                description=description,
                tasks=tasks,
            )


def parse_paragraph(text: str) -> Paragraph:
    return Paragraph(text.splitlines(keepends=True))
