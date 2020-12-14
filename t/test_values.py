#!/usr/bin/env python3
"""Unit-test values."""

import random

from values import Values


def test_defaults() -> None:
    """Object has correct defaults."""
    values = Values()
    assert values.length == 0
    assert values.rand_func == random.gauss
    assert values.rand_params == (0, 1)


def test_length() -> None:
    """Length set correctly."""
    size = 10
    values = Values(length=size)
    assert values.length == size


def test_rand_func() -> None:
    """Rand_func set correctly."""
    dist = random.uniform
    values = Values(rand_func=dist)
    assert values.rand_func == dist


def test_rand_params() -> None:
    """Rand_params set correctly."""
    params = (10, 20, 30)
    values = Values(rand_params=params)
    assert values.rand_params == params


def test_values() -> None:
    """Values set correctly."""
    nvalues = [7.0, 8.0, 9.0]
    values = Values()
    values.values = nvalues
    assert values.length == len(nvalues)
    assert values.values == nvalues


def test_average() -> None:
    """Average calculated correctly."""
    nvalues = [7.0, 8.0, 9.0]
    values = Values()
    values.values = nvalues
    assert values.average() == sum(nvalues) / len(nvalues)


def test_copy() -> None:
    """Copy made correctly."""
    dist = random.uniform
    size = 10
    params = (10, 20)
    values = Values(length=size, rand_func=dist, rand_params=params)
    values_copy = values.copy()
    # assert values_copy.rand_func == dist
    assert values_copy.length == size
    assert values_copy.rand_params == params
    assert values_copy.values == values.values

    # changing the copy does not change the original
    nvalues = [7.0, 8.0, 9.0]
    values_copy.values = nvalues
    assert values_copy.length != values.length


def test_trendy() -> None:
    """Trendy calculated correctly."""
    nvalues = [7.0, 8.0, 9.0]
    values = Values()
    values.values = nvalues
    assert values.average() == sum(nvalues) / len(nvalues)