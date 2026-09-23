# Q3. Write a program to solve the N-Queens problem for a given N and print one valid solution.

def solve_n_queens(n):
    board = [-1] * n
    def is_safe(row, col):
        for r in range(row):
            if board[r] == col or abs(board[r] - col) == abs(r - row):
                return False
        return True
    def place_queen(row):
        if row == n:
            return True
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                if place_queen(row + 1):
                    return True
                board[row] = -1
        return False
    if place_queen(0):
        for row in board:
            line = ["."] * n
            line[row] = "Q"
            print(" ".join(line))
    else:
        print("No solution")
solve_n_queens(4)
