#!/usr/bin/env python

from contextlib import contextmanager
from contextvars import ContextVar
from typing import Generator


CURRENT_TEXT: ContextVar[str] = ContextVar("CURRENT_TEXT", default="Kikou")


@contextmanager
def block(text: str) -> Generator[str, None, None]:
    old = CURRENT_TEXT.get()
    CURRENT_TEXT.set(text)
    yield text
    CURRENT_TEXT.set(old)


if __name__ == "__main__":
    print("1 " + CURRENT_TEXT.get())
    with block("a"):
        print("2 " + CURRENT_TEXT.get())
        with block("b"):
            print("3 " + CURRENT_TEXT.get())
        print("4 " + CURRENT_TEXT.get())
    print("5 " + CURRENT_TEXT.get())
    