# Even - Odd range splitter

# empty lists for even and odd numbers
even_numbers = []
odd_numbers = []

# Ask the user for the start and end of the range
start = int(input("Enter Start Number: "))
end = int(input("Enter End Number: "))

# using for loop
for i in range(start, end + 1): #end+1 is used because range() excludes the last number
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

# Printing even and odd numbers in lists
print("Even Numbers: ", even_numbers)
print("Odd Numbers: ", odd_numbers)