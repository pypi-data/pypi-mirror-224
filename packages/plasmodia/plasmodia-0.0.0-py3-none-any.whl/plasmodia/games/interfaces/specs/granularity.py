from enum import Enum
from types import MappingProxyType

import numpy as np
from numpy.typing import DTypeLike


class Granularity(str, Enum):
    CONTINUOUS = "CONT"
    DISCRETE = "DISC"


from_types: MappingProxyType[DTypeLike, Granularity] = MappingProxyType(
    {
        # Boolean types.
        bool: Granularity.DISCRETE,
        "bool": Granularity.DISCRETE,
        np.bool_: Granularity.DISCRETE,
        # Integer types.
        int: Granularity.DISCRETE,
        "int": Granularity.DISCRETE,
        "int16": Granularity.DISCRETE,
        "int32": Granularity.DISCRETE,
        "int64": Granularity.DISCRETE,
        "int128": Granularity.DISCRETE,
        np.int_: Granularity.DISCRETE,
        np.int16: Granularity.DISCRETE,
        np.int32: Granularity.DISCRETE,
        np.int64: Granularity.DISCRETE,
        np.int128: Granularity.DISCRETE,
        # Floating point types.
        float: Granularity.CONTINUOUS,
        "float": Granularity.CONTINUOUS,
        "float16": Granularity.CONTINUOUS,
        "float32": Granularity.CONTINUOUS,
        "float64": Granularity.CONTINUOUS,
        "float128": Granularity.CONTINUOUS,
        np.float_: Granularity.CONTINUOUS,
        np.float16: Granularity.CONTINUOUS,
        np.float32: Granularity.CONTINUOUS,
        np.float64: Granularity.CONTINUOUS,
        np.float128: Granularity.CONTINUOUS,
    }
)
