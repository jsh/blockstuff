#!/usr/bin/env pypy3
"""Manipulate sequences of real values."""

import random
import re
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
        self._values = [rand_func(*self._rand_params) for _ in range(self._length)]

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

    def __str__(self) -> str:
        """String representation."""
        pat = re.compile(r"<bound method (\S+)")
        match = pat.match(f"{self.rand_func}")
        if match:
            rand_func_name = match.group(1)
        else:
            rand_func_name = "No random function"
        return (
            f"length={self.length}, rand_func_name={rand_func_name}, "
            f"rand_params={self.rand_params}, values={self.values}"
        )

    def __lt__(self, other: "Values") -> bool:
        """Average less that of than right arg."""
        return self.average() < other.average()

    def __gt__(self, other: "Values") -> bool:
        """Average greater than that of right arg."""
        return self.average() > other.average()

    def __ne__(self, other) -> bool:
        """Two Values unequal."""
        return self.values != other.values

    def __eq__(self, other) -> bool:
        """Two Values unequal."""
        return self.values == other.values

    def __add__(self, other: "Values") -> "Values":
        """Concatenate values."""
        assert self.rand_func == other.rand_func
        assert self.rand_params == other.rand_params
        merger = self.copy()
        merger.values = self.values + other.values
        return merger

    def average(self, ave_fn: Callable = statistics.mean) -> float:
        """Average of values."""
        return ave_fn(self.values)

    def copy(self) -> "Values":
        """A deep copy."""
        return deepcopy(self)
