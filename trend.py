#!/usr/bin/env pypy3
"""Manipulate trends of reals."""

import random
from typing import Callable

from values import Values


class Trend(Values):
    """Trend object."""

    def __init__(
        self,
        length: int = 0,
        rand_func: Callable = random.gauss,
        rand_params: tuple = (0, 1),
    ) -> None:
        super().__init__(length, rand_func, rand_params)

    def __lt__(self, next_trend: "Trend") -> bool:
        """Merging preserves an increasing trend."""
        return self.average() < next_trend.average()

    def __gt__(self, next_trend: "Trend") -> bool:
        """Merging preserves decreasing trend."""
        return self.average() > next_trend.average()

    def __ne__(self, next_trend: "Trend") -> bool:
        """Never merge."""
        _, _ = self, next_trend
        return self.values != next_trend.values

    def __add__(self, next_trend: "Trend") -> "Trend":
        """Concatenate trends."""
        merged_values = self.values + next_trend.values
        assert self.rand_func == next_trend.rand_func
        assert self.rand_params == next_trend.rand_params
        merged_trend = self.copy()
        merged_trend.values = merged_values
        return(merged_trend)
