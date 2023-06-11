from pytest import fixture
from mistletoe.block_token import Paragraph

from radium226.resume_generator.parser import parse_paragraph
from radium226.resume_generator.renderer import render_paragraph

from lxml.etree import tostring


@fixture
def paragraph() -> Paragraph:
    return parse_paragraph("Hello *how are you*?")


def test_render_paragraph(paragraph):
    element = render_paragraph(paragraph)
    print(tostring(element))
