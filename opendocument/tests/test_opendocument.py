from radium226.opendocument import Text
from radium226.opendocument.text import Paragraph


def test_text():

    with Document() as document:
        with Text() as text:
            pass
