#!/usr/bin/python3

import sys
if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)

if N < 4:
    print('N must be at least 4')
    sys.exit(1)

def is_safe(board, row, col):
    for i in range(col):
        if board[i] == row or board[i] == row - (col - i) or board[i] == row + (col - i):
            return False
    return True

def solve(board, col, solutions):
    if col == N:
        solutions.append(board[:])
        return
    for row in range(N):
        if is_safe(board, row, col):
            board[col] = row
            solve(board, col + 1, solutions)

solutions = []
solve([0] * N, 0, solutions)

for solution in solutions:
    print([[row, solution[row]] for row in range(N)])
