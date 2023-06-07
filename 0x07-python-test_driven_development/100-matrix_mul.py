#!/usr/bin/python3

def validate_matrix(matrix):
    if not isinstance(matrix, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if len(matrix) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")


def matrix_mul(m_a, m_b):
    validate_matrix(m_a)
    validate_matrix(m_b)

    rows_a = len(m_a)
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    cols_b = len(m_b[0])

    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

