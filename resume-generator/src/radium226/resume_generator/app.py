from click import command, argument
from pathlib import Path

# from .models import Resume



@command()
@argument("yaml_file_path", type=Path)
def app(yaml_file_path: Path):
    print("Resume Generator! ")
    # resume = Resume.parse_file(yaml_file_path)

    # for experience in resume.experiences:
    #     for position in experience.position:
    #         print(position.json())

    # print(resume)