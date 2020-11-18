#!/usr/bin/env pypy3
"""Manipulate trends of reals."""

import statistics
from copy import deepcopy
from typing import Callable, List

Block = List[float]
Blocks = List[Block]


def average(seq: Block, ave_fn: Callable = statistics.mean) -> float:
    """An average."""
    return ave_fn(seq)


def increasing_trend(old_block: Block, new_block: Block) -> bool:
    """Merging preserves an increasing trend."""
    return average(old_block) < average(new_block)


def decreasing_trend(old_block: Block, new_block: Block) -> bool:
    """Merging preserves decreasing trend."""
    return average(old_block) > average(new_block)


def always(old_block: Block, new_block: Block) -> bool:
    """Always merge."""
    _, _ = (old_block, new_block)
    return True


def never(old_block: Block, new_block: Block) -> bool:
    """Never merge."""
    _, _ = old_block, new_block
    return False


def merge(old_block: Block, new_block: Block) -> Block:
    """Concatenate blocks."""
    return old_block + new_block


def assimilate_block(
    blocks: Blocks, new_block: Block, meldable=increasing_trend
) -> Blocks:
    """Assimilate new block into old using criterion meldable."""
    blocks = deepcopy(blocks)  # don't modify the original
    if not blocks:
        return [new_block]
    block = blocks.pop()
    if not meldable(block, new_block):
        return blocks + [block, new_block]
    block = merge(block, new_block)
    return assimilate_block(blocks, block, meldable)


def decompose_into_blocks(elems: Block) -> Blocks:
    """Break a sequence into blocks."""
    blocks: Blocks = []
    for elem in elems:
        blocks = assimilate_block(blocks, [elem])  # nosec
    return blocks


def random_block(length: int, rand_func: Callable, *args) -> Block:
    """Create a block full of random numbers."""
    return [rand_func(*args) for _ in range(length)]


def rotate_blocks(blocks: Blocks) -> Blocks:
    """
    Shift off the leading, leftmost block,
    then push it onto the right end, assimilating as needed.
    """
    leftmost = blocks[0]
    return assimilate_block(blocks[1:], leftmost)


def rotate_to_single_block(blocks: Blocks) -> Blocks:
    """Rotate an array of blocks until there's just one."""
    while len(blocks) > 1:
        blocks = rotate_blocks(blocks)
    return blocks


def show_blocks(blocks: Blocks, verbose: bool = True) -> None:
    """Show the blocks and their averages."""
    if verbose:
        print("\naverage |\ttrend\n")
    for block in blocks:
        line = ""
        if verbose:
            line += f"{average(block):7.2f} |\t"
        for val in block:
            line += f"{val:2.2f}\t"
        print(line)
