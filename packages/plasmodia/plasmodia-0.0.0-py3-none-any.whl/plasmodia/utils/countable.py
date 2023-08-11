from abc import abstractmethod
from typing import Protocol


class Plural(Protocol):
    @abstractmethod
    def __len__(self) -> int:
        ...
