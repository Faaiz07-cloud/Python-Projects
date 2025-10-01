# Contact Book

import os
import json
from logging import exception

Contact_File = "contacts.txt"

#create file if not exits and load contacts
def load_contact():
    if os.path.exists(Contact_File):
        with open(Contact_File,"r") as f:
            return json.load(f)
    return {}

# save contacts
def save_contacts(contacts):
    with open(Contact_File,"w") as f:
        json.dump(contacts,f)

# add contact
def add_contact(contacts):
    name = input("Enter your name: ").strip()
    if name in contacts:
        print("That name is already taken")
    else:
        phone = input("Enter your phone number: ").strip()
        contacts[name] = phone
        print("Contact added!")

# search contact
def search_contact(contacts):
    name = input("Enter your name to search: ").strip()
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact with this name does not exist")

# update contacts
def update_contact(contacts):
    old_name = input("Enter your old name: ").strip()
    if old_name in contacts:
        new_name = input("Enter your new name: ").strip()
        new_phone = input("Enter your new phone number: ").strip()
        del contacts[old_name]
        contacts[new_name] = new_phone
        print("Contact updated!")
    else:
        print("Contact with this name does not exist")

#  delete contact
def delete_contact(contacts):
    name = input("Enter your name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print("Contact deleted!")
    else:
        print("Contact with this name does not exist")

# display contacts
def display_contacts(contacts):
    if contacts:
        print("\nContact List")
        for key, value in contacts.items():
           print(f"{key}: {value}")
    else:
        print("No contacts found")

# Contact Book Display
def main():
    contacts = load_contact()
    while True:
        print("\nWelcome to Contact Book")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")
        choice = (input("Enter your choice: (1-6) "))
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            search_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            display_contacts(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Choose (1-6)")

# call main function
try:
    main()
except KeyboardInterrupt:
    print(f"\nExiting...")