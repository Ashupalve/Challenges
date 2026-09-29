# Q3. Write a program to rotate a square matrix (2D list) 90 degrees clockwise in place.

def rotate_90(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
    return matrix
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(rotate_90(m))