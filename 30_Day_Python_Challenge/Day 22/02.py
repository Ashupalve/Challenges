# Q2. Write a program to transpose a matrix (2D list) without using numpy.

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]
m = [[1, 2, 3], [4, 5, 6]]
print(transpose(m))