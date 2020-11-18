#!/usr/bin/env python3
"""Unit-test blockstuff."""

import random

from blockstuff import (
    always,
    assimilate_block,
    average,
    decompose_into_blocks,
    decreasing_trend,
    increasing_trend,
    merge,
    never,
    random_block,
    rotate_blocks,
    rotate_to_single_block,
)


def test_always() -> None:
    """Always succeeds."""
    assert always([3.0, 2.0], [20.0, 2.0, 3.0, 4.0])
    assert always([4.0, 3.0, 2.0, 20.0], [2.0, 3.0])


def test_assimilate_block() -> None:
    """Assimilates new block with old blocks."""
    assert assimilate_block([], [1.0, 2.0]) == [[1.0, 2.0]]
    assert assimilate_block([[1.0, 2.0]], [3.0, 4.0]) == [[1.0, 2.0, 3.0, 4.0]]
    assert assimilate_block([[3.0, 4.0]], [1.0, 2.0]) == [[3.0, 4.0], [1.0, 2.0]]


def test_average() -> None:
    """Average is between extremes."""
    assert 1 < average([1.0, 2.0]) < 2
    seq = []
    for _ in range(10):
        seq.append(random.random())  # nosec
    assert min(seq) < average(seq) < max(seq)


def test_decompose_into_blocks() -> None:
    """Decomposes into blocks."""
    seq = [1.0, 2.0, 3.0, 1.1]
    blocks = decompose_into_blocks(seq)
    assert [[1.0, 2.0, 3.0], [1.1]] == blocks


def test_decreasing_trend() -> None:
    """Average of second arg < average of first arg."""
    assert decreasing_trend([100.0], [2.0])
    assert decreasing_trend([101.0, 2.0], [20.0, 2.0, 3.0, 4.0])
    assert not decreasing_trend([3.0, 2.0], [20.0, 2.0, 3.0, 4.0])


def test_increasing_trend() -> None:
    """Average of second arg > average of first arg."""
    assert increasing_trend([2.0], [100.0])
    assert increasing_trend([4.0, 3.0, 2.0, 20.0], [2.0, 101.0])
    assert not increasing_trend([4.0, 3.0, 2.0, 20.0], [2.0, 3.0])


def test_merge() -> None:
    """Merges two blocks."""
    assert merge([], [1.0]) == [1.0]
    assert merge([1.0], [2.0]) == [1.0, 2.0]
    assert merge([1.0, 2.0], [3.0, 4.0]) == [1.0, 2.0, 3.0, 4.0]


def test_never() -> None:
    """Always fails"""
    assert not never([3.0, 2.0], [20.0, 2.0, 3.0, 4.0])
    assert not never([4.0, 3.0, 2.0, 20.0], [2.0, 3.0])


def test_random_block() -> None:
    """Creates random block."""
    length = 100
    elems = random_block(length, random.uniform, 0, 1)
    assert len(elems) == length
    assert (len(set(elems))) == length  # they're all different
    assert (0 <= elem < 1 for elem in elems)


def test_rotate_blocks() -> None:
    """"Rotates blocks."""
    blocks = [[4.0], [3.0], [1.0]]
    blocks = rotate_blocks(blocks)
    assert blocks == [[3.0], [1.0, 4.0]]
    blocks = rotate_blocks(blocks)
    assert blocks == [[1.0, 4.0, 3.0]]
    assert rotate_blocks(blocks) == blocks  # no-op


def test_rotate_to_single_block() -> None:
    """"Rotates to single block in one call."""
    blocks = [[4.0], [3.0], [1.0]]
    blocks = rotate_to_single_block(blocks)
    assert blocks == [[1.0, 4.0, 3.0]]
    blocks = rotate_to_single_block(blocks)
    assert blocks == [[1.0, 4.0, 3.0]]
