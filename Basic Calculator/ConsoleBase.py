# Basic Calculator

# functions for add, sub, mul, div
def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    return num1 / num2

# Main function
def calculator():
    print("\n------- Basic Calculator -------")
    while True:
        try:
            num1 = input("Enter the first number: ")
            if num1 == "q":
                print("\nThank you for using calculator")
                exit()
            num1 = int(num1)
            num2 = input("Enter the second number: ")
            if num2 == "q":
                print("\nThank you for using calculator")
                exit()
            num2 = int(num2)
        except ValueError:
            print("\nInvalid input. Please try again.")
            continue
        while True:
            operation = input("\nChoose an operation: +-*/ ")
            if operation == "+":
                result = add(num1, num2)
                print(f"\n------{num1} + {num2} = {result}------\n")
                break
            elif operation == "-":
                result = sub(num1, num2)
                print(f"\n------{num1} - {num2} = {result}------\n")
                break
            elif operation == "*":
                result = mul(num1, num2)
                print(f"\n------{num1} * {num2} = {result}------\n")
                break
            elif operation == "/":
                result = div(num1, num2)
                print(f"\n------{num1} / {num2} = {result}------\n")
                break
            else:
                print("\nInvalid operator. Please try again.")
                continue

try:
    calculator()
except KeyboardInterrupt:
    print("\nThank you for using calculator")


