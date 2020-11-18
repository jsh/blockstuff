#!/usr/bin/env python3
"""
Create a sequence,
break it into trends,
then rotate it until it's a single trend.
"""

import argparse
import random
import sys
from typing import List, Optional

from blockstuff import decompose_into_blocks, random_block, rotate_blocks


def parse_args(args: Optional[List] = None) -> argparse.Namespace:
    """Parse the args
    :param str description: description message for executable
    :param list or None args: the argument list to parse
    :returns: the args, massaged and sanity-checked
    :rtype: argparse.Namespace

    When this finishes we return a Namespace that has these attributes
      - verbose: how chatty to be (bool)
      - length: sequence length
    """

    parser = argparse.ArgumentParser(
        description="Decompose a sequence, then rotate until it is a single trend."
    )

    parser.add_argument("--verbose", help="be extra chatty", action="store_true")
    parser.add_argument("--length", help="How long a sequence to use.", type=int)
    parser.add_argument("--trials", help="How many trials to run", type=int)

    if args is None:
        args = []
    parsed_args = parser.parse_args(args)
    if parsed_args.verbose:
        print(parsed_args, file=sys.stderr)

    return parsed_args


def main() -> None:
    """The big enchilada."""
    blocks = []

    args = parse_args(sys.argv[1:])
    for _ in range(args.trials):
        seq = random_block(args.length, random.gauss, 0, 1)
        blocks = decompose_into_blocks(seq)
        nbreaks = len(blocks) - 1
        initial_breaks = nbreaks
        rotations = 0
        while nbreaks:
            block_sizes = [len(block) for block in blocks]
            if args.verbose:
                print(f"{nbreaks} | {block_sizes}")
            blocks = rotate_blocks(blocks)
            rotations += 1
            nbreaks = len(blocks) - 1
        block_sizes = [len(block) for block in blocks]
        if args.verbose:
            print(f"{nbreaks} | {block_sizes}")
            print(f"initial breaks: {initial_breaks}\trotations: {rotations}")
        else:
            print(f"{initial_breaks}\t{rotations}")


if __name__ == "__main__":
    main()
