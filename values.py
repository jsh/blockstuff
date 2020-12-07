#!/usr/bin/env pypy3
"""Manipulate sequences of real values."""

import random
import statistics
from copy import deepcopy
from typing import Callable, List


class Values:
    """A simple sequence of random floats."""

    def __init__(
        self,
        length: int = 0,
        rand_func: Callable = random.gauss,
        rand_params: tuple = (0, 1),
    ) -> None:
        """Create a block full of random numbers."""
        self._length = length
        self._rand_func = rand_func
        self._rand_params = rand_params
        self._values = [rand_func(*rand_params) for _ in range(length)]

    @property
    def length(self) -> int:
        """Length getter."""
        return self._length

    @property
    def rand_func(self) -> Callable:
        """Rand_func getter."""
        return self._rand_func

    @property
    def rand_params(self) -> tuple:
        """Rand_tuple getter."""
        return self._rand_params

    @property
    def values(self) -> List[float]:
        """Values getter."""
        return self._values

    @values.setter
    def values(self, new_values: List[float]) -> None:
        """Values setter."""
        self._length = len(new_values)
        self._values = new_values

    def average(self, ave_fn: Callable = statistics.mean) -> float:
        """Average of values."""
        return ave_fn(self._values)

    def copy(self) -> "Values":
        """A deep copy."""
        return deepcopy(self)
