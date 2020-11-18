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

from blockstuff import Blocks, assimilate_block, rotate_blocks


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

    if args is None:
        args = []
    parsed_args = parser.parse_args(args)
    if parsed_args.verbose:
        print(parsed_args, file=sys.stderr)

    return parsed_args


def initial_decomposition(length) -> Blocks:
    """The big enchilada."""
    blocks: Blocks = []

    for _ in range(length):
        blocks = assimilate_block(blocks, [random.gauss(0, 1)])  # nosec
    return blocks


def main() -> None:
    """The big enchilada."""
    blocks = []

    args = parse_args(sys.argv[1:])
    length = args.length
    blocks = initial_decomposition(length)
    print(len(blocks))
    while len(blocks) > 1:
        blocks = rotate_blocks(blocks)
        print(len(blocks))


if __name__ == "__main__":
    main()
