import tkinter as tk
import random

# -------------------------------- Backend ----------------------------
def generate_number():
    return random.randint(1, 100)

random_number = generate_number()
attempts = 0

def process():
    global attempts
    user_guess = entry.get()
    if not user_guess.isdigit():
        hint.configure(text="Please enter a number. 1-100")
        return

    user_guess = int(user_guess)
    attempts += 1

    if user_guess < random_number:
        hint.configure(text="Too Low")
    elif user_guess > random_number:
        hint.configure(text="Too High")
    else:
        result.configure(text="Yippie You win!!")
        rand_number.configure(text=f"The number was: {random_number}")
        attempts_num.configure(text=f"You guessed it in {attempts} attempts.")

# ----------------------------- GUI ----------------------------------
root = tk.Tk()
root.title("Number Guessing Game")
root.configure(bg="#7c57b4")
root.geometry("925x533")
root.resizable(False, False)

frame = tk.Frame(root, bg="#f1f1fb", width=450, height=400)
frame.pack(expand=True)
frame.propagate(False)

title = tk.Label(frame, text="Number Guessing Game", font=("Trebuchet MS", 20, "bold"), fg="#2c2b30", bg="#f1f1fb")
title.pack(pady=(20,0))

description = tk.Label(frame, text="Guess the number between 1-100.", font=("Arial", 11, "bold"), fg="#89888e", bg="#f1f1fb")
description.pack(pady=(16,0))

entry = tk.Entry(frame, width=7, font=("Arial", 20), justify="center")
entry.pack(pady=(27,0))

button = tk.Button(frame, text="GUESS", font=("Trebuchet MS", 10, "bold"),
                   width=12, height=2, bg="#663397", fg="#ffffff",
                   relief="ridge", activebackground="#452175", activeforeground="#ffffff", command=process)
button.pack(pady=(26,0))

hint = tk.Label(frame, text="", font=("Arial", 11, "bold"), fg="#89888e", bg="#f1f1fb")
hint.pack(pady=(20,0))

result = tk.Label(frame, text="", font=("Arial", 11, "bold"), fg="#89888e", bg="#f1f1fb")
result.pack(pady=(6,0))

rand_number = tk.Label(frame, text="", font=("Arial", 11, "bold"), fg="#89888e", bg="#f1f1fb")
rand_number.pack(pady=(6,0))

attempts_num = tk.Label(frame, text="", font=("Arial", 11, "bold"), fg="#89888e", bg="#f1f1fb")
attempts_num.pack(pady=(6,0))

root.mainloop()