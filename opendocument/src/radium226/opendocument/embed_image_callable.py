from typing import Protocol

from pathlib import Path
from lxml.etree import _Element


class EmbedImageCallable(Protocol):

    def __call__(self, image_file_path: Path) -> _Element:
        pass