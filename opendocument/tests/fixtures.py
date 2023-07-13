from pytest import fixture
from types import SimpleNamespace
from pathlib import Path
from dataclasses import dataclass
from time import sleep

from radium226.headless import Session
from radium226.headless.app import LibreOffice


@dataclass
class Result:

    test_name: str

    document_file_path: Path
    
    picture_file_path: Path


def pytest_addoption(parser):
    parser.addoption(
        "--result-folder-path", 
        action="store", 
        default=Path("/tmp/radium226-opendocument"), 
        type=Path,
    )


@fixture(scope="session")
def result_folder_path(request) -> Path:
    result_folder_path = request.config.getoption("--result-folder-path")
    result_folder_path.mkdir(
        parents=True,
        exist_ok=True,
    )
    return result_folder_path


@fixture(scope="session")
def session(result_folder_path: Path):
    with Session() as session:
        video_file_path = result_folder_path / "session.mp4"
        session.record_video(video_file_path)
        yield session


@fixture(scope="session", autouse=True)
def results() -> list[Result]:
    results = []
    yield results
    for result in results:
        print(result)


@fixture(scope="function")
def document_file_path(result_folder_path: Path, request) -> Path:
    return result_folder_path / (request.node.name + ".fodt")


@fixture(scope="function", autouse=True)
def libreoffice(session: Session, result_folder_path, document_file_path: Path, results: list[Result], request) -> None:
    yield None
    test_name = request.node.name
    # We open the document file
    session.open_app(LibreOffice(file_path=document_file_path))
    
    sleep(2.5)
    
    # We take the screenshot
    picture_file_path = result_folder_path / ( request.node.name + ".png" )
    session.take_picture(file_path=picture_file_path)
    
    sleep(2.5)

    result = Result(
        test_name=test_name,
        document_file_path=document_file_path,
        picture_file_path=picture_file_path,
    )
    results.append(result)
