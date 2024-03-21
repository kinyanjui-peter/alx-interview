#!/usr/bin/python 3
""" finding the minimum number of oprations
"""
def minOperations(n):
    if n <= 1:
        return n
    # Initialize an array to store the minimum number of operations
    minNumber = [0] * (n + 1)
    # Since we can't achieve 0 or 1 'H' characters, we start from 2
    for i in range(2, n + 1):
        minNumber[i] = float('inf')  # Initialize to infinity
        # Try all possible factors of i to find the minimum operations
        for j in range(1, i):
            if i % j == 0:
                minNumber[i] = min(minNumber[i], minNumber[j] + i // j)
    return minNumber[n]
