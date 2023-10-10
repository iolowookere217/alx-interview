#!/usr/bin/python3
"""a method that calculates the fewest number of operations
    needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    H = 1
    lnt_copiedH = 0
    min_ops = 0

    while H < n:
        if n % H == 0:
            min_ops += 2
            lnt_copiedH = H
            H *= 2
        else:
            min_ops += 1
            H += lnt_copiedH

    return min_ops



