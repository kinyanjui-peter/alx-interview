#!/usr/bin/env python3
"""
N queens puzzle solution using backtracking algorithm
"""

import sys


def is_safe(board, row, col, n):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i]:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j]:
            return False

    return True


def solve_n_queens_util(board, col, n):
    """
    Utility function to solve N queens problem
    """
    # If all queens are placed, return true
    if col >= n:
        return True

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # Recur to place rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # If placing queen in board[i][col] doesn't lead to a solution, then remove queen from board[i][col]
            board[i][col] = 0

    # If queen can't be placed in any row in this column, then return false
    return False


def solve_n_queens(n):
    """
    Solve the N queens problem
    """
    # Initialize board
    board = [[0 for _ in range(n)] for _ in range(n)]

    # Start recursion from the first column
    if not solve_n_queens_util(board, 0, n):
        return False

    return board


def print_board(board):
    """
    Print the board
    """
    for row in board:
        print(row)


def main():
    """
    Main function
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve N queens problem
    board = solve_n_queens(n)

    # Print solutions
    if not board:
        print("No solution found")
    else:
        for solution in board:
            print(solution)


if __name__ == "__main__":
    main()
