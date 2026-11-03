"""Two-player Tic-Tac-Toe in the terminal."""
def winner(b):
    lines = [b[0:3], b[3:6], b[6:9],
             b[0:9:3], b[1:9:3], b[2:9:3],
             b[0:9:4], b[2:7:2]]
    for line in lines:
        if line[0] != " " and line.count(line[0]) == 3:
            return line[0]
    return None

def play():
    board = [" "] * 9
    player = "X"
    while True:
        print("\n" + "\n---+---+---\n".join(
            " | ".join(board[i:i+3]) for i in (0, 3, 6)))
        try:
            move = int(input(f"{player}, choose cell 1-9: ")) - 1
            if move not in range(9) or board[move] != " ":
                print("Invalid or occupied cell."); continue
        except ValueError:
            print("Enter a number."); continue
        board[move] = player
        if winner(board):
            print(player, "wins!"); break
        if " " not in board:
            print("Draw!"); break
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    play()
