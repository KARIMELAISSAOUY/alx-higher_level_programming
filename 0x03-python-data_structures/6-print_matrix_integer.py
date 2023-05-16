#!/usr/bin/python3
# 6-print_matrix_integer.py
def print_matrix_integer(matrix=None):
    if matrix is None:
        matrix = [[]]

    for row in matrix:
        print(" ".join(str(col) for col in row))

