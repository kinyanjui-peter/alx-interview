#!/usr/bin/env python3
"""
Module for solving the coin change problem using dynamic programming.
"""


def makeChange(coins, total):
    if total < 0:
        return -1

    # Initialize dp array with float('inf') values
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins needed to make amount 0

    # Fill the dp array
    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still float('inf'), it means total cannot be achieved
    return dp[total] if dp[total] != float('inf') else -1


# Test cases
if __name__ == "__main__":
    print(makeChange([1, 2, 25], 37))    # Output: 7
    print(makeChange([1256, 54, 48, 16, 102], 1453))
