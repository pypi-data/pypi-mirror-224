from typing import Protocol

from plasmodia.games import Game

from .gamers import Gamer


class Player(Gamer[Game], Protocol):
    pass
