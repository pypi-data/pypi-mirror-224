from typing import Sequence, overload

import numpy as np
from numpy.typing import NDArray

from plasmodia.games.interfaces.interactive import State
from plasmodia.games.interfaces.specs import Spec

from ..interfaces import Game, MultiGames


class IndependentGames(MultiGames):
    def __init__(self, games: Sequence[Game]) -> None:
        super().__init__()

        self._obs_spec = self.join_specs([g.observation_spec for g in games])
        self._act_spec = self.join_specs([g.action_spec for g in games])
        self._games = games

    def __len__(self):
        return len(self._games)

    @overload
    def __getitem__(self, key: int) -> Game:
        ...

    @overload
    def __getitem__(self, key: slice) -> MultiGames:
        ...

    def __getitem__(self, key: int | slice) -> Game | MultiGames:
        if isinstance(key, slice):
            sliced = self._games[key]
            return IndependentGames(sliced)

        return self._games[key]

    def __iter__(self):
        return iter(self._games)

    def reset(self, seed: int = 42) -> NDArray:
        obs = []
        for game in self._games:
            obs.append(game.reset(seed=seed))
        return np.array(obs)

    def step(self, action: NDArray) -> State:
        if len(action) != len(self):
            raise ValueError("Action should be specified for each environment.")

        obs: list[State] = []
        for game, act in zip(self._games, action):
            obs.append(game.step(act))
        return State.concat(obs)

    @property
    def observation_spec(self) -> Spec:
        return self._obs_spec

    @property
    def action_spec(self) -> Spec:
        return self._act_spec
