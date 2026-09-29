# Q1. Write a program to implement matrix multiplication of two 2D lists (matrices) from scratch.


def matrix_multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    if cols_A != rows_B:
        raise ValueError("Incompatible matrix dimensions")
    result = [[0] * cols_B for _ in range(rows_A)]
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    return result
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print(matrix_multiply(A, B))