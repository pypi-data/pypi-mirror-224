from dataclasses import dataclass
from numbers import Number
from typing import (
    Any,
    ItemsView,
    Iterator,
    KeysView,
    Mapping,
    Protocol,
    Sequence,
    ValuesView,
)

import numpy as np
import torch
from numpy.typing import NDArray
from torch.nn import Module
from torch.optim import Optimizer

from ..interfaces import IterativeLearners


@dataclass(frozen=True)
class ExperienceBatch(Mapping[str, Any]):
    prev_obs: NDArray
    obs: NDArray
    action: NDArray
    reward: Number

    def keys(self) -> KeysView[str]:
        return self.__dict__.keys()

    def values(self) -> ValuesView[Any]:
        return self.__dict__.values()

    def items(self) -> ItemsView[str, Any]:
        return self.__dict__.items()

    def __iter__(self) -> Iterator[str]:
        return iter(self.keys())

    def __getitem__(self, key: str) -> Any:
        return self.__dict__[key]

    def __len__(self) -> int:
        return len(self.__dict__)


class ReinforcementLearning(IterativeLearners, Protocol):
    network: Module
    optimizer: Optimizer

    @torch.no_grad()
    def practice(self, episode: int) -> None:
        observation = self.game.reset()
        reward = float("-inf")
        done = False

        while not done:
            prev_observation = observation
            normalized = self._normalize_observation(observation)
            action = self.play(normalized, exploration=True)
            observation, reward, terminated, truncated = self.game.step(action)

            done = terminated or truncated

            self.experience.put(
                dict(
                    ExperienceBatch(
                        prev_obs=prev_observation,
                        obs=observation,
                        action=action,
                        reward=reward,
                    )
                )
            )

    @staticmethod
    def expected_reward(reward_list: Sequence[float] | NDArray):
        reward_list = np.array(reward_list)
        expected_total = np.cumsum(reward_list[::-1])[::-1]
        return expected_total
