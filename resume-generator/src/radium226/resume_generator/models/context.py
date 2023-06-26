from dataclasses import dataclass
from typing import NewType

from mistletoe.block_token import Paragraph


Context = NewType("Context", Paragraph)