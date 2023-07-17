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

    """
    drwxr-xr-x  2 adrien adrien      3 Jun 26 17:25 META-INF
    -rw-r--r--  1 adrien adrien 460405 Jun 26 17:25 CV.odt
    drwxr-xr-x  2 adrien adrien      3 Jun 26 17:25 Thumbnails
    -rw-r--r--  1 adrien adrien  46976 Jun 26 17:25 styles.xml
    -rw-r--r--  1 adrien adrien  14404 Jun 26 17:25 settings.xml
    drwxr-xr-x  2 adrien adrien     18 Jun 26 17:25 Pictures
    -rw-r--r--  1 adrien adrien     39 Jun 26 17:25 mimetype
    -rw-r--r--  1 adrien adrien   1051 Jun 26 17:25 meta.xml
    -rw-r--r--  1 adrien adrien    899 Jun 26 17:25 manifest.rdf
    -rw-r--r--  1 adrien adrien 174395 Jun 26 17:25 content.xml
    """

    type: DocumentType

    styles: _Element | None = field(init=False)

    settings: _Element | None = field(init=False)

    meta: _Element | None = field(init=False)

    file_path: InitVar[Path] = field(default_factory=lambda: Path(__file__).parent / "data" / "empty.fodt")

    content: Content = field(default_factory=Content)

    def __post_init__(self, file_path: Path):
        match self._storage_type_from_file(file_path):
            case StorageType.XML_FLAT:
                self._read_xml_flat(file_path)

            case StorageType.ZIP_CONTAINER:
                self._read_zip_container(file_path)

    def _storage_type_from_file(file_path: Path) -> StorageType:
        file_extension = file_path.suffix.lower()
        storage_types_by_file_extension = {
            '.odt': StorageType.ZIP_CONTAINER,
            '.fodt': StorageType.XML_FLAT,
        }
        return storage_types_by_file_extension[file_extension]

    def _read_xml_flat(self, file_path) -> None:
        with file_path.open("r") as file_stream:
            element_tree = parse(input_stream)
            document_element = element_tree.getroot()

        
    def __iadd__(self, block: Block) -> None:
        self.content += block
        return self

    def save_as(self, file_path: Path) -> None:
        

        with file_path.open("wb") as output_stream:
            output_stream.write(self.serialize(storage_type))

    def serialize(self, storage_type: StorageType = StorageType.XML_FLAT) -> bytes:
        match storage_type:
            case StorageType.XML_FLAT:
                return self._write_xml_flat()

            case StorageType.ZIP_CONTAINER:
                return self._write_zip_container()

    def _write_xml_flat(self) -> bytes:
        empty_file_path = 
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