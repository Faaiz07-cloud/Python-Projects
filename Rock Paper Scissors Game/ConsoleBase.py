# Rock Paper Scissors Game

import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def decide_winner(user, computer):
    if user == computer:
        return "It's a Draw!"
    elif ((user == "Paper" and computer == "Rock")
                        or
         (user == "Rock" and computer == "Scissors")
                        or
         (user == "Scissors" and computer == "Paper")):
            return "You wins"
    else:
        return "Computer wins"

def play():
    print("Welcome to the Rock Paper Scissors Game!\n")
    while True:
     user_choice = input("Please enter your choice: Rock, Paper, Scissors or Quit ")
     if user_choice == "Quit":
         print("Thanks for playing!")
         break
     elif user_choice not in ["Rock", "Paper", "Scissors"]:
         print("Invalid Choice: Please try again.\n")
         continue
     computer_choice = get_computer_choice()
     print(f"Computer Chooses: {computer_choice}")
     decision = decide_winner(user_choice, computer_choice)
     print(decision)
     print("_" * 30)

play()


