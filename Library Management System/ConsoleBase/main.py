# ----- Library Management System -----

# Modules
import os
import json

# File Name
File_Name = "library.json"

# ----- File Handling Functions -----

# Load Books
def load_books():
    if os.path.exists(File_Name):
        with open(File_Name, "r") as file:
            return json.load(file)
    return []

# Save Books
def save_books(books):
    with open(File_Name, "w") as file:
        json.dump(books, file, indent=4)

# ----- Helper Functions -----

# Generate ID
def generate_id(books):
    if not books:
        return 1 # if list is empty then id becomes 1
    else:
        max_id = max(book["id"] for book in books) + 1
        return max_id

# Find Books by ID
def find_books_by_id(books, book_id):
    if books:
        for book in books:
            if book["id"] == book_id:
                return book
    return None

# Search Books
def search_books(books, details):
     details = details.lower()
     return [
         book for book in books
         if details in book["title"].lower() or details in book["author"].lower()
     ]

# ----- Main Functions -----

# Add Books
def add_book(books):
    title = input("Enter book title: ").strip()
    author = input("Enter book author: ").strip()
    if not title or not author:
        print("\nInvalid input! Both fields required.\n")
        return main
    new_book = {
        "id": generate_id(books),
        "title": title,
        "author": author,
        "status" : "Available"
    }
    books.append(new_book)
    save_books(books)
    print("\nBook added successfully!\n")

# Issue Books
def issue_book(books):
    print("\nBooks List")
    for book in books:
        print(f'{book["id"]} | {book["title"]} | {book["author"]} | {book["status"]}')
    print("------------------------\n")

    try:
        book_id = int(input("Enter book id to issue: ").strip())
    except ValueError:
        print("\nInvalid ID! Please try again.\n")
        return
    book = find_books_by_id(books, book_id)
    if not book:
        print("\nBook not found!\n")
    elif book["status"] == "Issued":
        print("\nBook already issued!\n")
    else:
        book["status"] = "Issued"
        save_books(books)
        print("\nBook issued successfully!\n")

# Return Books
def return_book(books):
    print("\nBooks List")
    for book in books:
        print(f'{book["id"]} | {book["title"]} | {book["author"]} | {book["status"]}')
    print("----------------------\n")

    try:
        book_id = int(input("Enter book id to return: ").strip())
    except ValueError:
        print("\nInvalid ID! Please try again.\n")
        return
    book = find_books_by_id(books, book_id)
    if not book:
        print("\nBook not found!\n")
    elif book["status"] == "Available":
        print("\nBook already returned!\n")
    else:
        book["status"] = "Available"
        save_books(books)
        print("\nBook returned successfully!\n")

# Search Books
def search_books_main(books):
    details = input("Enter book title/auther to search: ").strip()
    result = search_books(books, details)
    if not result:
        print("\nBook not found!\n")
    else:
        for book in result:
            print(f'{book["id"]} | {book["title"]} | {book["author"]} | {book["status"]}')

# Display Books
def display_books(books):
    if not books:
        print("\nNo books found!\n")
    else:
        print("\nAvailable books:\n")
        for book in books:
            print(f'{book["id"]} | {book["title"]} | {book["author"]} | {book["status"]}')
        print("----------------------\n")

# Menu
def main():
    books = load_books()
    print(" ----- Library Management System -----")
    while True:
        print("\nLibrary Menu")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Search Book")
        print("5. Display All Books")
        print("6. Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            add_book(books)
        elif choice == "2":
            issue_book(books)
        elif choice == "3":
            return_book(books)
        elif choice == "4":
            search_books_main(books)
        elif choice == "5":
            display_books(books)
        elif choice == "6":
            print("\nExiting... Goodbye!\n")
            break
        else:
            print("\nInvalid choice! Please enter 1–6.\n")

# Run
try:
   if __name__ == "__main__":
        main()
except KeyboardInterrupt:
    print("\n\nExiting... Goodbye!\n")