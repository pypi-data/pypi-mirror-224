from __future__ import annotations

from abc import abstractmethod
from typing import NamedTuple, Protocol, Sequence

import numpy as np
from numpy.typing import NDArray

from .specs import Spec


class State(NamedTuple):
    observation: int | float | NDArray
    reward: float | NDArray
    terminated: bool | NDArray
    truncated: bool | NDArray

    @classmethod
    def concat(cls, seq: Sequence[State]) -> State:
        observations = np.stack([s.observation for s in seq])
        reward = np.stack([s.reward for s in seq])
        termintated = np.stack([s.terminated for s in seq])
        truncated = np.stack([s.truncated for s in seq])
        return cls(observations, reward, termintated, truncated)


class Interactive(Protocol):
    @abstractmethod
    def reset(self, seed: int = 42) -> NDArray:
        ...

    @abstractmethod
    def step(self, action: NDArray) -> State:
        ...

    @property
    @abstractmethod
    def observation_spec(self) -> Spec:
        ...

    @property
    @abstractmethod
    def action_spec(self) -> Spec:
        ...

    def _check_observation_shape(self, observation: NDArray) -> None:
        if (obs_shape := self.observation_spec.shape) != observation.shape:
            raise ValueError(
                "Illegal observation shape. "
                f"Expected: {obs_shape}. Received: {observation.shape}"
            )

    def _check_action_shape(self, action: NDArray) -> None:
        if (act_shape := self.action_spec.shape) != action.shape:
            raise ValueError(
                "Illegal action shape. "
                f"Expected: {act_shape}. Received: {action.shape}."
            )
