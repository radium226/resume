from typing import Callable
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED, ZipInfo
from shutil import copyfileobj
from lxml.etree import Element, parse, tostring
from io import BytesIO


class ODTFile():


    @staticmethod
    def modify_with(
        input_file_path: Path,
        output_file_path: Path,
        update_content: Callable[[Element], None] | None = None,
    ) -> None:
        with ZipFile(input_file_path, mode="r") as input_zip_file:
            with ZipFile(output_file_path, mode="w") as output_zip_file:
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
                                    update_content(element=element)
                                input_stream = BytesIO(tostring(element))

                            with output_zip_file.open(output_zip_info, mode="w") as output_stream:
                                copyfileobj(input_stream, output_stream)


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