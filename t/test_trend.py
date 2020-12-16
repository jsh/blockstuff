#!/usr/bin/env python3
"""Unit-test values."""
# pylint:disable=comparison-with-callable

import random

from trend import Trend


def test_defaults() -> None:
    """Object has correct defaults."""
    trend = Trend()
    assert trend.length == 0
    assert trend.rand_func == random.gauss
    assert trend.rand_params == (0, 1)


def test___lt__() -> None:
    """< compares correctly."""
    left = Trend()
    left.values = [1]
    right = Trend()
    right.values = [2]
    assert left < right


def test___gt__() -> None:
    """> compares correctly."""
    left = Trend()
    left.values = [2]
    right = Trend()
    right.values = [1]
    assert left > right


def test___ne__() -> None:
    """!= compares correctly."""
    left = Trend(length=10)
    right = Trend(length=10)
    assert left != right


def test___add__() -> None:
    """+ merges trends"""
    left = Trend()
    left.values = [2, 7]
    right = Trend()
    right.values = [1, 8]
    merger = left + right
    assert merger.values == [2, 7, 1, 8]
    assert merger.length == 4
