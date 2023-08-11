from typing import Protocol

from .interactive import Interactive


class Game(Interactive, Protocol):
    pass
