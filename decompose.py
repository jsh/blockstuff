#!/usr/bin/env python3
"""Decompose a sequence of reals into increasing trends."""

import sys
from random import random

from blockstuff import assimilate_block, show_blocks


def main():
    """The big enchilada."""
    blocks = []

    seq_length = int(sys.argv[1])
    for _ in range(seq_length):
        blocks = assimilate_block(blocks, [random()])  # nosec
    show_blocks(blocks)


if __name__ == "__main__":
    main()
