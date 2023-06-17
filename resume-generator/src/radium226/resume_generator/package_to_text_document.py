from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED, ZipInfo
from shutil import copyfileobj

# import os
# import zipfile
# def zipdir(path, ziph):
#     # ziph is zipfile handle
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             ziph.write(os.path.join(root, file))
# zipf = zipfile.ZipFile('Zipped_file.zip', 'w', zipfile.ZIP_DEFLATED)
# zipdir('./my_folder', zipf)
# zipf.close()

def package_to_text_document(folder_path: Path, text_document_file_path: Path) -> None:

    file_paths = filter(Path.is_file, folder_path.rglob("*"))
    
    with ZipFile(text_document_file_path, mode="w") as zip_file:
        for file_path in sorted(file_paths, key=lambda file_path: file_path.name != "mimetype"):
            with file_path.open("rb") as input_stream:
                file_name = str(file_path.relative_to(folder_path))
                
                zip_info = ZipInfo(file_name)
                if file_name != "mimetype":
                    zip_info.compress_type = ZIP_DEFLATED

                with zip_file.open(zip_info, mode="w") as output_stream:
                    copyfileobj(input_stream, output_stream)
        
        zip_file.printdir()

#     root_directory = Path(".")
# for path_object in root_directory.rglob('*'):
#     if path_object.is_file():
#         print(f"hi, I'm a file: {path_object}")
#     elif path_object.is_dir():
#         print(f"hi, I'm a dir: {path_object}")