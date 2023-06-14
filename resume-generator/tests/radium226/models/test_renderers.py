from pytest import fixture
from mistletoe.block_token import Paragraph

from radium226.resume_generator.models import *
from radium226.resume_generator.parsers import *
from radium226.resume_generator.renderers import *

from lxml.etree import tostring


@fixture
def paragraph() -> Paragraph:
    return parse_paragraph("Hello *how are you*?")


@fixture
def tasks() -> list[Task]:
    return [
        ComplexTask(parse_paragraph("FooBar"), [parse_paragraph("Foo"), parse_paragraph("Bar")]),
        parse_paragraph("BarFoo")
    ]


@fixture
def position(paragraph, tasks) -> Position:
    return Position(
        name="My PPosition",
        description=parse_paragraph("My *Position* description"),
        tasks=tasks,
    )

@fixture
def resume(position) -> Resume:
    return Resume(
        experiences=[Experience(positions=[position])]
    )


def test_render_paragraph(paragraph):
    element = render_paragraph(paragraph)
    print(tostring(element, encoding=str))


def test_render_tasks(tasks):
    element = render_tasks(tasks)
    print(tostring(element, encoding=str, pretty_print=True))

def test_render_position(position):
    element = render_position(position)
    print(tostring(element, encoding=str, pretty_print=True))

def test_render_resume(resume):
    element = render_resume(resume)
    print(tostring(element, encoding=str, pretty_print=True))