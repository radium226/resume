from click import command, argument
from pathlib import Path
from ruamel.yaml import YAML

from .parsers import parse_resume



@command()
@argument("yaml_file_path", type=Path, default=Path("../resume.yaml"))
def app(yaml_file_path: Path):
    print("Resume Generator! ")
    yaml = YAML()
    obj = yaml.load(yaml_file_path)
    resume = parse_resume(obj)
    print(resume)

    # for experience in resume.experiences:
    #     for position in experience.position:
    #         print(position.json())

    # print(resume)