import os
import json
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
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

def add_password(username, email, password):
    with open(PASSWORD_FILE, "a") as file:
        encrypted_password = fernet.encrypt(password.encode()).decode()
        file.write(f"{username} | {email} | {encrypted_password}\n")


# File Handling for Login & SignUp
users_file = "password_manager_users.json"

def load_users():
    if os.path.exists(users_file):
        with open(users_file, "r") as f:
            return json.load(f)
    return []

def save_users(users):
    with open(users_file, "w") as f:
        json.dump(users, f, indent=4)

# Class
class PasswordManager:
    def __init__(self, root):
        self.root = root
        self.current_username = None
        self.users = load_users()
        self.add_pass_window = None
        self.login_page()
        # self.dashboard()

    def login_page(self):
        self.clean_window()
        self.root.geometry("325x625+530+50")
        self.root.overrideredirect(True)
        self.root.config(bg="#000000")
        self.root.resizable(False, False)

        img_1 = Image.open("Password Manager Images/splash.png")
        img_1 = img_1.resize((335, 200))
        self.splash_img = ImageTk.PhotoImage(img_1)

        label = tk.Label(self.root, image=self.splash_img, bg="#000000")
        label.pack(pady=(40, 0))

        label_style = {"font": ("Segoe UI", 12), "bg": "#000000", "anchor": "w", "fg": "#ffffff"}
        entry_style = {
        "font": ("Segoe UI", 12),
        "bg": "#ffffff",              # White background inside entry
        "fg": "#000000",              # Black text for readability
        "insertbackground": "#00cec9",# Cursor color (same as highlight)
        "relief": "flat",
        "bd": 0,
        "highlightthickness": 2,      # Thicker border when selected
        "highlightbackground": "#f7931e", # Border color when NOT focused
        "highlightcolor": "#00cec9"   # Border color when focused
        }

        username_label = tk.Label(self.root, text="Username", **label_style)
        username_label.pack(fill="x", padx=(29, 0), pady=(12, 7))
        self.username_entry = tk.Entry(self.root, **entry_style)
        self.username_entry.pack(fill="x", padx=(30, 30), ipady=8)

        pass_label = tk.Label(self.root, text="Password", **label_style)
        pass_label.pack(fill="x", padx=(29, 0), pady=(32, 7))
        self.pass_entry = tk.Entry(self.root, **entry_style, show="*")
        self.pass_entry.pack(fill="x", padx=(30, 30), ipady=8)

        login_img = Image.open("Password Manager Images/login&signup.png")
        login_img = login_img.resize((95, 61))
        self.login_img_button = ImageTk.PhotoImage(login_img)

        login_button = tk.Button(self.root, image=self.login_img_button,
                                 bg='#000000', relief='flat', bd=0, command=self.login, activebackground="#000000")
        login_button.place(x=112, y=484)

        label_login = tk.Label(self.root, text="Login", bg="#f7931e", fg="#ffffff", font=("Segoe UI", 13, "bold"))
        label_login.place(x=135, y=500)

        self.root.bind("<Return>", lambda e: self.login())

        label_2 = tk.Label(self.root, text="Don't have an account?", bg="#000000", fg="#ffffff", font=("Segoe UI", 11))
        label_2.place(x=51, y=560)

        signup_button = tk.Button(self.root, text="SignUp", font=("Segoe UI", 13, "bold"),
                                  bg='#000000', fg="#f7931e", relief='flat', bd=0, command=self.signup_page,
                                  activebackground="#000000", activeforeground="#f7931e")
        signup_button.place(x=208, y=555)

    def login(self):
        username = self.username_entry.get()
        password = self.pass_entry.get()

        if not username or not password:
            messagebox.showwarning("Warning", "Both fields are required!")
            return

        for user in self.users:
            if user["username"] == username:
                if user["password"] == password:
                    self.current_username = user["username"]
                    messagebox.showinfo("Success", "You have been successfully logged in.")
                    self.dashboard()
                    return
                else:
                    messagebox.showerror("Error", "Invalid Password!")
                    return

        messagebox.showwarning("Warning", f"No account for '{username}'. Please sign up or retry.")

    def signup_page(self):
        self.clean_window()
        self.root.geometry("325x625+530+50")
        self.root.overrideredirect(True)
        self.root.config(bg="#000000")
        self.root.resizable(False, False)

        img_1 = Image.open("Password Manager Images/splash.png")
        img_1 = img_1.resize((335, 200))
        self.splash_img = ImageTk.PhotoImage(img_1)

        label = tk.Label(self.root, image=self.splash_img, bg="#000000")
        label.pack(pady=(40, 0))

        label_style = {"font": ("Segoe UI", 12), "bg": "#000000", "anchor": "w", "fg": "#ffffff"}
        entry_style = {
            "font": ("Segoe UI", 12),
            "bg": "#ffffff",  # White background inside entry
            "fg": "#000000",  # Black text for readability
            "insertbackground": "#00cec9",  # Cursor color (same as highlight)
            "relief": "flat",
            "bd": 0,
            "highlightthickness": 2,  # Thicker border when selected
            "highlightbackground": "#f7931e",  # Border color when NOT focused
            "highlightcolor": "#00cec9"  # Border color when focused
        }

        username_label = tk.Label(self.root, text="Username", **label_style)
        username_label.pack(fill="x", padx=(29, 0), pady=(12, 7))
        self.username_entry = tk.Entry(self.root, **entry_style)
        self.username_entry.pack(fill="x", padx=(30, 30), ipady=8)

        pass_label = tk.Label(self.root, text="Password", **label_style)
        pass_label.pack(fill="x", padx=(29, 0), pady=(32, 7))
        self.pass_entry = tk.Entry(self.root, **entry_style, show="*")
        self.pass_entry.pack(fill="x", padx=(30, 30), ipady=8)

        signup_img = Image.open("Password Manager Images/login&signup.png")
        signup_img = signup_img.resize((95, 61))
        self.signup_img_button = ImageTk.PhotoImage(signup_img)

        signup_button = tk.Button(self.root, image=self.signup_img_button,
                                 bg='#000000', relief='flat', bd=0, command=self.signup, activebackground="#000000")
        signup_button.place(x=112, y=484)

        label_signup = tk.Label(self.root, text="SignUp", bg="#f7931e", fg="#ffffff", font=("Segoe UI", 13, "bold"))
        label_signup.place(x=129, y=500)

        self.root.bind("<Return>", lambda e: self.signup())

        label_2 = tk.Label(self.root, text="Already have an account?", bg="#000000", fg="#ffffff", font=("Segoe UI", 11))
        label_2.place(x=51, y=560)

        login_button = tk.Button(self.root, text="Login", font=("Segoe UI", 13, "bold"),
                                  bg='#000000', fg="#f7931e", relief='flat', bd=0, command=self.login_page,
                                  activebackground="#000000", activeforeground="#f7931e")
        login_button.place(x=224, y=555)

    def signup(self):
        username = self.username_entry.get()
        password = self.pass_entry.get()

        if not username or not password:
            messagebox.showwarning("Warning", "Both fields are required!")
            return

        for user in self.users:
            if user['username'] == username:
                messagebox.showwarning("Warning", f"Username '{username}' is already registered.")
                return

        new_user = {"username": username, "password": password}
        self.users.append(new_user)
        save_users(self.users)

        messagebox.showinfo("Registration successful", "Account has been created.")
        self.login_page()

    def dashboard(self):
        self.clean_window()
        self.root.geometry("330x690+530+20")
        self.root.overrideredirect(True)
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)

        label_hello = tk.Label(self.root, text="Hello,", font=("Segoe UI", 18, "bold"), bg="#ffffff", fg="#c5c7c2")
        label_hello.place(x=25, y=8)
        label_name = tk.Label(self.root, text=self.current_username, font=("Segoe UI", 20, "bold"),
                              bg="#ffffff", fg="#272815")
        label_name.place(x=25, y=40)

        logout_img = Image.open("Password Manager Images/logout.png")
        logout_img = logout_img.resize((103, 80))
        self.logout_img_button = ImageTk.PhotoImage(logout_img)

        logout_button = tk.Button(self.root, image=self.logout_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.logout, activebackground="#ffffff")
        logout_button.place(x=209, y=10)

        frame = Image.open("Password Manager Images/rounded-rectangle.png")
        frame = frame.resize((320, 171))
        self.frame = ImageTk.PhotoImage(frame)

        label = tk.Label(self.root, image=self.frame, bg="#ffffff")
        label.place(x=3, y=100)

        logo = Image.open("Password Manager Images/logo.png")
        logo = logo.resize((135, 93))
        self.logo = ImageTk.PhotoImage(logo)

        label2 = tk.Label(self.root, image=self.logo, bg="#323232")
        label2.place(x=23, y=140)

        label3 = tk.Label(self.root, text="SecureX", bg="#323232", fg="#ffffff", font=("Segoe UI", 24, "bold"))
        label3.place(x=135, y=145)

        label4 = tk.Label(self.root, text="Security Made Simple", bg="#323232", fg="#ffffff", font=("Segoe UI", 10,))
        label4.place(x=137, y=195)

        label_recent_pass = tk.Label(self.root, text="Recently Added", bg="#ffffff", fg="#323232",
                                      font=("Calibri", 13, "bold"))
        label_recent_pass.place(x=24, y=282)

        button = tk.Button(self.root, text="View All", bg="#ffffff", fg="#6f6f6f", font=("Calibri", 12, "bold"),
                           relief="flat", bd=0, command=self.all)
        button.place(x=238, y=280)

        with open(PASSWORD_FILE, "r") as file:
            lines = file.readlines()

        y_axis = 315
        spacing = 100  # frame height + some vertical gap

        if not lines:
           tk.Label(self.root, text="No recent Passwords!",
                bg='#ffffff', fg='#6f6f6f', font=('Calibri', 13, 'bold')).place(x=81, y=370)

        for i, line in enumerate(reversed(lines[-3:])):
            username, email, encrypted_password = line.strip().split(" | ")
            decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()
            frame2 = tk.Frame(self.root, bg="#ffffff", width=300, height=100)
            frame2.place(x=15, y=y_axis + i * spacing)

            label_name_get = tk.Label(
                frame2,
                text=username,
                bg="#ffffff",
                fg="#111111",
                font=("Calibri", 15, "bold")
            )
            label_name_get.place(x=15, y=12)

            # Email (smaller + grayish)
            label_email_get = tk.Label(
                frame2,
                text=email,
                bg="#ffffff",
                fg="#777777",
                font=("Calibri", 11)
            )
            label_email_get.place(x=15, y=45)


            label_pass_get = tk.Label(
                frame2,
                text=decrypted_password,
                bg="#ffffff",
                fg="#222222",
                font=("Calibri", 11)
            )
            label_pass_get.place(x=15, y=70)

        add_img = Image.open("Password Manager Images/plus.png")
        add_img = add_img.resize((60, 60))
        self.add_img_button = ImageTk.PhotoImage(add_img)

        add_button = tk.Button(self.root, image=self.add_img_button,
                               bg='#ffffff', relief='flat', bd=0, command=self.add_product_page,
                               activebackground="#ffffff")
        add_button.place(x=252, y=612)

    def all(self):
        self.clean_window()
        self.root.title("All Passwords")
        self.root.resizable(False, False)
        self.root.overrideredirect(False)
        self.root.geometry("340x680")
        self.root.configure(background="#ffffff")

        back_img = Image.open("Password Manager Images/menu_bar_img.png")
        back_img = back_img.resize((33, 33))
        self.back_img_button = ImageTk.PhotoImage(back_img)

        button_back = tk.Button(self.root, image=self.back_img_button,
                                bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
        button_back.place(x=15, y=8)

        label_main = tk.Label(self.root, text="Password Manager",
                              bg='#ffffff', fg='#323232', font=('Calibri', 17, 'bold'))
        label_main.place(x=50, y=8)

        # ================== SCROLLABLE FRAME ==================
        # Create canvas
        canvas = tk.Canvas(self.root, bg="#ffffff", highlightthickness=0)
        canvas.place(x=0, y=50, width=340, height=630)

        # Add scrollbar
        scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        scrollbar.place(x=325, y=0, height=679)

        # Configure canvas
        canvas.configure(yscrollcommand=scrollbar.set)

        # Create inner frame
        scroll_frame = tk.Frame(canvas, bg="#ffffff")

        # Place frame inside canvas
        canvas.create_window((0, 0), window=scroll_frame, anchor="nw")

        # Update scroll region dynamically
        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        scroll_frame.bind("<Configure>", on_configure)
        # ======================================================

        with open(PASSWORD_FILE, "r") as file:
            lines = file.readlines()

        if not lines:
            tk.Label(self.root, text="No Passwords saved yet!",
                     bg='#ffffff', fg='#6f6f6f', font=('Calibri', 14, 'bold')).pack(pady=180)

        for i, line in enumerate(lines):
            username, email, encrypted_password = line.strip().split(" | ")
            decrypted_password = fernet.decrypt(encrypted_password.encode()).decode()

            frame2 = tk.Frame(scroll_frame, bg="#ffffff", width=300, height=100, highlightbackground="#e0e0e0",
                              highlightthickness=0)
            frame2.pack(pady=(10,0), padx=15, fill="x")  # 👈 pack instead of place

            label_name_get = tk.Label(
                frame2,
                text=username,
                bg="#ffffff",
                fg="#111111",
                font=("Calibri", 15, "bold")
            )
            label_name_get.pack(anchor="w", pady=(0, 0), padx=10)

            label_email_get = tk.Label(
                frame2,
                text=email,
                bg="#ffffff",
                fg="#777777",
                font=("Calibri", 11)
            )
            label_email_get.pack(anchor="w", padx=10)

            label_pass_get = tk.Label(
                frame2,
                text=decrypted_password,
                bg="#ffffff",
                fg="#222222",
                font=("Calibri", 11)
            )
            label_pass_get.pack(anchor="w", padx=10, pady=(0, 10))

    def add_product_page(self):
       if self.add_pass_window is None or not tk.Toplevel.winfo_exists(self.add_pass_window):
           self.add_pass_window = tk.Toplevel(self.root)
           self.add_pass_window.overrideredirect(False)
           self.add_pass_window.title("Add Password")
           self.add_pass_window.geometry("325x360")
           self.add_pass_window.resizable(False, False)
           self.add_pass_window.config(bg="#ffffff")

           label_style = {"font": ("Calibri", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
           entry_style = {
               "font": ("Calibri", 12),
               "bg": "#f5f6fa",
               "fg": "#2d3436",
               "relief": "flat",
               "bd": 0,
               "highlightthickness": 1,
               "highlightbackground": "#dcdde1",
               "highlightcolor": "#00cec9"
           }

           label_main = tk.Label(self.add_pass_window, text="Add a Password",
                                 bg='#ffffff', fg='#323232', font=('Segoe UI', 16, 'bold'))
           label_main.place(x=23, y=16)

           label_username = tk.Label(self.add_pass_window, text="Username", **label_style)
           label_username.pack(fill="x", padx=(31, 0), pady=(90, 4))
           self.username_entry = tk.Entry(self.add_pass_window, **entry_style)
           self.username_entry.pack(fill="x", padx=(30, 30), pady=(0, 18), ipady=6)

           label_email = tk.Label(self.add_pass_window, text="Email", **label_style)
           label_email.pack(fill="x", padx=(31, 0), pady=(0, 4))
           self.entry_email = tk.Entry(self.add_pass_window, **entry_style)
           self.entry_email.pack(fill="x", padx=(30, 30), pady=(0, 18), ipady=6)

           label_password = tk.Label(self.add_pass_window, text="Password", **label_style)
           label_password.pack(fill="x", padx=(31, 0), pady=(0, 4))
           self.entry_pass = tk.Entry(self.add_pass_window, **entry_style, show="*")
           self.entry_pass.pack(fill="x", padx=(30, 30), pady=(0, 18), ipady=6)

           add_button_img = Image.open("Password Manager Images/plus.png")
           add_button_img = add_button_img.resize((60,60))
           self.add_button_img = ImageTk.PhotoImage(add_button_img)

           add_button = tk.Button(self.add_pass_window, image=self.add_button_img,
                                    bg='#ffffff', relief='flat', bd=0, command=self.add,
                                    activebackground='#ffffff')
           add_button.place(x=248, y=7)

       else:
           self.add_pass_window.lift()
           self.add_pass_window.focus_force()

    def add(self):
            username = self.username_entry.get()
            email = self.entry_email.get()
            password = self.entry_pass.get()

            if not username or not email or not password:
                messagebox.showwarning("Warning", "Please fill all fields!")
                return

            add_password(username, email, password)
            self.dashboard()

    def logout(self):
        if messagebox.askokcancel("Logout", "Do you want to logout?"):
            self.login_page()

    def clean_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
run = PasswordManager(root)
root.mainloop()
