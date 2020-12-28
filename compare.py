#!/usr/bin/python3

COMPARITOR = int.__lt__


def cmp(first, second, comparitor=COMPARITOR):
    return comparitor(first, second)


print(cmp(2, 3))
print(cmp(3, 2))
print(cmp(3, 2, int.__gt__))
