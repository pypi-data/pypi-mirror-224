from typing import Protocol

from plasmodia.fantasies import MetaVerse
from plasmodia.games import MultiGames
from plasmodia.utils import Plural

from ..gamers import Gamer


class MultiPlayers(Plural, Gamer[MultiGames], Protocol):
    imagination: MetaVerse[MultiGames] | None
