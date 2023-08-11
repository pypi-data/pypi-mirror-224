from abc import abstractmethod
from typing import Hashable, Mapping, Protocol, Sequence

import numpy as np
from numpy.typing import NDArray

# TODO: Making collator a component


class Experience(Protocol):
    @abstractmethod
    def __len__(self) -> int:
        ...

    @abstractmethod
    def __getitem__(self, key: int | slice | NDArray) -> Mapping[Hashable, NDArray]:
        ...

    @abstractmethod
    def put(self, data: Mapping[Hashable, NDArray]) -> None:
        ...

    @abstractmethod
    def extend(self, data: Mapping[Hashable, NDArray]) -> None:
        ...

    @abstractmethod
    def peek(self, count: int = 1) -> Mapping[Hashable, NDArray]:
        ...

    @abstractmethod
    def get(self, count: int = 1) -> Mapping[Hashable, NDArray]:
        ...

    def collate(
        self, batch: Sequence[Mapping[Hashable, NDArray]]
    ) -> Mapping[Hashable, NDArray]:
        self._check_collate(batch)

        common_keys = batch[0].keys()
        return {key: np.stack([data[key] for data in batch]) for key in common_keys}

    def dissolve(
        self, batch: Mapping[Hashable, NDArray]
    ) -> Sequence[Mapping[Hashable, NDArray]]:
        self._check_dissolve(batch)

        return [
            {key: value[i] for key, value in batch.items()} for i in range(len(batch))
        ]

    def _check_collate(self, batch: Sequence[Mapping[Hashable, NDArray]]):
        if len(batch) in [0, 1]:
            return

        common_shape = {key: value.shape for key, value in batch[0].items()}
        for data in batch[1:]:
            shape = {key: value.shape for key, value in data.items()}
            if shape != common_shape:
                raise ValueError(
                    "All items must have the same set of properties and corresponding shapes."
                )

    def _check_dissolve(self, batch: Mapping[Hashable, NDArray]):
        lengths = [len(value) for value in batch.values()]
        if len(set(lengths)) <= 1:
            return

        raise ValueError("All properties must have the same length.")
