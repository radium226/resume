from pathlib import Path
from time import sleep

from radium226.opendocument import Document, StorageType, DocumentType
from radium226.opendocument.paragraph import Paragraph

from radium226.headless import Session
from radium226.headless.app import LibreOffice

from fixtures import Result


def test_document_write(document_file_path: Path):
    document = Document(type=DocumentType.TEXT)
    document += Paragraph("kikou")
    document.save_as(document_file_path)