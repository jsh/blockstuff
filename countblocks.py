#!/usr/bin/env python3
"""Show how number of blocks changes with sequence length."""


import sys
from random import random

import matplotlib.pyplot as plt  # type: ignore
import numpy as np  # type: ignore
import scipy.stats  # type: ignore

from blockstuff import assimilate_block


def lineplot(magnitudes, ntrends):
    """Plot commits against week."""
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


def main():
    """The big enchilada."""
    blocks = []

    magnitudes = int(sys.argv[1])
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
