#!/usr/bin/env python3
"""Show how number of blocks changes with sequence length."""

import argparse
import sys
from random import random
from typing import List, Optional

import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore
import scipy.stats  # type: ignore

from blockstuff import assimilate_block


def lineplot(magnitudes, ntrends):
    """Plot # of trends against log(sequence length)."""
    slope, intercept, rvalue, pvalue, stderr = scipy.stats.linregress(
        magnitudes, ntrends
    )
    line = (
        f"Regression line: y={slope:.2f}x+{intercept:.2f}, "
        f"r^2={rvalue**2:.2f}, p={pvalue:.2f}, e={stderr:.2f}"
    )
    plt.style.use("ggplot")
    _, axes = plt.subplots()
    axes.plot(magnitudes, ntrends, linewidth=0, marker=".", label="observed")
    axes.plot(magnitudes, intercept + slope * magnitudes, label=line)
    axes.set_xlabel("log(sequence length)")
    axes.set_ylabel("number of trends")
    axes.legend(facecolor="white")
    plt.show()


def parse_args(args: Optional[List] = None) -> argparse.Namespace:
    """Parse the args
    :param str description: description message for executable
    :param list or None args: the argument list to parse
    :returns: the args, massaged and sanity-checked
    :rtype: argparse.Namespace

    When this finishes we return a Namespace that has these attributes
      - verbose: how chatty to be (bool)
      - max_magnitude: largest power of 2 to use for a length.
    """

    parser = argparse.ArgumentParser(
        description="Plot block count against log(sequence length)."
    )

    parser.add_argument("--verbose", help="be extra chatty", action="store_true")
    parser.add_argument(
        "--max_magnitude", help="largest power of 2 to use for length", type=int
    )

    if args is None:
        args = []
    parsed_args = parser.parse_args(args)
    if parsed_args.verbose:
        print(parsed_args, file=sys.stderr)

    return parsed_args


def main():
    """The big enchilada."""
    blocks = []

    args = parse_args()
    magnitudes = args.max_magnitude
    numblocks = [0] * magnitudes
    for magnitude in range(magnitudes):
        size = 2 ** magnitude
        for _ in range(size):
            blocks = assimilate_block(blocks, [random()])  # nosec
        numblocks[magnitude] = len(blocks)
        print(f"size: {size}, blocks: {numblocks[magnitude]}")
    logsizes = np.arange(0, len(numblocks))
    ntrends = np.array(numblocks)
    lineplot(logsizes, ntrends)


if __name__ == "__main__":
    main()
