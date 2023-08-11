from abc import abstractmethod
from typing import Protocol

from plasmodia.games import Game

from .simulations import Simulatable


class Fantasy(Simulatable, Protocol):
    @property
    @abstractmethod
    def game(self) -> Game:
        ...
