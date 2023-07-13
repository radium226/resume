from pathlib import Path
from time import sleep

from radium226.opendocument import Document, StorageType, DocumentType
from radium226.opendocument.paragraph import Paragraph
from radium226.opendocument.span import Span
from radium226.headless import Session
from radium226.headless.app import LibreOffice

from fixtures import Result


def test_document_write(document_file_path: Path):
    document = Document(type=DocumentType.TEXT)
    document += Paragraph(
        children=[
            "I'm realy ",
            Span(
                style_name="Strong_20_Emphasis",
                children=["bold"]
            ),
            ", dude! ",
        ],
    )
    document.save_as(document_file_path)