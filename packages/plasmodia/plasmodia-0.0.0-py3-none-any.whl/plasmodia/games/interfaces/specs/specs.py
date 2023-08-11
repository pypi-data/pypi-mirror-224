from collections import defaultdict
from dataclasses import dataclass
from functools import cache

import numpy as np
from numpy.typing import DTypeLike, NDArray

from plasmodia import utils

from . import granularity
from .granularity import Granularity


@dataclass(frozen=True)
class Spec:
    bounds: NDArray
    """
    Bounds has the shape [*dimensions, 2]
    where lower bounds are bounds[..., 0], and upper bounds are bounds[..., 1]
    """

    def __post_init__(self):
        try:
            *_, two = self.bounds.shape
        except ValueError:
            raise ValueError("Bounds should be at least 2D.")

        if two != 2:
            raise ValueError("The last dimension should store [lower, upper] pairs.")

        if (dtype := self.dtype) not in (keys := granularity.from_types.keys()):
            raise ValueError(f"Dtype {dtype} is invalid. Expected one of {list(keys)}")

    def __contains__(self, coord: NDArray):
        return self.contains(coord)

    @property
    def lower(self) -> NDArray:
        return self.bounds[..., 0]

    @property
    def upper(self) -> NDArray:
        return self.bounds[..., 1]

    @property
    @cache
    def shape(self) -> tuple[int, ...]:
        return tuple(self.bounds.shape[:-1])

    @property
    def dtype(self) -> DTypeLike:
        return self.bounds.dtype

    def contains(self, coord: NDArray) -> bool:
        if coord.shape != self.shape:
            raise ValueError(f"Dimension mismatch. Should be: {self.shape}")

        return (utils.ge(coord, self.lower) & utils.le(coord, self.upper)).all().item()

    @property
    def granularity(self) -> Granularity:
        def unreachable():
            raise ValueError("Invalid dtype specified")

        granularity_mapping: dict[DTypeLike, Granularity] = defaultdict(
            unreachable, granularity.from_types
        )
        return granularity_mapping[self.dtype]

    @classmethod
    def from_bounds(cls, low: NDArray, high: NDArray, dtype: DTypeLike):
        return cls(bounds=np.concatenate([low, high], dtype=dtype))
