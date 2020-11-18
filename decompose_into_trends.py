#!/usr/bin/env pypy3
"""Decompose a sequence of reals into increasing trends."""

import argparse
import random
import sys
from typing import List, Optional

from blockstuff import decompose_into_blocks, random_block, show_blocks


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

    parser = argparse.ArgumentParser(description="Decompose sequence.")

    parser.add_argument("--verbose", help="be extra chatty", action="store_true")
    parser.add_argument("--length", help="How long a sequence to decompose", type=int)

    if args is None:
        args = []
    parsed_args = parser.parse_args(args)
    if parsed_args.verbose:
        print(parsed_args, file=sys.stderr)

    return parsed_args


def main():
    """The big enchilada."""
    args = parse_args(sys.argv[1:])
    seq = random_block(args.length, random.gauss, 0, 1)
    blocks = decompose_into_blocks(seq)
    show_blocks(blocks, args.verbose)


if __name__ == "__main__":
    main()
