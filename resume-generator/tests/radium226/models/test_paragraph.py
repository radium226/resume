from radium226.resume_generator.parser import parse_paragraph


def test_parse_paragraph():
    paragraph = parse_paragraph("This is *bold*")
    print(paragraph.children)