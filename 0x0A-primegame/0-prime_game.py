#!/usr/bin/python3
"""Module for solving the prime game question."""


def isWinner(x, nums):
    """
    Determine the winner of the prime game.

    Parameters:
    x (int): Number of rounds.
    nums (list): List of integers representing the
    upper limits of numbers in each round.

    Returns:
    str: Name of the player who wins the most rounds
    ("Maria" or "Ben"), or None if it's a tie.
    """
    if not nums or x < 1:
        return None

    max_limit = max(nums)
    # Find the maximum number in nums to determine the
    # range for the sieve

    # Initialize a list for the sieve of Eratosthenes
    sieve = [True] * (max(max_limit + 1, 2))

    # Implement the sieve of Eratosthenes to find all prime
    # numbers up to max_limit
    for start in range(2, int(pow(max_limit, 0.5)) + 1):
        if not sieve[start]:
            continue
        for multiple in range(start * start, max_limit + 1, start):
            sieve[multiple] = False

    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    prime_count = 0  # Counter for the number of primes
    for index in range(len(sieve)):
        if sieve[index]:
            prime_count += 1
        sieve[index] = prime_count
        # Store the cumulative count of primes up to each index

    maria_wins = 0  # Counter for the number of rounds Maria wins
    for round_limit in nums:
        maria_wins += sieve[round_limit] % 2 == 1
        # Maria wins if the number of primes is odd

    total_rounds = len(nums)
    if maria_wins * 2 == total_rounds:
        return None  # It's a tie
    if maria_wins * 2 > total_rounds:
        return "Maria"  # Maria wins more rounds
    return "Ben"  # Ben wins more rounds
