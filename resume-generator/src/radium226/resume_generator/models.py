from typing import NewType, TypeAlias
from pathlib import Path
from ruamel.yaml import YAML
from dataclasses import dataclass, field
from mistletoe.block_token import Paragraph
from pendulum import Period


Description = NewType("Description", Paragraph)


SimpleTask = NewType("SimpleTask", Paragraph)


@dataclass
class ComplexTask:

    description: Description | None = None
    tasks: list["Task"] = field(default_factory=list)


Task: TypeAlias = ComplexTask | SimpleTask


ToolName: TypeAlias = str


SimpleTool = NewType("SimpleTool", ToolName)


@dataclass
class ComplexTool:

    name: ToolName | None = None
    tools: list["Tools"] = field(default_factory=list)


Tool: TypeAlias = SimpleTool | ComplexTool





@dataclass
class Client():

    name: str


@dataclass
class Project():

    name: str


@dataclass
class Position:

    name: str
    period: Period
    description: Description
    client: Client | None
    project: Project | None
    tasks: list[Task] = field(default_factory=list)
    tools: list[Tool] = field(default_factory=list)


@dataclass
class Company:

    name: str
    website: str


@dataclass
class Experience:

    company: Company
    positions: list[Position] = field(default_factory=list)


@dataclass
class Resume:

    experiences: list[Experience] = field(default_factory=list)
