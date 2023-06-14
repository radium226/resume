from radium226.resume_generator.parsers import parse_task, parse_paragraph
from radium226.resume_generator.models import ComplexTask, SimpleTask, Description


def test_parse_task():
    task = parse_task({
        "description": "T1",
        "tasks": [
            "T11",
            {
                "description": "T12",
                "tasks": [
                    "T121",
                    "T122",
                ],
            },
            "T13",
        ],
    })
    
    assert task == ComplexTask(
        description=Description(parse_paragraph("T1")),
        tasks=[
            SimpleTask(parse_paragraph("T11")),
            ComplexTask(
                description=Description(parse_paragraph("T12")),
                tasks=[
                    SimpleTask(parse_paragraph("T121")),
                    SimpleTask(parse_paragraph("T122")),
                ],
            ),
            SimpleTask(parse_paragraph("T13")),
        ],
    )