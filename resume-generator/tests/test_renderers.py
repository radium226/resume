from pytest import fixture
from pathlib import Path
from lxml.etree import _Element
from time import sleep

from radium226.headless import Session
from radium226.headless.app import LibreOffice

from radium226.resume_generator.xml import NAMESPACES_BY_PREFIX, append_children_to_parent_element

from radium226.resume_generator.parsers import parse_paragraph
from radium226.resume_generator.renderers import render_paragraph
from radium226.resume_generator.open_document import ODTFile


@fixture
def session(request):
    file_name = request.node.name + ".mp4"
    with Session() as session:
        video_file_path = Path(f"/tmp/test_renderers") / file_name
        video_file_path.parent.mkdir(parents=True, exist_ok=True)
        session.record_video(video_file_path)
        yield session


def test_render_paragraph(session):
    model_file_path = Path(__file__).parent / "data" / "empty.odt"
    output_file_path = Path("/tmp/test_renderers/test_render_paragraph.odt")
    
    def update_content(element):
        root_element = next(iter(element.xpath("/office:document-content/office:body/office:text", namespaces=NAMESPACES_BY_PREFIX)))
        for child in root_element.getchildren():
            root_element.remove(child)

        paragraph = parse_paragraph("I'm currently testing the rendering of *paragraphs*")
        
        append_children_to_parent_element(root_element, render_paragraph(paragraph))

        return []

    
    ODTFile.modify_with(
        input_file_path=model_file_path,
        output_file_path=output_file_path,
        update_content=update_content,
    )

    session.open_app(LibreOffice(output_file_path))
    sleep(5)