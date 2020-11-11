#!/usr/bin/env python3
"""Manipulate trends of reals."""

import statistics
from copy import deepcopy
from typing import List

Block = List[float]
Blocks = List[Block]


def average(seq: Block) -> float:
    """An average."""
    return statistics.fmean(seq)


def increasing_trend(old_block: Block, new_block: Block) -> bool:
    """Merging preserves an increasing trend."""
    return average(old_block) < average(new_block)


def decreasing_trend(old_block: Block, new_block: Block) -> bool:
    """Merging preserves decreasing trend."""
    return average(old_block) > average(new_block)


def always(old_block: Block, new_block: Block) -> bool:
    """Always merge."""
    return True


def never(old_block: Block, new_block: Block) -> bool:
    """Never merge."""
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


def show_blocks(blocks: Blocks) -> None:
    """Show the blocks and their averages."""
    for block in blocks:
        line = f"{average(block):4.2f} |\t"
        for val in block:
            line += f"{val:4.2f}\t"
        print(line)
