# Q4. Write a program to check whether a given matrix is a magic square (row, column, and diagonal
# sums are all equal)

def is_magic_square(matrix):
    n = len(matrix)
    magic_sum = sum(matrix[0])
    for row in matrix:
        if sum(row) != magic_sum:
            return False
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != magic_sum:
            return False
    if sum(matrix[i][i] for i in range(n)) != magic_sum:
        return False
    if sum(matrix[i][n-1-i] for i in range(n)) != magic_sum:
        return False
    return True
m = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
print(is_magic_square(m))