from typing import Protocol, Sequence

import numpy as np

from plasmodia import utils
from plasmodia.utils import Plural

from .interactive import Interactive
from .specs import Spec


class MultiGames(Plural, Interactive, Protocol):
    @staticmethod
    def join_specs(specs: Sequence[Spec]) -> Spec:
        try:
            # Check if all specs have the same shape and dtype.
            _ = utils.unique_or_raise([spec.shape for spec in specs])
            _ = utils.unique_or_raise([spec.dtype for spec in specs])
        except ValueError:
            raise ValueError("Cannot join spaces because they are not compatible.")

        bounds = np.stack([spec.bounds for spec in specs], casting="no")
        return Spec(bounds=bounds)
