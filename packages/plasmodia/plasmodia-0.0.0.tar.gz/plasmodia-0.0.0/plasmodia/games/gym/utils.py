import numpy as np
from gymnasium.spaces import Box, Discrete, MultiDiscrete, Space

from ..interfaces import Spec


def gym_space_to_spec(space: Space) -> Spec:
    if isinstance(space, Box):
        return box_to_spec(space)

    if isinstance(space, Discrete):
        return discrete_to_spec(space)

    if isinstance(space, MultiDiscrete):
        return multi_discrete_to_spec(space)

    raise NotImplementedError


def box_to_spec(space: Box) -> Spec:
    low = space.low
    high = space.high
    return Spec.from_bounds(low=low, high=high, dtype="f")


def discrete_to_spec(space: Discrete) -> Spec:
    shape = space.shape if space.shape is not None else []
    low = np.zeros(shape=shape)
    high = np.full(shape=shape, fill_value=space.n)
    return Spec.from_bounds(low=low, high=high, dtype="i")


def multi_discrete_to_spec(space: MultiDiscrete) -> Spec:
    shape = space.shape
    low = np.zeros(shape=shape)
    high = space.nvec
    return Spec.from_bounds(low=low, high=high, dtype="i")
