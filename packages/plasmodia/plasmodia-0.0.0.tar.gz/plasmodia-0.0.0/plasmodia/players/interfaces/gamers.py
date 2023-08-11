from abc import abstractmethod
from typing import Protocol, TypeVar

from numpy.typing import NDArray

from plasmodia.experiences import Experience
from plasmodia.fantasies import Simulatable
from plasmodia.games import Interactive

G = TypeVar("G", bound=Interactive)
"G is the type of game to play."


class Gamer(Protocol[G]):
    imagination: Simulatable[G] | None
    experience: Experience
    game: G

    @abstractmethod
    def _normalize_observation(self, observation: NDArray) -> NDArray:
        ...

    @abstractmethod
    def play(self, observation: NDArray, *, exploration: bool = False) -> NDArray:
        ...

    @abstractmethod
    def learn(self) -> None:
        ...
