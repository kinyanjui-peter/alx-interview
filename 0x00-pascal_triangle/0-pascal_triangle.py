#!/usr/bin/python3
"""
Function that prints Pascal's triangle.
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to the nth row."""
    if n <= 0 or not isinstance(n, int):
        # Return an empty list if n is non-positive or not an integer
        return []

    triangle = []
    for row_num in range(n):
        new_row = [1]
        if row_num > 0:
            prev_row = triangle[-1]
            for y in range(1, row_num):
                new_row.append(prev_row[y - 1] + prev_row[y])
            new_row.append(1)
        triangle.append(new_row)
    return triangle


def print_triangle(triangle):
    """Print Pascal's triangle."""
    for row in triangle:
        print(row)
