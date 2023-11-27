#!/usr/bin/python3
""" program that solves the N queens problem."""
import sys


def is_safe(board, row, col, n):
    """Function to solve the N-Queens
    problem using backtracking
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i = row
    j = col
    while i < n and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True


def solve(board, col, n, solutions):
    """Function to solve the N-Queens
    problem using backtracking
    """
    if col == n:
        solution = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1
            solve(board, col + 1, n, solutions)
            board[i][col] = 0


def print_solutions(solutions):
    """Function to print the solutions found"""
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
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
    board = [[0 for i in range(n)] for j in range(n)]
    solutions = []
    solve(board, 0, n, solutions)
    print_solutions(solutions)
