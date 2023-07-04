from click import command, argument, option
from pathlib import Path
from ruamel.yaml import YAML
from lxml.etree import tostring, _Element
from functools import partial

from ..models import Resume
from ..parsers import parse_resume
from ..renderers import render_resume, render_skills, render_profile, render_contacts, init_current_render_context, get_current_render_context
from ..open_document import ODTFile, EmbeddedImage
from ..xml import NAMESPACES_BY_PREFIX, append_children_to_parent_element


def render_resume_into_element(resume: Resume, number_of_jobs: int, element: _Element) -> list[EmbeddedImage]:
    XPATH_QUERY_FOR_MAIN_CELL = "//table:table[@table:name='Tableau6']/table:table-row[2]/table:table-cell[2]"
    main_cell_element = next(iter(element.xpath(XPATH_QUERY_FOR_MAIN_CELL, namespaces=NAMESPACES_BY_PREFIX)))
    for child in main_cell_element.getchildren():
        main_cell_element.remove(child)

    XPATH_QUERY_FOR_LEFT_CELL = "//table:table[@table:name='Tableau6']/table:table-row[2]/table:table-cell[1]"
    left_cell_element = next(iter(element.xpath(XPATH_QUERY_FOR_LEFT_CELL, namespaces=NAMESPACES_BY_PREFIX)))
    for child in left_cell_element.getchildren():
        left_cell_element.remove(child)

    resume.jobs = list(resume.jobs[:number_of_jobs])
    init_current_render_context()
    
    append_children_to_parent_element(main_cell_element, list(render_resume(resume)))
    append_children_to_parent_element(
        left_cell_element,
        list( 
            render_contacts(resume.contacts) +
            render_profile(resume.profile) + 
            render_skills(resume.skills)
        ),
    )

    return get_current_render_context().embedded_images

    


@command()
@option("--model", "model_file_path", type=Path, default=Path(__file__).parent.parent / "model.odt")
@option("--number-of-jobs", "number_of_jobs", type=int, default=2)
@argument("input_file_path", type=Path, metavar="INPUT", default="../data.yml")
@argument("output_file_path", type=Path, metavar="OUTPUT", default="/tmp/resume.odt")
def generate(model_file_path: Path, number_of_jobs: int, input_file_path: Path, output_file_path: Path):
    # Parsing resume
    yaml = YAML()
    yaml.constructor.yaml_constructors[u'tag:yaml.org,2002:timestamp'] = yaml.constructor.yaml_constructors[u'tag:yaml.org,2002:str']
    yaml_obj = yaml.load(input_file_path)
    resume = parse_resume(yaml_obj)

    ODTFile.modify_with(
        input_file_path=model_file_path,
        output_file_path=output_file_path,
        update_content=partial(render_resume_into_element, resume=resume, number_of_jobs=number_of_jobs),
    )