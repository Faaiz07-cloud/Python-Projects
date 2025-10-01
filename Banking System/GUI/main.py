import os
import json
import tkinter as tk
from tkinter import messagebox, simpledialog
from PIL import Image, ImageTk

# File Handling for Login & SignUp

users_file = "users.json"

def load_users():
    if os.path.exists(users_file):
        with open(users_file, "r") as f:
            return json.load(f)
    return []

def save_users(users):
    with open(users_file, "w") as f:
         json.dump(users, f, indent=4)


# File Handling for User Balance

balance_file = "balance.json"

def load_balance():
    if os.path.exists(balance_file):
        with open(balance_file, "r") as f:
            return json.load(f)
    return {}

def save_balance(balance):
    with open(balance_file, "w") as f:
        json.dump(balance, f, indent=4)

# File Handling for Transactions History

transaction_file = "transaction.json"

def load_transactions():
    if os.path.exists(transaction_file):
        with open(transaction_file, "r") as f:
            return json.load(f)
    return {}

def save_transactions(entry):
    with open(transaction_file, "w") as f:
        json.dump(entry, f, indent=4)


class BankingSystem:
    def __init__(self, root):
       self.root = root
       self.root.geometry("325x625")

       self.users = load_users()
       self.user_balance = load_balance()

       self.current_user_id = None
       self.current_user_name = None
       self.current_user_phone = None
       self.existing_account_no = None
       self.existing_passwords = None

       self.user_details_win = None
       self.login_page()
       # self.dashboard()

    def login_page(self):
        self.clean_window()
        self.root.geometry("325x625")
        self.root.title("Banking System - Login")
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)

        img_1 = Image.open("BankingSystem Images/bank.png")
        img_1 = img_1.resize((335, 225))
        self.bank_img = ImageTk.PhotoImage(img_1)

        label = tk.Label(self.root, image=self.bank_img, bg="#ffffff")
        label.pack(pady=(40, 0))

        label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w",  "fg": "#353b48" }
        entry_style = {
            "font": ("Segoe UI", 12),
            "bg": "#f5f6fa",
            "fg": "#353b48",
            "relief": "flat",
            "bd": 0,
            "highlightthickness": 1,
            "highlightbackground": "#dcdde1",
            "highlightcolor": "#00cec9"
        }

        account_no_label = tk.Label(self.root, text="Account No.", **label_style)
        account_no_label.pack(fill="x", padx=(29, 0), pady=(12, 7))
        self.account_no_entry = tk.Entry(self.root, **entry_style)
        self.account_no_entry.pack(fill="x", padx=(30, 30), ipady=8)

        pass_label = tk.Label(self.root, text="Password", **label_style)
        pass_label.pack(fill="x", padx=(29, 0), pady=(32, 7))
        self.pass_entry = tk.Entry(self.root, **entry_style, show="*")
        self.pass_entry.pack(fill="x", padx=(30, 30), ipady=8)

        login_img = Image.open("BankingSystem Images/login.png")
        login_img = login_img.resize((95, 60))
        self.login_img_button = ImageTk.PhotoImage(login_img)

        login_button = tk.Button(self.root, image=self.login_img_button,
                                 bg='#ffffff', relief='flat', bd=0, command=self.login, activebackground="#ffffff")
        login_button.place(x=112, y=484)

        self.root.bind("<Return>", lambda e: self.login())

        label_2 = tk.Label(self.root, text="Don't have an account?", bg="#ffffff",  font=("Segoe UI", 11),)
        label_2.place(x=51, y=560)

        signup_button = tk.Button(self.root, text="SignUp", font=("Segoe UI", 11, "bold"),
                                 bg='#ffffff', relief='flat', bd=0, command=self.signup_page, activebackground="#ffffff")
        signup_button.place(x=208, y=558)

    def login(self):
        account_no = self.account_no_entry.get()
        password = self.pass_entry.get()

        if not account_no or not password:
            messagebox.showwarning("Warning", "Please enter your account number or password.")
            return
        account_found = False
        for user in self.users:
            if user["acc_no"] == account_no:
                if user["password"] == password:
                    self.existing_account_no = user["acc_no"]
                    self.current_user_id = user["id"]
                    self.current_user_name = user["name"]
                    self.current_user_phone = user["phone"]
                    messagebox.showinfo("Success", "You have been successfully logged in.")
                    self.dashboard()
                    return
                else:
                    messagebox.showerror("Error", "Invalid password.")
                    return

        if not account_found:
            messagebox.showwarning("Warning",f"Account No. {account_no} not found. Please create a new account or try a different Account No.")

    def signup_page(self):
        self.clean_window()
        self.root.geometry("325x695")
        self.root.title("Banking System - SignUp")
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)

        img_1 = Image.open("BankingSystem Images/bank.png")
        img_1 = img_1.resize((230, 155))
        self.bank_img = ImageTk.PhotoImage(img_1)

        label = tk.Label(self.root, image=self.bank_img, bg="#ffffff")
        label.pack(pady=(0, 0))

        label_style = {"font": ("Segoe UI", 10, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
        entry_style = {
            "font": ("Segoe UI", 10),
            "bg": "#f5f6fa",
            "fg": "#353b48",
            "relief": "flat",
            "bd": 0,
            "highlightthickness": 1,
            "highlightbackground": "#dcdde1",
            "highlightcolor": "#00cec9"
        }

        # Customer ID
        customer_id_label = tk.Label(self.root, text="Customer ID", **label_style)
        customer_id_label.pack(fill="x", padx=(29, 0), pady=(7, 7))  # label to entry gap = 7
        self.customer_id_entry = tk.Entry(self.root, **entry_style,)
        self.customer_id_entry.pack(fill="x", padx=(30, 30), ipady=8, pady=(0, 19))  # entry to next label gap = 20

        # Customer Name
        customer_name_label = tk.Label(self.root, text="Customer Name", **label_style)
        customer_name_label.pack(fill="x", padx=(29, 0), pady=(0, 7))
        self.customer_name_entry = tk.Entry(self.root, **entry_style,)
        self.customer_name_entry.pack(fill="x", padx=(30, 30), ipady=8, pady=(0, 19))

        # Phone Number
        customer_phone_label = tk.Label(self.root, text="Phone No.", **label_style)
        customer_phone_label.pack(fill="x", padx=(29, 0), pady=(0, 7))
        self.customer_phone_entry = tk.Entry(self.root, **entry_style)
        self.customer_phone_entry.pack(fill="x", padx=(30, 30), ipady=8, pady=(0, 19))

        # Account Number
        acc_no_label = tk.Label(self.root, text="Account No.", **label_style)
        acc_no_label.pack(fill="x", padx=(29, 0), pady=(0, 7))
        self.acc_no_entry = tk.Entry(self.root, **entry_style)
        self.acc_no_entry.pack(fill="x", padx=(30, 30), ipady=8, pady=(0, 19))

        # Password
        pass_label = tk.Label(self.root, text="Password", **label_style)
        pass_label.pack(fill="x", padx=(29, 0), pady=(0, 7))
        self.pass_entry = tk.Entry(self.root, **entry_style, show="*")
        self.pass_entry.pack(fill="x", padx=(30, 30), ipady=8, pady=(0, 19))

        signup_img = Image.open("BankingSystem Images/signup.png")
        signup_img = signup_img.resize((90, 55))
        self.signup_img_button = ImageTk.PhotoImage(signup_img)

        signup_button = tk.Button(self.root, image=self.signup_img_button,
                                 bg='#ffffff', relief='flat', bd=0, command=self.signup, activebackground="#ffffff" )
        signup_button.place(x=112, y=591)

        self.root.bind("<Return>", lambda e: self.signup())

        label_2 = tk.Label(self.root, text="Already have an account?", bg="#ffffff", font=("Segoe UI", 11), )
        label_2.place(x=50, y=654)

        login_button = tk.Button(self.root, text="Login", font=("Segoe UI", 11, "bold"),
                                  bg='#ffffff', relief='flat', bd=0, command=self.login_page,
                                  activebackground="#ffffff")
        login_button.place(x=222, y=652)

    def signup(self):
        customer_id = self.customer_id_entry.get()
        customer_name = self.customer_name_entry.get()
        customer_phone = self.customer_phone_entry.get()
        acc_no = self.acc_no_entry.get()
        password = self.pass_entry.get()

        if not customer_id or not customer_name or not customer_phone or not acc_no or not password:
            messagebox.showwarning("Warning", "Please complete all required fields.")
            return

        for user in self.users:
            existing_id = user['id']
            existing_accounts = user['acc_no']
            if existing_id == customer_id:
                messagebox.showwarning("Warning", f"Customer ID '{customer_id}' is already registered.")
                return
            if existing_accounts == acc_no:
                messagebox.showwarning("Warning", f"Account Number '{acc_no}' is already associated with another customer.")
                return
        new_user = {
            "id": customer_id,
            "name": customer_name,
            "phone": customer_phone,
            "acc_no": acc_no,
            "password": password,
        }
        self.users.append(new_user)
        save_users(self.users)

        self.user_balance[acc_no] = 0
        save_balance(self.user_balance)

        messagebox.showinfo("Registration successful", f"Customer '{customer_id}' has been successfully registered with Account No. {acc_no}.")
        self.login_page()

    def dashboard(self):
        self.clean_window()
        self.root.geometry("325x628")
        self.root.title("Dashboard")
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)

        label_hello = tk.Label(self.root, text="Hello,", font=("Segoe UI", 18, "bold"), bg="#ffffff", fg="#c5c7c2")
        label_hello.place(x=25, y=8)
        label_name = tk.Label(self.root, text=self.current_user_name, font=("Segoe UI", 20, "bold"), bg="#ffffff", fg="#272815")
        label_name.place(x=25, y=40)

        logout_img = Image.open("BankingSystem Images/logout.png")
        logout_img = logout_img.resize((103, 80))
        self.logout_img_button = ImageTk.PhotoImage(logout_img)

        logout_button = tk.Button(self.root, image=self.logout_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.logout, activebackground="#ffffff")
        logout_button.place(x=209, y=10)

        balance = Image.open("BankingSystem Images/balance pic.png")
        balance = balance.resize((307, 200))
        self.balance = ImageTk.PhotoImage(balance)

        label_balance_pic = tk.Label(self.root, image=self.balance, bg="#ffffff")
        label_balance_pic.place(x=7, y=110)

        label_bvc = tk.Label(self.root, text="BVC", font=("Segoe UI", 17, "bold"), bg="#ffec73", fg="#3D240F")
        label_bvc.place(x=30, y=138)

        label_available_balance = tk.Label(self.root, text="Available Balance", font=("Segoe UI", 15, "bold"), bg="#ffec73", fg="#3D240F")
        label_available_balance.place(x=30, y=203)

        balance = self.user_balance.get(self.existing_account_no, 0)

        self.label_balance = tk.Label(self.root, text=balance, font=("Segoe UI", 29, "bold"), bg="#ffec73", fg="#3D240F")
        self.label_balance.place(x=30, y=236)

        rectangle = Image.open("BankingSystem Images/Rectangle.jpg")
        rectangle = rectangle.resize((307, 85))
        self.rectangle = ImageTk.PhotoImage(rectangle)

        label_rectangle_pic = tk.Label(self.root, image=self.rectangle, bg="#ffffff")
        label_rectangle_pic.place(x=7, y=320)

        deposit_img = Image.open("BankingSystem Images/deposit.png")
        deposit_img = deposit_img.resize((84, 74))
        self.deposit_img_button = ImageTk.PhotoImage(deposit_img)

        deposit_button = tk.Button(self.root, image=self.deposit_img_button,
                                  bg='#f4f2f0', relief='flat', bd=0, command=self.add, activebackground="#f4f2f0")
        deposit_button.place(x=24, y=326)

        withdraw_img = Image.open("BankingSystem Images/withdraw.png")
        withdraw_img = withdraw_img.resize((84, 74))
        self.withdraw_img_button = ImageTk.PhotoImage(withdraw_img)

        withdraw_button = tk.Button(self.root, image=self.withdraw_img_button,
                                   bg='#f4f2f0', relief='flat', bd=0, command=self.withdraw, activebackground="#f4f2f0")
        withdraw_button.place(x=123, y=328)

        user_img = Image.open("BankingSystem Images/user.png")
        user_img = user_img.resize((84, 74))
        self.user_img_button = ImageTk.PhotoImage(user_img)

        user_button = tk.Button(self.root, image=self.user_img_button,
                                   bg='#f4f2f0', relief='flat', bd=0, command=self.details, activebackground="#f4f2f0")
        user_button.place(x=216, y=325)


        label6 = tk.Label(self.root, text="Recently Payment", bg="#ffffff", fg="#222222", font=("Calibri", 15, "bold"))
        label6.place(x=30, y=428)

        button = tk.Button(self.root, text="View All", bg="#ffffff", fg="#6f6f6f",  font=("Calibri", 11, "bold"),
                           relief="flat", bd=0, command=self.view_all_transactions)
        button.place(x=246, y=430)

        transactions = load_transactions()
        user_transactions = transactions.get(self.existing_account_no, [])

        # Last 2 show karna
        last_transactions = user_transactions[-2:][::-1]

        if not last_transactions:
            tk.Label(self.root, text="No recent transactions",
                     font=("Calibri", 14), bg="#ffffff", fg="#666").place(x=30, y= 470)
            return

        # Frame jahan sari transactions show hongi
        transactions_frame = tk.Frame(self.root, bg="#ffffff")
        transactions_frame.place(x=30, y=470)

        for t in last_transactions:
            transaction_type = t['type']
            amount = t['amount']
            date = t['date']

            # Row frame for each transaction
            row_frame = tk.Frame(transactions_frame, bg="#ffffff")
            row_frame.pack(fill="x", pady=5)

            # Top row (Type & Amount)
            top_row = tk.Frame(row_frame, bg="#ffffff")
            top_row.pack(fill="x")

            tk.Label(top_row, text=transaction_type, font=("Calibri", 14, "bold"),
                     bg="#ffffff", fg="#222").pack(side="left")

            tk.Label(top_row, text=amount, font=("Calibri", 15, "bold"),
                     bg="#ffffff", fg="#222").pack(side="right", padx=140)

            # Bottom row (Date)
            tk.Label(row_frame, text=date, font=("Calibri", 12),
                     bg="#ffffff", fg="#666").pack(anchor="w", pady=(2, 5))


    def view_all_transactions(self):
        self.clean_window()
        self.root.title("Transactions")
        self.root.resizable(False, False)
        self.root.geometry("325x625")
        self.root.configure(background="#ffffff")

        back_img = Image.open("BankingSystem Images/menu_bar_img.png")
        back_img = back_img.resize((33, 33))
        self.back_img_button = ImageTk.PhotoImage(back_img)

        button_back = tk.Button(self.root, image=self.back_img_button,
                                bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
        button_back.place(x=15, y=8)

        label_all_transactions = tk.Label(self.root, text="Transactions",
                                         bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
        label_all_transactions.place(x=50, y=2)

        # frame for canvas(used for divider) and scrollbar

        transactions = load_transactions()
        user_transactions = transactions.get(self.existing_account_no, [])

        if not user_transactions:
            tk.Label(self.root, text="No Transactions Yet", font=("Calibri", 15),
                     bg="#ffffff", fg="#666").place(x=60,y=70)
            return


        frame = tk.Frame(self.root, bg='#ffffff')
        frame.pack(fill="both", expand=True, pady=(63, 0))

        canvas = tk.Canvas(frame, bg="#ffffff", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = tk.Frame(canvas, bg="#ffffff")
        window = canvas.create_window((0, 0), window=content_frame, anchor="nw")

        for t in user_transactions[::-1]:
                transaction_type = t['type']
                amount = t['amount']
                date = t['date']

                tk.Label(content_frame, text=transaction_type,
                         font=('Calibri', 16, 'bold'), bg="#ffffff", fg='#222222',
                         anchor="w", ).pack(anchor="w", padx=(33,0), pady=(0, 3))
                color = "green" if t["type"] == "Deposit" else "red"
                tk.Label(content_frame, text=f"Rs: {amount}",
                         font=("Calibri", 15, "bold"), bg="#ffffff", fg=color,
                         anchor="w", ).pack(anchor="w", padx=35)

                tk.Label(content_frame, text=date,
                         font=('Calibri', 14, 'bold'), fg="#6f6f6f", bg="#ffffff",
                         anchor="w").pack(anchor="w", padx=34, pady=(0, 6))

                # Divider Line
                tk.Frame(content_frame, bg="#e0e0e0", height=1).pack(fill="x", pady=5)

        # Update scroll region
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            # Make content_frame same width as canvas
            canvas.itemconfig(window, width=event.width)

        canvas.bind("<Configure>", on_configure)

        # Mousewheel scroll support
        def _on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        canvas.bind_all("<MouseWheel>", _on_mousewheel)

    def add(self):
        amount = simpledialog.askinteger("+", "Enter amount to Deposit")
        if amount is None:
            return
        if amount <= 0:
            messagebox.showwarning("Warning", "Please enter a valid amount. Must be greater than 0.")
            return
        current_balance = self.user_balance.get(self.existing_account_no, 0)
        self.user_balance[self.existing_account_no] = current_balance + amount
        save_balance(self.user_balance)

        # ✅ Transaction Save
        transactions = load_transactions()
        from datetime import datetime
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d | %H:%M"),
            "type": "Deposit",
            "amount": amount,
            "acc_no": self.existing_account_no
        }
        if self.existing_account_no not in transactions:
            transactions[self.existing_account_no] = []
        transactions[self.existing_account_no].append(entry)
        save_transactions(transactions)

        updated_balance = self.user_balance[self.existing_account_no]
        self.label_balance.config(text=updated_balance)
        messagebox.showinfo("Success", f"{amount} Deposited Successfully.")

        self.dashboard()
    def withdraw(self):
        amount = simpledialog.askinteger("-", "Enter amount to Withdraw")
        current_balance = self.user_balance.get(self.existing_account_no, 0)
        if amount is None:
            return
        if amount <= 0:
            messagebox.showwarning("Warning", "Please enter a valid amount. Must be greater than 0.")
            return
        if amount > current_balance:
            messagebox.showwarning("Warning", "Insufficient balance.")
            return
        self.user_balance[self.existing_account_no] = current_balance - amount
        save_balance(self.user_balance)

        # ✅ Transaction Save
        transactions = load_transactions()
        from datetime import datetime
        entry = {
            "date": datetime.now().strftime("%Y-%m-%d | %H:%M"),
            "type": "Withdraw",
            "amount": amount,
            "acc_no": self.existing_account_no
        }
        if self.existing_account_no not in transactions:
            transactions[self.existing_account_no] = []
        transactions[self.existing_account_no].append(entry)
        save_transactions(transactions)

        updated_balance = self.user_balance[self.existing_account_no]
        self.label_balance.config(text=updated_balance)
        messagebox.showinfo("Success", f"{amount} Withdrawn Successfully.")

        self.dashboard()

    def details(self):
        if self.user_details_win is None or not tk.Toplevel.winfo_exists(self.user_details_win):
            self.user_details_win = tk.Toplevel(self.root)
            self.user_details_win.title("Account Details")
            self.user_details_win.geometry("325x442")
            self.user_details_win.configure(bg="#ffffff")
            self.user_details_win.resizable(False, False)

            label_hello_1 = tk.Label(self.user_details_win, text="Hello,", font=("Segoe UI", 18, "bold"), bg="#ffffff", fg="#c5c7c2")
            label_hello_1.place(x=25, y=8)
            label_name_1 = tk.Label(self.user_details_win, text=self.current_user_name, font=("Segoe UI", 20, "bold"), bg="#ffffff",
                                  fg="#272815")
            label_name_1.place(x=25, y=40)

            logout_img_1 = Image.open("BankingSystem Images/logout.png")
            logout_img_1 = logout_img_1.resize((103, 80))
            self.logout_img_button_1 = ImageTk.PhotoImage(logout_img_1)

            logout_button_1 = tk.Button(self.user_details_win, image=self.logout_img_button_1,
                                      bg='#ffffff', relief='flat', bd=0, command=self.logout,
                                      activebackground="#ffffff")
            logout_button_1.place(x=209, y=10)

            rectangle_1 = Image.open("BankingSystem Images/Rectangle details.jpg")
            rectangle_1 = rectangle_1.resize((307, 85))
            self.rectangle_1 = ImageTk.PhotoImage(rectangle_1)

            label_rectangle_pic_1 = tk.Label(self.user_details_win, image=self.rectangle_1, bg="#ffffff")
            label_rectangle_pic_1.place(x=7, y=110)

            label_details = tk.Label(self.user_details_win, text="Account Details", font=("Segoe UI", 20, "bold"),
                                     bg="#ffffff", fg="#272815")
            label_details.place(x=27, y=130)

            rectangle_2 = Image.open("BankingSystem Images/Rectangle Data.jpg")
            rectangle_2 = rectangle_2.resize((307, 202))
            self.rectangle_2 = ImageTk.PhotoImage(rectangle_2)

            label_rectangle_pic_2 = tk.Label(self.user_details_win, image=self.rectangle_2, bg="#ffffff")
            label_rectangle_pic_2.place(x=7, y=210)

            label_name_2 = tk.Label(self.user_details_win, text=f"Name: {self.current_user_name}" , font=("Calibri", 16, "bold"),
                                     bg="#ffffff", fg="#272815")
            label_name_2.place(x=27, y=232)

            label_cus_id = tk.Label(self.user_details_win, text=f"ID: {self.current_user_id}", font=("Calibri", 16, "bold"),
                                    bg="#ffffff", fg="#272815")
            label_cus_id.place(x=27, y=272)

            label_cus_phone = tk.Label(self.user_details_win, text=f"Phone No: {self.current_user_phone}", font=("Calibri", 16, "bold"),
                                    bg="#ffffff", fg="#272815")
            label_cus_phone.place(x=27, y=316)

            label_acc_no = tk.Label(self.user_details_win, text=f"Account No: {self.existing_account_no}", font=("Calibri", 16, "bold"),
                                    bg="#ffffff", fg="#272815")
            label_acc_no.place(x=27, y=360)

        else:
            self.user_details_win.lift()
            self.user_details_win.focus_force()
    def logout(self):
        if messagebox.askokcancel("Logout", "Do you want to logout?"):
            self.login_page()

    def clean_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
run = BankingSystem(root)
root.mainloop()

