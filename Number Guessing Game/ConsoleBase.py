# Number Guessing Game

import random

# function for generating numbers
def generate_number():
    return random.randint(1, 100)

# main function
def play():
    number = generate_number()
    attempts = 0
    while True:
      user_guess = int(input("Guess a number between 1 and 100: "))
      if user_guess < number:
          print("Too Low")
      elif user_guess > number:
          print("Too High")
      elif user_guess == number:
          print("Correct")
          break
      attempts += 1
    print(f"You guessed in {attempts} attempts")

try:
    play()
except KeyboardInterrupt:
    print("\nBye")

