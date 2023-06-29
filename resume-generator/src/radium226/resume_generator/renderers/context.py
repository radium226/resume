from lxml.etree import Element
from contextvars import ContextVar
from pathlib import Path
from dataclasses import dataclass

from ..open_document import EmbeddedImage, TableStyle, text


CURRENT_CONTEXT = ContextVar("CURRENT_CONTEXT")


MIME_TYPES_BY_SUFFIX = {
    ".svg": "image/svg+xml",
    ".png": "image/png",
}



class RenderContext():

    def __init__(self):
        self.number_of_tables = 10
        self.embedded_images = []

    def next_table_name(self) -> str:
        self.number_of_tables += 1
        return f"Tableau_{self.number_of_tables}"

    def embedded_image(self, *, file_path: Path, width: str | None = None, height: str | None = None) -> Element:
        with file_path.open("rb") as file_stream:
            embedded_image_content = file_stream.read()
            embedded_image_name = file_path.name
            embedded_image_mime_type = MIME_TYPES_BY_SUFFIX[file_path.suffix.lower()]
            self.embedded_images.append(
                EmbeddedImage(
                    name=embedded_image_name,
                    mime_type=embedded_image_mime_type,
                    content=embedded_image_content,
                )
            )

            return text.frame(
                width=width,
                height=height,
                children=[
                    text.image(
                        href=f"Pictures/{embedded_image_name}",
                        mime_type=embedded_image_mime_type,
                    ),
                ]
            )
    
    def register_table_style(table_style: TableStyle) -> None:
        pass



def init_current_render_context() -> None:
    CURRENT_CONTEXT.set(RenderContext())


def get_current_render_context() -> RenderContext:
    return CURRENT_CONTEXT.get()
