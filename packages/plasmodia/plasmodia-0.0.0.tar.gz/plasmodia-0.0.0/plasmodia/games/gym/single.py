from gymnasium import Env
from numpy.typing import NDArray

from plasmodia.games.interfaces.interactive import State
from plasmodia.games.interfaces.specs import Spec

from ..interfaces import Game
from . import utils


class GymEnvWrapper(Game):
    def __init__(self, env: Env) -> None:
        super().__init__()

        self._env = env
        self._obs_spec = utils.gym_space_to_spec(env.observation_space)
        self._act_spec = utils.gym_space_to_spec(env.action_space)

    def reset(self, seed: int = 42) -> NDArray:
        obs, _ = self._env.reset(seed=seed)
        return obs

    def step(self, action: NDArray) -> State:
        obs, reward, term, trunc, _ = self._env.step(action)
        return State(obs, float(reward), term, trunc)

    @property
    def observation_spec(self) -> Spec:
        return self._obs_spec

    @property
    def action_spec(self) -> Spec:
        return self._act_spec
