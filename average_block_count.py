#!/usr/bin/env pypy3
"""Average number of blocks in a sequence of a given length."""


import argparse
import sys
from random import random
from typing import List, Optional

from blockstuff import assimilate_block


def parse_args(args: Optional[List] = None) -> argparse.Namespace:
    """Parse the args
    :param str description: description message for executable
    :param list or None args: the argument list to parse
    :returns: the args, massaged and sanity-checked
    :rtype: argparse.Namespace

    When this finishes we return a Namespace that has these attributes
      - verbose: how chatty to be (bool)
      - length: sequence length
      - trials: number of trials
    """

    parser = argparse.ArgumentParser(
        description="Average # of blocks over several trials."
    )

    parser.add_argument("--verbose", help="be extra chatty", action="store_true")
    parser.add_argument("--length", help="How long a sequence to decompose", type=int)
    parser.add_argument("--trials", help="How many trials to run", type=int)

    if args is None:
        args = []
    parsed_args = parser.parse_args(args)
    if parsed_args.verbose:
        print(parsed_args, file=sys.stderr)

    return parsed_args


def main():
    """The big enchilada."""

    args = parse_args(sys.argv[1:])
    cumulative_numblocks = 0
    for _ in range(args.trials):
        blocks = []
        for _ in range(args.length):
            blocks = assimilate_block(blocks, [random()])  # nosec
        cumulative_numblocks += len(blocks)
    header = "average number of blocks:\t" if args.verbose else ""
    print(f"{header}{cumulative_numblocks/args.trials}")


if __name__ == "__main__":
    main()
