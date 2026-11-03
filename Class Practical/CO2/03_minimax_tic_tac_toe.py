"""Minimax algorithm for optimal Tic-Tac-Toe play (computer is X)."""
WIN_LINES = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
def result(b):
    for a,c,d in WIN_LINES:
        if b[a] != " " and b[a] == b[c] == b[d]: return b[a]
    return "draw" if " " not in b else None

def minimax(board, maximizing):
    outcome = result(board)
    if outcome == "X": return 1
    if outcome == "O": return -1
    if outcome == "draw": return 0
    scores = []
    for i, cell in enumerate(board):
        if cell == " ":
            board[i] = "X" if maximizing else "O"
            scores.append(minimax(board, not maximizing))
            board[i] = " "
    return max(scores) if maximizing else min(scores)

def best_move(board):
    moves = []
    for i, cell in enumerate(board):
        if cell == " ":
            board[i] = "X"
            moves.append((minimax(board, False), i))
            board[i] = " "
    return max(moves)[1] if moves else None

if __name__ == "__main__":
    b = ["X","O"," "," ","X"," ","O"," "," "]
    move = best_move(b)
    print("Board:", b, "Best move for X:", move + 1 if move is not None else None)
