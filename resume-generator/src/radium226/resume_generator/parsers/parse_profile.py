from typing import Generator
from mistletoe import Document, markdown
from mistletoe.block_token import Paragraph
from mistletoe.ast_renderer import ASTRenderer

from ..models import Profile


def parse_profile(obj: str) -> Profile:
    print(" === parse_profile === ")
    print(obj)
    document = Document(obj.splitlines(keepends=True))
    print(markdown(obj.splitlines(keepends=True), ASTRenderer))
    
    def iter_document() -> Generator[Paragraph, None, None]:
        for paragraph in document.children:
            match paragraph:
                case Paragraph(): # type: ignore
                    yield paragraph

    paragraphs=list(iter_document())
    
    profile = Profile(paragraphs=paragraphs)
    
    return profile