#!/usr/bin/env python3
"""
Create a sequence,
break it into trends,
then rotate it until it's a single trend.
Next, flip it around
decompose into trends,
and report the number of trends.
"""

import argparse
import random
import sys
from typing import List, Optional

from blockstuff import (
    decompose_into_blocks,
    decreasing_trend,
    random_block,
    rotate_to_single_block,
)


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
    number_of_backwards_trends = 0
    for _ in range(args.trials):
        # generate a random *single* trend of length args.length
        seq = random_block(args.length, random.gauss, 0, 1)
        blocks = decompose_into_blocks(seq)
        block = rotate_to_single_block(blocks)[0]
        # and decompose it in the opposite direction
        reverse_blocks = decompose_into_blocks(block, decreasing_trend)
        number_of_backwards_trends += len(reverse_blocks)
        if args.verbose:
            print(f"seq: {seq}")
            print(f"blocks: {blocks}")
            print(f"trend: {block}")
            print(f"backwards trends: {reverse_blocks}")
    if args.verbose:
        print(
            f"length: {args.length}, "
            f" mean backwards trends: {number_of_backwards_trends/args.trials:2.2f}"
        )
    else:
        print(f"{number_of_backwards_trends/args.trials:2.2f}")


if __name__ == "__main__":
    main()
