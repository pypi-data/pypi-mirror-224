from abc import abstractmethod
from typing import Protocol, TypeVar

from games import Interactive
from numpy.typing import NDArray

I = TypeVar("I", bound=Interactive)


class Simulatable(Protocol[I]):
    world: I
    "The world to simulate depends on the environment."

    @abstractmethod
    def rollout(self) -> NDArray:
        ...
