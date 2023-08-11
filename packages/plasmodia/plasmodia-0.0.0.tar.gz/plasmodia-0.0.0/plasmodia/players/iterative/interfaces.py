from abc import abstractmethod
from typing import Protocol

from alive_progress import alive_it

from ..interfaces import MultiPlayers


class IterativeLearners(MultiPlayers, Protocol):
    iterations: int

    def learn(self, batch_size: int) -> None:
        for i in alive_it(range(self.iterations)):
            self.episode(i, batch_size=batch_size)

    def episode(self, i: int, batch_size: int) -> None:
        self.practice(i)
        self.improve(i, batch_size=batch_size)

    @abstractmethod
    def practice(self, episode: int) -> None:
        ...

    @abstractmethod
    def improve(self, episode: int, batch_size: int) -> None:
        ...
