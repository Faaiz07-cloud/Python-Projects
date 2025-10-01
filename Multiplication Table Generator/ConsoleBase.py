# Multiplication Table Generator
# print("\n----------- Multiplication Table Generator -------------")
# try:
#  while True:
#     user = int(input("Enter a number: "))
#     i = 1
#     print(f"\nTable of {user}:")
#     while i <= 10:
#       print(f"{user} * {i} = {user * i}")
#       i = i + 1
#     print("-----------------------------------------------\n")
# except KeyboardInterrupt:
#     print("\nExiting...")

# -------------------- with file-handling ------------------------------

print("\n------------------- Multiplication Table Generator ----------------------")
try:
 while True:
    user = int(input("Enter a number: "))
    upto = int(input("Print table up to: "))
    print(f"\n------------- Table of {user} ---------------")
    i = 1
    with open("Tables_Record.txt", "a") as file:
        file.write(f"------------- Table of {user} ---------------\n")

        while i <= upto:
            lines = f"{user} x {i} = {user * i}"
            print(lines)
            file.write(lines + "\n")
            i = i + 1
        print("-----------------------------------------------\n")
        file.write("---------------------------------------------\n\n")
except KeyboardInterrupt:
    print("\nProgram Terminated")
