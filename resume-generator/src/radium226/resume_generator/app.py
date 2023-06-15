from click import command, argument
from pathlib import Path
from ruamel.yaml import YAML
from lxml.etree import tostring

from .parsers import parse_resume
from .renderers import render_resume



@command()
@argument("yaml_file_path", type=Path, default=Path("../resume.yaml"))
@argument("fodt_file_path", type=Path, default=Path("../resume.fodt"))
def app(yaml_file_path: Path, fodt_file_path: Path):
    print("Resume Generator! ")
    yaml = YAML()
    obj = yaml.load(yaml_file_path)
    resume = parse_resume(obj)
    
    document = render_resume(resume)
    fodt_file_content = tostring(document, encoding="utf-8", pretty_print=True, xml_declaration=True).decode()
    print(fodt_file_content)
    with fodt_file_path.open("w") as fodt_file_stream:
        fodt_file_stream.write(fodt_file_content)

    # for experience in resume.experiences:
    #     for position in experience.position:
    #         print(position.json())

    # print(resume)