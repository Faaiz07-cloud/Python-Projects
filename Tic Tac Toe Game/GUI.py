import tkinter as tk
from tkinter import messagebox

# --- Game Logic ---
def check_win(board, player):
    win_condition = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    for cond in win_condition:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == player:
            return True
    return False

# --- GUI Version ---
def tic_tac_toe():
    root = tk.Tk()
    root.title("Tic Tac Toe")
    root.resizable(False, False)
    root.config(bg="#ffffff")

    board = [" "] * 9
    player = ["X"]

    buttons = []

    # --- Labels ---
    title_label = tk.Label(root, text="🎮 Tic Tac Toe", font=("Arial", 20, "bold"), bg="#ffffff", fg="#333333")
    title_label.grid(row=0, column=0, columnspan=3, pady=10)

    turn_label = tk.Label(root, text="Player X's Turn", font=("Arial", 14), bg="#ffffff", fg="green")
    turn_label.grid(row=1, column=0, columnspan=3, pady=5)

    def handle_click(i):
        if board[i] != " ":
            return
        board[i] = player[0]

        # set color for X and O
        if player[0] == "X":
            buttons[i].config(text=player[0], state="disabled", disabledforeground="green")
        else:
            buttons[i].config(text=player[0], state="disabled", disabledforeground="blue")

        # check winner
        if check_win(board, player[0]):
            messagebox.showinfo("Game Over", f"🏆 Player {player[0]} wins!")
            root.quit()
            return
        elif " " not in board:
            messagebox.showinfo("Game Over", "🤝 It's a draw!")
            root.quit()
            return

        # switch player
        player[0] = "O" if player[0] == "X" else "X"
        turn_label.config(text=f"Player {player[0]}'s Turn",
                          fg="green" if player[0] == "X" else "blue")

    # --- Buttons Grid ---
    frame = tk.Frame(root, bg="#ffffff")
    frame.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

    for i in range(9):
        btn = tk.Button(frame, text=" ", font=("Arial", 24, "bold"),
                        width=5, height=2, relief="ridge", bg="#f8f8f8",
                        command=lambda i=i: handle_click(i))
        btn.grid(row=i//3, column=i%3, padx=5, pady=5)
        buttons.append(btn)

    root.mainloop()

if __name__ == "__main__":
    tic_tac_toe()
