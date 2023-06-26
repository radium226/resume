from click import command, argument
from pathlib import Path
from ruamel.yaml import YAML

from ..parsers import parse_resume


@command()
@argument("yaml_file_path", metavar="YAML_FILE", type=Path)
def parse(yaml_file_path: Path) -> None:
    print(f"Parsing {yaml_file_path}... ")

    yaml = YAML()
    resume_obj = yaml.load(yaml_file_path)
    print(resume_obj)
    resume = parse_resume(resume_obj)
    print(resume)