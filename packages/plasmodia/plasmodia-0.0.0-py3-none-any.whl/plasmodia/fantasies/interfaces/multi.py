from abc import abstractmethod
from typing import Protocol

from plasmodia.games import Game

from .simulations import Simulatable
from .single import Fantasy


class MetaVerse(Simulatable, Protocol):
    @abstractmethod
    def fantasies(self) -> tuple[Fantasy, ...]:
        ...

    @abstractmethod
    def games(self) -> tuple[Game, ...]:
        ...
