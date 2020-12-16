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

    def average(self, ave_fn: Callable = statistics.mean) -> float:
        """Average of values."""
        return ave_fn(self._values)

    def copy(self) -> "Values":
        """A deep copy."""
        return deepcopy(self)

    # def trendy(self,
    #            compare: Callable = __lt__,
    #            ave_fn: Callable = statistics.mean) -> bool:
    #     if self.length == 1:
    #         return True
    #     for index in range(1, self.length):
    #         values = self.values
    #         if not compare(ave_fn(values[:index]), ave_fn(values[index:])):
    #             return False
    #     return True
    #
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
