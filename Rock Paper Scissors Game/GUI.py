import tkinter as tk
import random

# ---------------------------- back-end functions --------------------------------------
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def decide_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a Draw"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
         return "You Win "
    else:
        return "Computer Wins "

def play(user_choice):
    computer_choice = get_computer_choice()
    computer_label.config(text=f"Computer Chooses: {computer_choice}")
    decision = decide_winner(user_choice, computer_choice)
    result_label.config(text=f"Result: {decision}", highlightthickness=2, highlightbackground="#009688")

# ---------------------------------- GUI -------------------------------------------
root = tk.Tk()

root.geometry("600x500")
root.title("Rock Paper Scissors Game")
root.resizable(False, False)
root.config(bg="#ffefd5")

# main title
main_title = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 25, "bold") )
main_title.config(bg="#ffefd5", fg="#e91e63", highlightthickness=2, highlightbackground="#e91e63")
main_title.pack(pady=(25,0))

# choose title
choose_title = tk.Label(root, text="Choose Your Option ",  font=("Arial", 19, "bold"))
choose_title.config( bg="#ffefd5", fg="#ff9800")
choose_title.pack(pady=(35,0))

# buttons frame
frame_buttons = tk.Frame(root, bg="#ffefd5")
frame_buttons.pack(pady=10)

button_style = {
    "font": ("Arial" , 15 , "bold"),
    "relief": "ridge",
    "width" : 11,
    "height": 2
}

rock_button = tk.Button(frame_buttons, text="Rock", **button_style, command=lambda: play("Rock"))
rock_button.config(bg="#ff5722", fg="white", activebackground="#e64a19")
rock_button.grid(row=0, column=0, padx=10, pady=(25,0))

paper_button = tk.Button(frame_buttons, text="Paper", **button_style,  command=lambda: play("Paper"))
paper_button.config(bg="#4caf50", fg="white", activebackground="#388e3c")
paper_button.grid(row=0, column=1, padx=10, pady=(25,0))

scissors_button = tk.Button(frame_buttons, text="Scissors", **button_style,  command=lambda: play("Scissors"))
scissors_button.config(bg="#2196f3", fg="white", activebackground="#1976d2")
scissors_button.grid(row=0, column=2, padx=10, pady=(25,0))

# computer choice label
computer_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 17, "bold"))
computer_label.config(bg="#ffefd5", fg="#3f51b5")
computer_label.pack(pady=(20,0))

# result label
result_label = tk.Label(root, text="", font=("Arial", 24, "bold"))
result_label.config(bg="#ffefd5", fg="#009688")
result_label.pack(pady=(30,0))

# quit button
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.config(bg="#d32f2f", fg="white", activebackground="#b71c1c", font=("Arial", 11, "bold"),
                   relief="ridge", width= 10, height= 2)
quit_button.pack(pady=(30,0))

root.mainloop()
