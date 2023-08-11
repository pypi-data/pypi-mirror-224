from typing import Hashable, Mapping

from numpy import random as np_random
from numpy.typing import NDArray

from .bases import DequeExperienceBase


class UniformDequeExperience(DequeExperienceBase):
    def __init__(self) -> None:
        super().__init__()

    def peek(self, count: int = 1) -> Mapping[Hashable, NDArray]:
        assert count > 0, "count must be a positive integer"

        indices = np_random.choice(len(self), count, replace=False)

        # Unfortuantely, deque doesn't support indexing with a list of indices.
        result = [self._storage[i] for i in indices]
        return self.collate(result)
