#!/usr/bin/env pypy3
"""Show how number of blocks changes with sequence length."""

import argparse
import random
import statistics
import sys
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
    length = args.length
    trials = args.trials
    numblocks_dict = (
        {}
    )  # numblocks_dict{3} is the number of trials that produced 3 blocks
    # -- useful for graphing
    numblocks_list = (
        []
    )  # numblocks_list[3] is the number of blocks produced in the fourth trial
    # -- useful for statistics
    for _ in range(trials):
        blocks = []
        for _ in range(length):
            blocks = assimilate_block(blocks, [random.uniform(0, 1)])  # nosec
        numblocks = len(blocks)
        numblocks_list.append(numblocks)
        if numblocks not in numblocks_dict:
            numblocks_dict[numblocks] = 0
        numblocks_dict[numblocks] += 1

    if args.verbose:
        try:
            print(f"mode(# of blocks), {statistics.mode(numblocks_list)}")
        except Exception:
            print("no single mode")
        print(f"median(# of blocks), {statistics.median(numblocks_list)}")
        print(f"mean(# of blocks), {statistics.mean(numblocks_list)}")
        print(f"variance(# of blocks), {statistics.variance(numblocks_list)}")

    if args.verbose:
        print("\nnumber of blocks\ttimes seen\n")

    for key in sorted(numblocks_dict.keys()):
        print(f"{key:15}\t\t{numblocks_dict[key]:10}")


if __name__ == "__main__":
    main()
