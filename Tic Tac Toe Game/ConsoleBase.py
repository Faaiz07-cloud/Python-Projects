# Tic Tac Toe Game
def display_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print(f"--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print(f"--+--+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_win(board, player):
    win_condition = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
        [0, 4, 8], [2, 4, 6]             # diagonal
    ]
    for condition in win_condition:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def tic_tac_toe():
    print("\nWelcome to Tic Tac Toe!")
    board = [" "]*9
    player = "X"

    for turn in range(9):
        display_board(board)
        print(f"{player}'s turn:")
        while True:
            try:
                move = int(input("Choose a move: (1-9) ")) -1
                if move < 0 or move > 8:
                    print("❌ Please enter a number between 1–9.")
                elif board[move] != " ":
                    print("❌ That spot is already taken. Try again.")
                else:
                    break
            except ValueError:
                print("❌ Please enter a number between 1–9.")
        board[move] = player

        if check_win(board, player):
            display_board(board)
            print(f"\n🏆 {player} wins the game!")
            return
        # switch player
        if player == "X":
            player = "O"
        else:
            player = "X"

    display_board(board)
    print(f"\n🤝 It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()