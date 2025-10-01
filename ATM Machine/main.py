import tkinter as tk
from tkinter import messagebox
import os

balance_file = "balance.txt"
transactions_file = "transactions.txt"

# ---------- File Handling ----------
def initialize_files():
    if not os.path.exists(balance_file):
        with open(balance_file, "w") as f:
            f.write("0.0")
    if not os.path.exists(transactions_file):
        open(transactions_file, "w").close()

def read_balance():
    with open(balance_file, "r") as f:
        return float(f.read())

def updated_balance(amount):
    with open(balance_file, "w") as f:
        f.write(str(amount))

def add_transaction(entry):
    with open(transactions_file, "a") as f:
        f.write(entry + "\n")

def get_last_5_transactions():
    try:
        with open(transactions_file, "r") as f:
            lines = f.readlines()
            return lines[-5:]
    except FileNotFoundError:
            print("No Transactions yet!")

# ---------- Tkinter GUI ----------
class ATMApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ATM System")
        self.root.geometry("500x380")
        self.root.config(bg="#f5f7fb")

        # Main Title
        tk.Label(root, text="💳 Welcome to ATM 💳",
                 font=("Arial Rounded MT Bold", 18),
                 bg="#f5f7fb", fg="#2c3e50").pack(pady=20)

        # Frame (Card Style)
        self.card = tk.Frame(root, bg="white", bd=2, relief="ridge")
        self.card.pack(pady=10, padx=20, fill="both", expand=True)

        # Use Grid Layout for Buttons
        btn_opts = {"font": ("Arial", 12), "fg": "white", "relief": "flat", "width": 15, "height": 2, "padx": 10, "pady": 10}

        tk.Button(self.card, text="Deposit", command=self.deposit_ui, bg="#27ae60", **btn_opts).grid(row=0, column=0, padx=10, pady=10)
        tk.Button(self.card, text="Withdraw", command=self.withdraw_ui, bg="#c0392b", **btn_opts).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.card, text="Check Balance", command=self.check_balance, bg="#2980b9", **btn_opts).grid(row=1, column=0, padx=10, pady=10)
        tk.Button(self.card, text="Last 5 Transactions", command=self.show_transactions, bg="#8e44ad", **btn_opts).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.card, text="Exit", command=root.quit, bg="#7f8c8d", **btn_opts).grid(row=2, column=0, columnspan=2, pady=20)

        # Center align
        self.card.grid_columnconfigure(0, weight=1)
        self.card.grid_columnconfigure(1, weight=1)

    # ---------- Features ----------
    def deposit_ui(self):
        self.popup("Deposit Money", self.deposit)

    def withdraw_ui(self):
        self.popup("Withdraw Money", self.withdraw)

    def popup(self, title, action):
        win = tk.Toplevel(self.root)
        win.title(title)
        win.geometry("300x200")
        win.config(bg="white")

        tk.Label(win, text="Enter Amount:", font=("Arial", 12), bg="white").pack(pady=20)
        entry = tk.Entry(win, font=("Arial", 12))
        entry.pack(pady=10)

        def submit():
            try:
                amount = float(entry.get())
                action(amount)
                win.destroy()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number")

        tk.Button(win, text="Submit", command=submit,
                  bg="#27ae60", fg="white", font=("Arial", 12), relief="flat").pack(pady=10)

    def deposit(self, amount):
        if amount > 0:
            balance = read_balance() + amount
            updated_balance(balance)
            add_transaction(f"Deposited: {amount}")
            messagebox.showinfo("Success", f"Deposit Successful!\nNew Balance: {balance}")
        else:
            messagebox.showerror("Error", "Enter a positive number")

    def withdraw(self, amount):
        balance = read_balance()
        if amount <= 0:
            messagebox.showerror("Error", "Enter a positive number")
        elif amount > balance:
            messagebox.showerror("Error", "Insufficient balance")
        else:
            balance -= amount
            updated_balance(balance)
            add_transaction(f"Withdrawn: {amount}")
            messagebox.showinfo("Success", f"Withdraw Successful!\nNew Balance: {balance}")

    def check_balance(self):
        balance = read_balance()
        messagebox.showinfo("Balance", f"Your Current Balance: {balance}")

    def show_transactions(self):
        transactions = get_last_5_transactions()
        if not transactions:
            messagebox.showinfo("Transactions", "No transactions found")
        else:
            messagebox.showinfo("Last 5 Transactions", "\n".join([t.strip() for t in transactions]))


# ---------- Run ----------
if __name__ == "__main__":
    initialize_files()
    root = tk.Tk()
    app = ATMApp(root)
    root.mainloop()
