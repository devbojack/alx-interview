#!/usr/bin/python3
"""Minimum Operations: Copy All and Paste"""


def minOperations(n):
    """Returns the fewest number of operations needed
    to result in exactly n H characters
    """
    if n < 0:
        return 0

    total_operations = 0
    evens = 2

    while evens <= n:
        if n % evens == 0:
            total_operations += evens
            n = n / evens
            evens -= 1
        evens += 1

    return total_operations
