from pathlib import Path

from radium226.opendocument import Document, StorageType, DocumentType
from radium226.opendocument.paragraph import Paragraph


def test_document_write():
    document = Document(type=DocumentType.TEXT)
    document += Paragraph("kikou")
    document.save_as(Path("./test.fodt"))