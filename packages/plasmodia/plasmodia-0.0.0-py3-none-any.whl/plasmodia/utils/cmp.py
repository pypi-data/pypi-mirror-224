import numpy as np
from numpy.typing import NDArray


def eq(a: NDArray, b: NDArray) -> NDArray:
    return np.isclose(a, b)


def le(a: NDArray, b: NDArray) -> NDArray:
    assert a.shape == b.shape

    return (a < b) | eq(a, b)


def ge(a: NDArray, b: NDArray) -> NDArray:
    return le(b, a)
