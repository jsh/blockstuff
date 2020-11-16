#!/usr/bin/env python3
"""Unit-test blockstuff."""

from random import random

from blockstuff import (
    always,
    assimilate_block,
    average,
    decreasing_trend,
    increasing_trend,
    merge,
    never,
)


def test_average() -> None:
    """Average is between extremes."""
    assert 1 < average([1, 2]) < 2
    seq = []
    for _ in range(10):
        seq.append(random())  # nosec
    assert min(seq) < average(seq) < max(seq)


def test_increasing_trend() -> None:
    """Average of second arg > average of first arg."""
    assert increasing_trend([2], [100])
    assert increasing_trend([4, 3, 2, 20], [2, 101])
    assert not increasing_trend([4, 3, 2, 20], [2, 3])


def test_decreasing_trend() -> None:
    """Average of second arg < average of first arg."""
    assert decreasing_trend([100], [2])
    assert decreasing_trend([101, 2], [20, 2, 3, 4])
    assert not decreasing_trend([3, 2], [20, 2, 3, 4])


def test_always() -> None:
    """Always succeed."""
    assert always([3, 2], [20, 2, 3, 4])
    assert always([4, 3, 2, 20], [2, 3])


def test_never() -> None:
    """Always fail."""
    assert not never([3, 2], [20, 2, 3, 4])
    assert not never([4, 3, 2, 20], [2, 3])


def test_merge() -> None:
    """Merge two blocks."""
    assert merge([], [1.0]) == [1.0]
    assert merge([1.0], [2.0]) == [1.0, 2.0]
    assert merge([1.0, 2.0], [3.0, 4.0]) == [1.0, 2.0, 3.0, 4.0]


def test_assimilate_block() -> None:
    """Assimilate new block with old blocks."""
    assert assimilate_block([], [1, 2]) == [[1, 2]]
    assert assimilate_block([[1, 2]], [3, 4]) == [[1, 2, 3, 4]]
    assert assimilate_block([[3, 4]], [1, 2]) == [[3, 4], [1, 2]]
