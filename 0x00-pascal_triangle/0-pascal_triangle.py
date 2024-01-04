#!/usr/bin/python3
"""
Returns a list of lists of intergers
representing the Pascal's triangle of n
or an empty list if (n <= 0)
"""


def pascal_triangle(n):
    """
    Pascal triangle list list
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle
