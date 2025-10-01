# Word Frequency Counter Program

import os

file_name = input("Enter file name: eg. data.txt--- ")

lines = [
     "Welcome to our platform!",
    "Here, you can explore new features,",
    "connect with your friends,",
    "and manage your profile with just a few clicks.",
    "Don't forget to check your notifications",
    "and keep your settings up to date."
]

if not os.path.isfile(file_name):
    with open(file_name, "w") as file:
        for line in lines:
            file.write(line + "\n")
        print(f"\n{file_name} successfully created!")

else:
    print("\nFile already exists.")


if os.path.exists(file_name):
    with open(file_name, "r") as file:
        content = file.read()

word_count = {}

for word in content.split():
    word = word.lower().strip('<>.,/?()&*$#%^@#!{}[]')
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord Count:")
for key, value in word_count.items():
    print(f"{key}: {value}")