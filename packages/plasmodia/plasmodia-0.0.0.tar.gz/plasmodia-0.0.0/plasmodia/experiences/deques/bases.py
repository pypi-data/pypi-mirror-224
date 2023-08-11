from abc import ABC, abstractmethod
from collections import deque
from typing import Hashable, Mapping, Sequence

from numpy import ndarray
from numpy.typing import NDArray

from ..interfaces import Experience


class DequeExperienceBase(Experience, ABC):
    def __init__(self) -> None:
        super().__init__()

        self._storage: deque[Mapping[Hashable, NDArray]] = deque()

    def __len__(self) -> int:
        return len(self._storage)

    def __getitem__(
        self, key: int | slice | Sequence[int] | NDArray
    ) -> Mapping[Hashable, NDArray]:
        if isinstance(key, int):
            return self._storage[key]

        if isinstance(key, (ndarray, list, tuple)):
            return self.collate([self._storage[idx] for idx in key])

        if isinstance(key, slice):
            return self[list(range(key.start, key.stop))]

        raise NotImplementedError

    def put(self, data: Mapping[Hashable, NDArray]) -> None:
        self._storage.append(data)

    def extend(self, data: Mapping[Hashable, NDArray]) -> None:
        self._storage.extend(self.dissolve(data))

    @abstractmethod
    def peek(self, count: int = 1) -> Mapping[Hashable, NDArray]:
        ...

    def get(self, count: int = 1) -> Mapping[Hashable, NDArray]:
        assert count > 0, "count must be a positive integer"

        result = [self._storage[idx] for idx in range(count)]

        for _ in range(count):
            self._storage.popleft()

        return self.collate(result)
