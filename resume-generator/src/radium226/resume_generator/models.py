from typing import NewType, TypeAlias
from pathlib import Path
from ruamel.yaml import YAML
from dataclasses import dataclass, field
from mistletoe.block_token import Paragraph


Description = NewType("Description", Paragraph)


SimpleTask = NewType("SimpleTask", Paragraph)


@dataclass
class ComplexTask:

    description: Description | None = None
    tasks: list["Task"] = field(default_factory=list)


Task: TypeAlias = ComplexTask | SimpleTask


@dataclass
class Position:

    name: str
    description: Description
    tasks: list[Task] = field(default_factory=list)


@dataclass
class Experience:

    positions: list[Position] = field(default_factory=list)


@dataclass
class Resume:

    experiences: list[Experience] = field(default_factory=list)