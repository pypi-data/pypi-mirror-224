from typing import Hashable, Mapping

from numpy.typing import NDArray

from .bases import DequeExperienceBase


class FIFODequeExperience(DequeExperienceBase):
    def peek(self, count: int = 1) -> Mapping[Hashable, NDArray]:
        assert count > 0, "count must be a positive integer"

        result = [self._storage[idx] for idx in range(count)]
        return self.collate(result)
