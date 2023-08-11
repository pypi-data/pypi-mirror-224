from typing import Hashable, Mapping

import numpy as np
from numpy import ndarray
from numpy.typing import NDArray

from .interfaces import Experience


class ListExperience(Experience):
    def __init__(self) -> None:
        super().__init__()

        self._storage: list[Mapping[Hashable, NDArray]] = []

    def __len__(self) -> int:
        return len(self._storage)

    def __getitem__(self, key: int | slice | NDArray) -> Mapping[Hashable, NDArray]:
        if isinstance(key, int):
            return self._storage[key]

        if isinstance(key, slice):
            return self.collate(self._storage[key])

        if isinstance(key, ndarray):
            data = np.array(self._storage)[key]
            return self.collate(list(data))

        raise NotImplementedError

    def put(self, data: Mapping[Hashable, NDArray]) -> None:
        self._storage.append(data)

    def extend(self, data: Mapping[Hashable, NDArray]) -> None:
        self._storage.extend(self.dissolve(data))

    def peek(self, count: int = 1) -> Mapping[Hashable, NDArray]:
        return self.collate(self._storage[:count])

    def get(self, count: int = 1) -> Mapping[Hashable, NDArray]:
        result = self._storage[:count]
        self._storage = self._storage[count:]
        return self.collate(result)
