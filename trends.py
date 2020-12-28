#!/usr/bin/env pypy3
"""Manipulate increasing trends of reals."""

from copy import deepcopy

from trend import Trend
from values import average


class Trends:
    def __init__():
        values

    def assimilate_trend(trends: "Trends", new_trend: Trend) -> "Trends":
        """Assimilate new trend into old using criterion meldable."""
        trends = deepcopy(trends)  # don't modify the original
        if not trends:
            return [new_trend]
        trend = trends.pop()
        if not trend < new_trend:
            return trends + [trend, new_trend]
        trend = trend + new_trend
        return assimilate_trend(trends, trend)

    def decompose_into_trends(elems: Trend) -> "Trends":
        """Break a sequence into trends."""
        trends: "Trends" = []
        for elem in elems:
            trends = assimilate_trend(trends, [elem])  # nosec
        return trends

    def rotate_trends(trends: "Trends") -> "Trends":
        """
        Shift off the leading, leftmost trend,
        then push it onto the right end, assimilating as needed.
        """
        leftmost = trends[0]
        return assimilate_trend(trends[1:], leftmost)

    def rotate_to_single_trend(trends: "Trends") -> "Trends":
        """Rotate an array of trends until there's just one."""
        while len(trends) > 1:
            trends = rotate_trends(trends)
        return trends

    def show_trends(trends: "Trends", verbose: bool = True) -> None:
        """Show the trends and their averages."""
        if verbose:
            print("\naverage |\ttrend\n")
        for trend in trends:
            line = ""
            if verbose:
                line += f"{average(trend):7.2f} |\t"
            for val in trend:
                line += f"{val:2.2f}\t"
            print(line)
