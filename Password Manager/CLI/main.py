# ---------- Password Manager ----------

# Modules
import os

from cryptography import fernet
from cryptography.fernet import Fernet

# Encryption Setup
KEY_FILE = "key.key"
PASSWORD_FILE = "passwords.txt"

# Function to generate encryption key (only once)
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as key_file:
        key_file.write(key)

def load_key():
    with open(KEY_FILE, 'rb') as key_file:
        return key_file.read()

# Check if key exists, otherwise create it
if not os.path.exists(KEY_FILE):
    generate_key()

load_key = load_key()
fernet = Fernet(load_key)

# File I/O + Encryption
def add_password(username, email, password):
    with open(PASSWORD_FILE, "a") as file:
        encrypted_password = fernet.encrypt(password.encode()).decode()
        file.write(f"{username} | {email} | {encrypted_password}\n")
    print("\nPassword saved successfully (encrypted).")

def view_passwords()    :
    if not os.path.exists(PASSWORD_FILE):
        print("\nNo saved passwords yet.")
        return

    with open(PASSWORD_FILE, "r") as file:
         lines = file.readlines()

    print("\nSaved Passwords:\n")
    for line in lines:
        username, email, encrypted_password = line.strip().split(" | ")
        decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
        print(f"{username} | {email} → {decrypted_password}")
    print()
    print("-" * 50)

def delete_password():
     if not os.path.exists(PASSWORD_FILE):
         print("\nNo saved passwords yet.")
         return

     with open(PASSWORD_FILE, "r") as file:
         lines = file.readlines()

     print("\nSaved Passwords:\n")
     for line in lines:
         username, email, encrypted_password = line.strip().split(" | ")
         decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
         print(f"{username} | {email} → {decrypted_password}")
     print()
     print("-" * 50)

     user_input = input("\nDo you want to delete a saved password? (y/n): ")
     if user_input == "y":
         email_ask = input("\nEnter the email of the account you want to delete: ")
         deleted = False
         new_lines = []
         for line in lines:
             username, email, encrypted_password = line.strip().split(" | ")
             if email != email_ask:
                 new_lines.append(line)
             else:
                 deleted = True
         with open(PASSWORD_FILE, "w") as file:
              file.writelines(new_lines)
         if deleted:
              print("\nPassword deleted successfully.")
         else:
                 print(f"\nNo password found for email: {email_ask}")
     elif user_input == "n":
         print("\nAction cancelled. Returning to main menu...")
     else:
         print("\nInvalid input. Returning to main menu...")

# CLI Interface
def main():
           while True:
                      print("\n----- Welcome to Password Manager -----")
                      print("1. Add Password")
                      print("2. View Password")
                      print("3. Delete Password")
                      print("0. Exit")
                      choice = input("\nEnter your choice: ")
                      if choice == "1":
                          username = input("Enter your username: ")
                          email = input("Enter your email (e.g., Gmail): ")
                          password = input("Enter your password: ")
                          if not username or not email or not password:
                              print("\nPlease fill all fields.")
                              continue
                          add_password(username, email, password)
                      elif choice == "2":
                             view_passwords()
                      elif choice == "3":
                             delete_password()
                      elif choice == "0":
                            print("\nThank you for using Password Manager.")
                            exit()
                      else:
                          print("\nInvalid choice. Please try again.")

# Run
try:
    if __name__ == "__main__":
                              main()
except KeyboardInterrupt:
                         print("\n\nBye.........")