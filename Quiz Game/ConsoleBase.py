# Quiz Game

# list of dictionaries (quiz, options, answers)
quiz = [
    {"q": "2+2?", "options": ["2", "3", "4", "5"], "answer": "4"},
    {"q": "Capital of France?", "options": ["Paris", "Rome", "Berlin", "Madrid"], "answer": "Paris"},
    {"q": "Largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
    {"q": "5 * 6 = ?", "options": ["11", "30", "56", "26"], "answer": "30"},
    {"q": "Which gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "answer": "Carbon Dioxide"},
    {"q": "Fastest land animal?", "options": ["Tiger", "Cheetah", "Horse", "Lion"], "answer": "Cheetah"},
    {"q": "H2O is chemical formula of?", "options": ["Oxygen", "Water", "Hydrogen", "Salt"], "answer": "Water"},
    {"q": "Square root of 81?", "options": ["9", "8", "7", "6"], "answer": "9"},
    {"q": "Which continent is Egypt in?", "options": ["Asia", "Europe", "Africa", "South America"], "answer": "Africa"},
    {"q": "National language of Pakistan?", "options": ["Urdu", "Punjabi", "Sindhi", "English"], "answer": "Urdu"}
]

# title
print(f"\n>>>>>>>>>>>>>>>>>>>> Quiz Game <<<<<<<<<<<<<<<<<<<<\n")

# variable that count correct answers score
score = 0

# for loop for displaying quiz
for i,question in enumerate(quiz, start=1):
    print(f"Quiz {i}: {question['q']}")
    for j, option in enumerate(question['options'], start=1):
        print(f"{j}. {option}")
    user = input("\nEnter your Answer >>> : ")
    if user.strip().lower() == question['answer'].strip().lower():
        print(f"\n---------- {user} is a correct answer! ----------\n")
        score += 1
    else:
        print(f"---------- {user} is incorrect answer! ----------")
        print(f"---------- Correct answer: '{question['answer']}' ----------\n")

# displaying score
print(f"\n You got {score} out of {len(quiz)} questions!.")

