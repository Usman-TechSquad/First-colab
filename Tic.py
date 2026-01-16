# Tic Tac Toe Game

board = [" " for _ in range(9)]

def print_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner(player):
    win_conditions = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw():
    return " " not in board

current_player = "X"

print("Welcome to Tic Tac Toe!")
print("Positions are from 1 to 9")
print_board()

while True:
    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

    if board[move] != " ":
        print("That position is already taken. Try again.")
        continue

    board[move] = current_player
    print_board()

    if check_winner(current_player):
        print(f"🎉 Player {current_player} wins!")
        break

    if is_draw():
        print("🤝 It's a draw!")
        break

    current_player = "O" if current_player == "X" else "X"
