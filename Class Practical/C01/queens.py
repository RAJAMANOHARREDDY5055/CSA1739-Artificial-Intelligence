
N = 8

def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False

        if col - (row - i) >= 0 and board[i][col - (row - i)]:
            return False

        if col + (row - i) < N and board[i][col + (row - i)]:
            return False

    return True

def solve(board, row):
    if row == N:
        return True

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = True

            if solve(board, row + 1):
                return True

            board[row][col] = False

    return False

board = [[False] * N for _ in range(N)]

if solve(board, 0):
    print("Solution:")
    print_board(board)
else:
    print("No solution found")
