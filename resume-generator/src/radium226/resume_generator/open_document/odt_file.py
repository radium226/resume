from typing import Callable
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED, ZipInfo
from shutil import copyfileobj
from lxml.etree import Element, parse, tostring
from io import BytesIO

from ..xml import create_element, append_children_to_parent_element

from .embedded_image import EmbeddedImage


class ODTFile():


    @staticmethod
    def modify_with(
        input_file_path: Path,
        output_file_path: Path,
        update_content: Callable[[Element], None] | None = None,
    ) -> None:
        with ZipFile(input_file_path, mode="r") as input_zip_file:
            with ZipFile(output_file_path, mode="w") as output_zip_file:
                embedded_images = []
                for input_zip_info in input_zip_file.infolist():
                    file_name = input_zip_info.filename
                    if input_zip_info.is_dir():
                        output_zip_file.mkdir(file_name)
                    else:
                        output_zip_info = ZipInfo(file_name)
                        output_zip_info.compress_type = input_zip_info.compress_type
                        with input_zip_file.open(input_zip_info, mode="r") as input_stream:
                            if file_name == "content.xml":
                                element = parse(input_stream)
                                if update_content:
                                    for embedded_image in update_content(element=element):
                                        if embedded_image.name not in [e.name for e in embedded_images]:
                                            embedded_images.append(embedded_image)
                                input_stream = BytesIO(tostring(element))

                            if file_name == "META-INF/manifest.xml":
                                manifest_element_tree = parse(input_stream)
                                manifest_element = manifest_element_tree.getroot()
                                file_entry_elements = []
                                for embedded_image in embedded_images:
                                    file_entry_elements.append(
                                        create_element(
                                            "manifest:file-entry",
                                            attributes={
                                                "manifest:full-path": f"Pictures/{embedded_image.name}",
                                                "manifest:media-type": embedded_image.mime_type,
                                            }
                                        )
                                    )
                                append_children_to_parent_element(manifest_element, file_entry_elements)
                                input_stream = BytesIO(tostring(manifest_element_tree))

                            with output_zip_file.open(output_zip_info, mode="w") as output_stream:
                                copyfileobj(input_stream, output_stream)
                
                for embedded_image in embedded_images:
                    output_zip_info = ZipInfo(f"Pictures/{embedded_image.name}")
                    print(output_zip_info)
                    output_zip_info.compress_type = input_zip_info.compress_type
                    with output_zip_file.open(output_zip_info, mode="w") as output_stream:
                        output_stream.write(embedded_image.content)

                    


    @staticmethod
    def package(input_folder_path: Path, ouput_file_path: Path) -> None:
        # We have to put the mimetype at the begining and store them without compression

        file_paths = filter(Path.is_file, input_folder_path.rglob("*"))

        with ZipFile(ouput_file_path, mode="w") as zip_file:
            for file_path in sorted(file_paths, key=lambda file_path: file_path.name != "mimetype"):
                with file_path.open("rb") as input_stream:
                    file_name = str(file_path.relative_to(input_folder_path))
                    
                    zip_info = ZipInfo(file_name)
                    if file_name != "mimetype":
                        zip_info.compress_type = ZIP_DEFLATED

                    with zip_file.open(zip_info, mode="w") as output_stream:
                        copyfileobj(input_stream, output_stream)