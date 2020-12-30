#!/usr/bin/env pypy3
"""Show how number of blocks changes with sequence length."""

import argparse
import random
import statistics
import sys
from typing import List, Optional

from blockstuff import decompose_into_blocks, random_block


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
    numbreaks_dict = (
        {}
    )  # numbreaks_dict{3} is the number of trials that produced 3 breaks (4 blocks)
    # -- useful for graphing
    numbreaks_list = (
        []
    )  # numbreaks_list[3] is the number of breaks produced in the fourth trial
    # -- useful for statistics
    for _ in range(trials):
        seq = random_block(length, random.gauss, 0, 1)
        blocks = decompose_into_blocks(seq)
        numbreaks = len(blocks) - 1  # blocks the fences, breaks the fenceposts
        numbreaks_list.append(numbreaks)
        if numbreaks not in numbreaks_dict:
            numbreaks_dict[numbreaks] = 0
        numbreaks_dict[numbreaks] += 1

    if args.verbose:
        try:
            print(f"mode(# of breaks), {statistics.mode(numbreaks_list)}")
        except Exception:
            print("no single mode")
        print(f"median(# of breaks), {statistics.median(numbreaks_list)}")
        print(f"mean(# of breaks), {statistics.mean(numbreaks_list)}")
        print(f"variance(# of breaks), {statistics.variance(numbreaks_list)}")
        print(
            "q ~ variance/mean = "
            f"{statistics.variance(numbreaks_list)/statistics.mean(numbreaks_list)}"
        )

    if args.verbose:
        print("\nnumber of breaks\t# of trials seen\n")

    for key in sorted(numbreaks_dict.keys()):
        print(f"{key:15}\t\t{numbreaks_dict[key]:10}")


if __name__ == "__main__":
    main()
