from dataclasses import dataclass, field
from enum import StrEnum, auto

from lxml.etree import _Element, parse, tostring
from pathlib import Path

from .content import Content
from .block import Block
from .namespaces_by_prefix import NAMESPACES_BY_PREFIX
from .storage_type import StorageType
from .document_type import DocumentType

from .xml import create_element


@dataclass
class Document():

    type: DocumentType

    content: Content = field(default_factory=Content)

    def __iadd__(self, block: Block) -> None:
        self.content += block
        return self

    def save_as(self, file_path: Path) -> None:
        storage_type = {
            '.odt': StorageType.ZIP_CONTAINER,
            '.fodt': StorageType.XML_FLAT,
        }[file_path.suffix.lower()]

        with file_path.open("wb") as output_stream:
            output_stream.write(self.serialize(storage_type))

    def serialize(self, storage_type: StorageType = StorageType.XML_FLAT) -> bytes:
        match storage_type:
            case StorageType.XML_FLAT:
                return self._write_xml_flat()

            case StorageType.ZIP_CONTAINER:
                return self._write_zip_container()

    def _write_xml_flat(self) -> bytes:
        empty_file_path = Path(__file__).parent / "data" / "empty.fodt"
        with empty_file_path.open("r") as stream:
            element_tree = parse(stream)
            document_element = element_tree.getroot()
            body_element_to_replace = next(iter(document_element.xpath("/office:document/office:body", namespaces=NAMESPACES_BY_PREFIX)))
            match self.type:
                case DocumentType.TEXT:
                    body_element = create_element(
                        "office:body",
                        children=[
                            create_element(
                                "office:text",
                                children=[
                                    element 
                                    for child_block in self.content.child_blocks 
                                    for element in child_block.to_elements()
                                ],
                            ),
                        ],
                    )


            document_element.replace(body_element_to_replace, body_element)

            return tostring(element_tree, xml_declaration=True, encoding="UTF-8")

    def _write_zip_container(self) -> bytes:
        raise Exception("Not yet implemented! ")

        