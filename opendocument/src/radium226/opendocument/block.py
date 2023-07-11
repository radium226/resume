from typing import Protocol

class Block(Protocol):

    def __iadd__(self, block: "Block") -> None:
        pass