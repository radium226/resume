from click import command, argument, option
from pathlib import Path
from ruamel.yaml import YAML
from lxml.etree import tostring, Element
from functools import partial

from ..models import Resume
from ..parsers import parse_resume
from ..renderers import render_resume
from ..open_document import ODTFile
from ..xml import NAMESPACES_BY_PREFIX, append_children_to_parent_element


def render_resume_into_element(resume: Resume, element: Element) -> None:
    XPATH_QUERY = "//table:table[@table:name='Tableau6']/table:table-row[2]/table:table-cell[2]"
    body = next(iter(element.xpath(XPATH_QUERY, namespaces=NAMESPACES_BY_PREFIX)), None)
    for child in body.getchildren():
        body.remove(child)

    append_children_to_parent_element(body, render_resume(resume))


@command()
@option("--model", "model_file_path", type=Path, default=Path(__file__).parent.parent / "model.odt")
@argument("input_file_path", type=Path, metavar="INPUT", default="../data.yml")
@argument("output_file_path", type=Path, metavar="OUTPUT", default="/tmp/resume.odt")
def generate(model_file_path: Path, input_file_path: Path, output_file_path: Path):
    # Parsing resume
    yaml = YAML()
    yaml_obj = yaml.load(input_file_path)
    resume = parse_resume(yaml_obj)

    ODTFile.modify_with(
        input_file_path=model_file_path,
        output_file_path=output_file_path,
        update_content=partial(render_resume_into_element, resume=resume),
    )