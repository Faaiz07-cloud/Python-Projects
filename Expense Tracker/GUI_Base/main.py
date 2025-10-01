# ---------- Modules ----------
import os
import json
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

# ---------- Json File ----------
data_file = "GUI_expenses.json"

# ---------- Load Expenses ----------
def load_expenses():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    else:
        return []

# ---------- Save Expenses ----------
def save_expenses(expenses):
    with open(data_file, "w") as file:
        json.dump(expenses, file, indent=4)

# ---------- ExpenseTracker Class (GUI) ----------
class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")
        self.root.resizable(False, False)
        self.root.geometry("374x620")
        self.root.configure(background="#ffffff")

        self.expenses = load_expenses()
        self.show_home_page()

    def show_home_page(self):
        self.clean_window()
        self.root.title("Expense Tracker")
        self.root.geometry("374x620")

        img_1 = Image.open("Images/home_img.png")
        img_1 = img_1.resize((460,415))
        self.home_img = ImageTk.PhotoImage(img_1)

        label = tk.Label(self.root, image=self.home_img, bg="#ffffff")
        label.pack(pady=(32,0))

        img2 = Image.open("Images/start_img.png")
        img2 = img2.resize((120, 120))
        self.start_img = ImageTk.PhotoImage(img2)
        button = tk.Button(self.root, image=self.start_img, bg="#ffffff", relief="flat", bd=0, command=self.dashboard)
        button.place(x=62, y=457)

        img_exit = Image.open("Images/exit.png")
        img_exit = img_exit.resize((120, 120))
        self.exit_img = ImageTk.PhotoImage(img_exit)
        button = tk.Button(self.root, image=self.exit_img, bg="#ffffff", relief="flat", bd=0, command=self.root.destroy)
        button.place(x=193, y=457)

    def dashboard(self):
        self.clean_window()
        self.root.config(bg="#ffffff")
        self.root.title("Dashboard")
        self.root.geometry("374x655")

        frame = tk.Frame(self.root, bg="#ffffff")
        frame.pack(pady=(20, 0), fill="x")

        img3 = Image.open("Images/menu_bar_img.png")
        img3 = img3.resize((44, 44))
        self.HomeImg = ImageTk.PhotoImage(img3)
        button = tk.Button(frame, image=self.HomeImg, bg="#ffffff", relief="flat", bd=0, command=self.show_home_page)
        button.grid(row=0, column=0, sticky="w", padx=(10, 4))

        label2 = tk.Label(frame, text="Dashboard", bg="#ffffff", fg="#000000",
                          font=("Times New Roman", 26, "bold"))
        label2.grid(row=0, column=1, sticky="w")

        frame2 = tk.Frame(self.root, bg="#ffffff", width=275, height=150)
        frame2.place(x=47, y=70)

        img4 = Image.open("Images/RoundCornerFrame.png")
        img4 = img4.resize((275, 150))
        self.corner_frame = ImageTk.PhotoImage(img4)
        label3 = tk.Label(frame2, image=self.corner_frame, bg="#ffffff")
        label3.place(x=0, y=0, relwidth=1, relheight=1)

        total_expense = sum(float(exp["amount"]) for exp in self.expenses) if self.expenses else 0
        label4 = tk.Label(frame2, text="Total Balance", bg="#212121", fg="#ffffff",
                          font=("Calibri", 17, "bold"))
        label4.place(x=69, y=32)

        label5 = tk.Label(frame2, text=f"${total_expense:,.2f}", bg="#212121", fg="#ffffff",
                          font=("Calibri", 26, "bold"))
        label5.place(x=39, y=68)

        label6 = tk.Label(self.root, text="Recent Expenses", bg="#ffffff", fg="#222222", font=("Calibri", 18, "bold"))
        label6.place(x=18, y=228)

        label7 = tk.Label(self.root, text="Today", bg="#ffffff", fg="#6f6f6f",
                          font=("Calibri", 14, "bold"))
        label7.place(x=18, y=269)

        button = tk.Button(self.root, text="View All", bg="#ffffff", fg="#6f6f6f",  font=("Calibri", 14, "bold"),
                           relief="flat", bd=0, command=self.view_all_expenses)
        button.place(x=270, y=268)

        img = Image.open("Images/DataFrame.png")
        img = img.resize((320, 84))
        self.DataFrameImg = ImageTk.PhotoImage(img)

        user_img = Image.open("Images/user.png")
        user_img = user_img.resize((60, 60))
        self.User_Image = ImageTk.PhotoImage(user_img)

        # ------------------------------------------------------
        # Create multiple frames and place them vertically
        # ------------------------------------------------------
        y_axis = 310
        spacing = 85  # frame height + some vertical gap
        last_expenses = self.expenses[-3:] if self.expenses else []

        for i, exp in enumerate(reversed(last_expenses)):  # reverse so latest is on top
            frame3 = tk.Frame(self.root, bg="#ffffff", width=320, height=84)
            frame3.place(x=27, y=y_axis + i * spacing)

            label = tk.Label(frame3, image=self.DataFrameImg, bg="#ffffff")
            label.place(x=0, y=0, relwidth=1, relheight=1)

            label = tk.Label(frame3, image=self.User_Image, bg="#e0e0e0")
            label.place(x=13, y=10)

            label = tk.Label(frame3, text=exp["category"], bg="#e0e0e0", fg="#000000", font=("Calibri", 16, "bold"))
            label.place(x=75, y=14)

            label = tk.Label(frame3, text=exp["details"], bg="#e0e0e0", fg="#8c8c8c", font=("Calibri", 12, "bold"))
            label.place(x=75, y=43)

            label = tk.Label(frame3, text=f"${exp['amount']}", bg="#e0e0e0", fg="#000000", font=("Calibri", 16, "bold"))
            label.place(x=239, y=25)

        img5 = Image.open("Images/AddImage.png")
        img5 = img5.resize((68, 68))
        self.add_button = ImageTk.PhotoImage(img5)
        button = tk.Button(self.root, image=self.add_button, bg="#ffffff", relief="flat", bd=0, command=self.add_expense)
        button.place(x=289, y=573)

    def add_expense(self):
        self.clean_window()
        self.root.title("Add Expense")
        self.root.geometry("420x647")
        self.root.config(bg="#ffffff")

        # ---------- Title ----------
        title = tk.Label(self.root, text="Add Expense",
                         font=("Segoe UI", 22, "bold"),
                         bg="#ffffff", fg="#2d3436")
        title.pack(pady=(20, 10))

        # Common label style
        label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#636e72"}
        entry_style = {"font": ("Segoe UI", 12), "bd": 0, "bg": "#ffffff", "highlightthickness": 1,
                       "highlightbackground": "#cccccc",
                       "highlightcolor": "#0984e3"}

        # ---------- Date ----------
        date_label = tk.Label(self.root, text="Date (DD/MM/YYYY)", **label_style)
        date_label.pack(fill="x", padx=30, pady=(15, 3))
        date_entry = tk.Entry(self.root, **entry_style)
        date_entry.pack(fill="x", padx=34, ipady=7)

        # ---------- Category ----------
        category_label = tk.Label(self.root, text="Category", **label_style)
        category_label.pack(fill="x", padx=30, pady=(15, 3))
        category_entry = tk.Entry(self.root, **entry_style)
        category_entry.pack(fill="x", padx=34, ipady=7)

        # ---------- Amount ----------
        amount_label = tk.Label(self.root, text="Amount", **label_style)
        amount_label.pack(fill="x", padx=30, pady=(15, 3))
        amount_entry = tk.Entry(self.root, **entry_style)
        amount_entry.pack(fill="x", padx=34, ipady=7)

        # ---------- Mode ----------
        mode_label = tk.Label(self.root, text="Mode", **label_style)
        mode_label.pack(fill="x", padx=30, pady=(15, 3))
        mode_entry = tk.Entry(self.root, **entry_style)
        mode_entry.pack(fill="x", padx=34, ipady=7)

        # ---------- Details ----------
        details_label = tk.Label(self.root, text="Details", **label_style)
        details_label.pack(fill="x", padx=30, pady=(15, 3))
        details_entry = tk.Text(self.root, font=("Segoe UI", 12),
                                bd=0, height=5, bg="#ffffff",
                                highlightthickness=1,
                                highlightbackground="#cccccc",
                                highlightcolor="#0984e3")
        details_entry.pack(fill="x", padx=34, pady=(0, 15))

        def save_new_expense():
            date = date_entry.get().strip()
            category = category_entry.get().strip()
            amount = amount_entry.get().strip()
            mode = mode_entry.get().strip()
            details = details_entry.get("1.0", "end-1c").strip()

            if not (date and category and amount and mode and details):
                messagebox.showerror("Error", "All fields are required!")
                return

            try:
                float(amount)
            except:
                messagebox.showerror("Error", "Amount must be a number!")
                return

            new_expense = {
                "date": date,
                "category": category,
                "amount": amount,
                "mode": mode,
                "details": details
            }
            self.expenses.append(new_expense)
            save_expenses(self.expenses)

            messagebox.showinfo("Success", "Expense added successfully!")
            self.dashboard()

        entry_img = Image.open("Images/start2.png")
        entry_img = entry_img.resize((105, 38))
        self.entry_img_button = ImageTk.PhotoImage(entry_img)
        button = tk.Button(self.root, image=self.entry_img_button, bg="#ffffff",
                           relief="flat", bd=0, command=save_new_expense, activeforeground="#ffffff",
                           activebackground="#ffffff", highlightthickness=0)
        button.place(x=111, y=585)

        cancel_img = Image.open("Images/cancel2.png")
        cancel_img = cancel_img.resize((105, 38))
        self.cancel_img_button = ImageTk.PhotoImage(cancel_img)
        button = tk.Button(self.root, image=self.cancel_img_button, bg="#ffffff", relief="flat", bd=0,
                           activeforeground="#ffffff", activebackground="#ffffff",
                           highlightthickness=0, command=self.dashboard)
        button.place(x=220, y=585)

    def view_all_expenses(self):
         self.clean_window()
         self.root.geometry("697x618")
         self.root.title("All Expenses")
         self.root.config(bg="#f5f5f5")

         style = ttk.Style()
         style.theme_use("default")
         style.configure("Treeview.Heading", font=("Segoe UI", 15, "bold"), padding=[2, 4], relief="flat", bd=0, background="#0178d6", foreground="white")
         style.configure("Treeview", font=("Segoe UI", 14), rowheight=35)
         style.map("Treeview.Heading",
                   background=[("active", "#0160a9")],
                   foreground=[("active", "white")])

         columns = ("ID", "Category", "Expense", "Mode", "Date", "Details")
         treeview = ttk.Treeview(root, columns=columns, show="headings", style="Treeview", height=15)
         treeview.heading("ID", text="ID", anchor="w")
         treeview.heading("Category", text="Category", anchor="w")
         treeview.heading("Expense", text="Expense", anchor="w")
         treeview.heading("Mode", text="Mode", anchor="w")
         treeview.heading("Date", text="Date", anchor="w")
         treeview.heading("Details", text="Details", anchor="w")

         treeview.column("ID", width=43, anchor="w")
         treeview.column("Category", width=99, anchor="w")
         treeview.column("Expense", width=93, anchor="w")
         treeview.column("Mode", width=74, anchor="w")
         treeview.column("Date", width=120, anchor="w")
         treeview.column("Details", width=215, anchor="w")
         treeview.place(x=25, y=25)

         treeview.tag_configure("odd_row", background="#f2f2f2")
         treeview.tag_configure("even_row", background="#ffffff")

         for index, exp in enumerate(self.expenses):
             values = (index + 1, exp["category"], exp["amount"], exp["mode"], exp["date"], exp["details"])
             tag = "even_row" if index % 2 == 0 else "odd_row"
             treeview.insert("", "end", values=values, tags=(tag,))

         previous_img = Image.open("Images/close.png")
         previous_img = previous_img.resize((20, 20))
         self.previous_button = ImageTk.PhotoImage(previous_img)
         button = tk.Button(self.root, image=self.previous_button, bg="#0178D6", relief="flat", bd=0,
                            activebackground="#0178D6", highlightthickness=0, command=self.dashboard)
         button.place(x=644, y=36)

    def clean_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ---------- Create Main Window ----------
root = tk.Tk()

# ---------- Initialize ExpenseTracker Class ----------
play = ExpenseTracker(root)

# ---------- Start Event Loop ----------
root.mainloop()
