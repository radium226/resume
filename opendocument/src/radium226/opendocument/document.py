from dataclasses import dataclass, field

from lxml.etree import _Element

from .styles import Styles
from .body import Body
from .content import Content


@dataclass
class Document():

    styles: list[Style] = field(default_factory=list)

    embedded_images: list[EmbeddedImage] = field(default_factory=list)

    body = field(default_factory=Body)
    
    def __iadd__(self, content: Content) -> None:
        self.body += content

    def to_elements(self, styles: Styles) -> list[_Element]:


    def write(self, flat: bool = True) -> bytes:
        elements = self.body.to_elements(self.styles, self.embedded_images)


    @classmethod
    def empty() -> "Document":
        pass

        