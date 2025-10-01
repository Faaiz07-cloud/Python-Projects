import os
import json
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk


File_Name = "library2.json"

def load_books():
    if os.path.exists(File_Name):
        with open(File_Name, "r") as file:
            return json.load(file)
    return []

def save_books(books):
    with open(File_Name, "w") as file:
        json.dump(books, file, indent=4)

def generate_id(books):
    if not books:
        return 1 # if list is empty then id becomes 1
    else:
        max_id = max(book["id"] for book in books) + 1
        return max_id

def find_book_by_id(books, book_id):
    for book in books:
        if book["id"] == book_id:
            return book
    return None


class LibraryManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.resizable(False, False)
        self.root.geometry("377x627")
        self.root.configure(background="#ffffff")

        self.valid_user = "admin"
        self.valid_pass = "12345"

        # for storing window reference
        self.add_win = None
        self.issue_win = None
        self.return_win = None

        self.books = load_books()

        self.show_home_page()

    def show_home_page(self):
         self.clean_window()
         self.root.title("Library Management System - Login")
         self.root.resizable(False, False)
         self.root.geometry("377x627")
         self.root.configure(background="#ffffff")

         img_1 = Image.open("Library Images/splash.png")
         img_1 = img_1.resize((410,210))
         self.home_img = ImageTk.PhotoImage(img_1)

         label = tk.Label(self.root, image=self.home_img, bg="#ffffff")
         label.pack(pady=(40,0))

         label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
         entry_style = {
             "font": ("Segoe UI", 12),
             "bg": "#f5f6fa",
             "fg": "#2d3436",
             "relief": "flat",
             "bd": 0,
             "highlightthickness": 1,
             "highlightbackground": "#dcdde1",
             "highlightcolor": "#00cec9"
         }

         username_label = tk.Label(self.root, text="Username", **label_style)
         username_label.pack(fill="x", padx=(29, 0), pady=(15, 7))
         self.username_entry = tk.Entry(self.root, **entry_style)
         self.username_entry.pack(fill="x", padx=(30, 30), ipady=8)

         pass_label = tk.Label(self.root, text="Password", **label_style)
         pass_label.pack(fill="x", padx=(29, 0), pady=(35, 7))
         self.pass_entry = tk.Entry(self.root, **entry_style, show="*")
         self.pass_entry.pack(fill="x", padx=(30, 30), ipady=8)

         # self.username_entry.insert(0, "admin")
         # self.pass_entry.insert(0, "12345")

         login_img = Image.open("Library Images/login.png")
         login_img = login_img.resize((120, 110))
         self.login_img_button = ImageTk.PhotoImage(login_img)

         login_button = tk.Button(self.root, image=self.login_img_button,
                                    bg='#ffffff', relief='flat', bd=0, command=self.login)
         login_button.place(x=126, y=480)

         self.root.bind("<Return>", lambda e: self.login())

    def login(self):
        username = self.username_entry.get().strip()
        password = self.pass_entry.get().strip()
        if not username or not password:
            messagebox.showerror("Error", "Please enter your username and password.")
            return

        if username != self.valid_user or password != self.valid_pass:
            messagebox.showerror("Error", "Invalid username and password.")
            return
        self.dashboard()


    def dashboard(self):
       self.clean_window()

       self.status_count = {"Available": 0, "Issued": 0}

       for self.data in self.books:
           self.status = self.data["status"]
           if self.status in self.status_count:
               self.status_count[self.status] += 1

       self.total_books = len(self.books)
       self.unique_authors = len(set([self.data["author"] for self.data in self.books]))

       self.root.title("Dashboard")
       self.root.resizable(False, False)
       self.root.geometry("405x677")
       self.root.configure(background="#ffffff")

       label_dashboard = tk.Label(self.root, text="Dashboard",
                                  bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
       label_dashboard.place(x=20, y=12)

       logout_img = Image.open("Library Images/logout.png")
       logout_img = logout_img.resize((112, 82))
       self.logout_img_button = ImageTk.PhotoImage(logout_img)

       logout_button = tk.Button(self.root, image=self.logout_img_button,
                                bg='#ffffff', relief='flat', bd=0, command=self.logout, activebackground="#ffffff")
       logout_button.place(x=276, y=3)

       label_welcome = tk.Label(self.root, text="Welcome to Library Management",  bg='#ffffff', fg='#1b1c1c', font=('Segoe UI', 15,) )
       label_welcome.place(x=20, y=75)
       label_system = tk.Label(self.root, text="System", bg='#ffffff', fg='#1b1c1c',
                                font=('Segoe UI', 15,))
       label_system.place(x=20, y=102)

       label_overview = tk.Label(self.root, text="Library Overview", bg='#ffffff', fg='#1166c1',
                                font=('Segoe UI', 16, "bold"))
       label_overview.place(x=20, y=153)


       all_img = Image.open("Library Images/all.png")
       all_img = all_img.resize((173, 173))
       self.all_img = ImageTk.PhotoImage(all_img)

       button_all = tk.Button(self.root, image=self.all_img, bg="#ffffff", relief="flat", bd=0, command=self.list_all_books, activebackground="#ffffff")
       button_all.place(x=25, y=213)

       label_all_count = tk.Label(self.root, text=self.total_books, bg='#ede7f6', fg='#666666',
                                 font=('Segoe UI', 27, "bold"))
       label_all_count.place(x=87, y=313)

       available_img = Image.open("Library Images/available.png")
       available_img = available_img.resize((173, 173))
       self.available_img = ImageTk.PhotoImage(available_img)

       button_available = tk.Button(self.root, image=self.available_img, bg="#ffffff", relief="flat", bd=0, command=self.list_available_books, activebackground="#ffffff")
       button_available.place(x=207, y=213)

       label_available_count = tk.Label(self.root, text=self.status_count['Available'], bg='#ede7f6', fg='#666666',
                                 font=('Segoe UI', 27, "bold"))
       label_available_count.place(x=269, y=313)

       issued_img = Image.open("Library Images/issued.png")
       issued_img = issued_img.resize((173, 173))
       self.issued_img = ImageTk.PhotoImage(issued_img)

       button_issued = tk.Button(self.root, image=self.issued_img, bg="#ffffff", relief="flat", bd=0, command=self.list_issue_books, activebackground="#ffffff")
       button_issued.place(x=25, y=395)

       label_issued_count = tk.Label(self.root, text=self.status_count['Issued'], bg='#ede7f6', fg='#666666',
                                 font=('Segoe UI', 27, "bold"))
       label_issued_count.place(x=87, y=495)

       authors_img = Image.open("Library Images/authors.png")
       authors_img = authors_img.resize((173, 173))
       self.authors_img = ImageTk.PhotoImage(authors_img)

       button_authors = tk.Button(self.root, image=self.authors_img, bg="#ffffff", relief="flat", bd=0, command=self.list_authors, activebackground="#ffffff")
       button_authors.place(x=207, y=395)

       label_authors_count = tk.Label(self.root, text=self.unique_authors, bg='#ede7f6', fg='#666666',
                                 font=('Segoe UI', 27, "bold"))
       label_authors_count.place(x=269, y=495)

       add_button_img = Image.open("Library Images/Add Book.jpg")
       add_button_img = add_button_img.resize((110, 100))
       self.add_button_img = ImageTk.PhotoImage(add_button_img)

       add_button = tk.Button(self.root, image=self.add_button_img,
                                bg='#ffffff', relief='flat', bd=0, command=self.add_book, activebackground='#ffffff')
       add_button.place(x=31, y=572)

       issue_button_img = Image.open("Library Images/Issue Book.jpg")
       issue_button_img = issue_button_img.resize((110, 100))
       self.issue_button_img = ImageTk.PhotoImage(issue_button_img)

       issue_button = tk.Button(self.root, image=self.issue_button_img,
                                bg='#ffffff', relief='flat', bd=0, command=self.issue_book, activebackground='#ffffff')
       issue_button.place(x=148, y=572)

       return_button_img = Image.open("Library Images/Return Book.jpg")
       return_button_img = return_button_img.resize((110, 100))
       self.return_button_img = ImageTk.PhotoImage(return_button_img)

       return_button = tk.Button(self.root, image=self.return_button_img,
                                bg='#ffffff', relief='flat', bd=0, command=self.return_book, activebackground='#ffffff')
       return_button.place(x=265, y=572)


    def list_all_books(self):
        self.clean_window()
        self.root.title("Library")
        self.root.resizable(False, False)
        self.root.geometry("405x677")
        self.root.configure(background="#ffffff")


        back_img = Image.open("Library Images/menu_bar_img.png")
        back_img = back_img.resize((33, 33))
        self.back_img_button = ImageTk.PhotoImage(back_img)

        button_back = tk.Button(self.root, image=self.back_img_button,
                                bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
        button_back.place(x=15, y=8)

        label_all_books = tk.Label(self.root, text="Library",
                                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
        label_all_books.place(x=50, y=2)

        # frame for canvas(used for divider) and scrollbar

        frame = tk.Frame(self.root, bg='#ffffff')
        frame.pack(fill="both", expand=True, pady=(63, 0))

        canvas = tk.Canvas(frame, bg="#ffffff", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = tk.Frame(canvas, bg="#ffffff")
        window = canvas.create_window((0, 0), window=content_frame, anchor="nw")

        for book in self.books:

            # ID & Title
            tk.Label(content_frame, text=f"{book['id']}. {book['title']}",
                     font=('Calibri', 16, 'bold'), bg="#ffffff", fg='#323232',
                     anchor="w",).pack(anchor="w", padx=12, pady=(0, 3))

            # Author
            tk.Label(content_frame, text=f"Author: {book['author']}",
                     font=("Calibri", 13, "bold"), bg="#ffffff", fg="#6f6f6f",
                     anchor="w",).pack(anchor="w", padx=35)

            # Status
            status_color = "green" if book["status"] == "Available" else "red"
            tk.Label(content_frame, text=f"{book['status']}",
                     font=('Calibri', 15, 'bold'), fg=status_color, bg="#ffffff",
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

    def list_available_books(self):
        self.clean_window()
        self.root.title("Available Books")
        self.root.resizable(False, False)
        self.root.geometry("405x677")
        self.root.configure(background="#ffffff")

        back_img = Image.open("Library Images/menu_bar_img.png")
        back_img = back_img.resize((33, 33))
        self.back_img_button = ImageTk.PhotoImage(back_img)

        button_back = tk.Button(self.root, image=self.back_img_button,
                                bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
        button_back.place(x=15, y=8)

        label_available_books = tk.Label(self.root, text="Available Books",
                                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
        label_available_books.place(x=50, y=2)

        # frame for canvas(used for divider) and scrollbar

        frame = tk.Frame(self.root, bg='#ffffff')
        frame.pack(fill="both", expand=True, pady=(63, 0))

        canvas = tk.Canvas(frame, bg="#ffffff", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = tk.Frame(canvas, bg="#ffffff")
        window = canvas.create_window((0, 0), window=content_frame, anchor="nw")

        for book in self.books:
          if book["status"] == "Available":
            # ID & Title
            tk.Label(content_frame, text=f"{book['id']}. {book['title']}",
                     font=('Calibri', 16, 'bold'), bg="#ffffff", fg='#323232',
                     anchor="w", ).pack(anchor="w", padx=12, pady=(0, 3))

            # Author
            tk.Label(content_frame, text=f"Author: {book['author']}",
                     font=("Calibri", 13, "bold"), bg="#ffffff", fg="#6f6f6f",
                     anchor="w", ).pack(anchor="w", padx=35)

            # Status
            status_color = "green" if book["status"] == "Available" else "red"
            tk.Label(content_frame, text=f"{book['status']}",
                     font=('Calibri', 15, 'bold'), fg=status_color, bg="#ffffff",
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

    def list_issue_books(self):
        self.clean_window()
        self.root.title("Issued Books")
        self.root.resizable(False, False)
        self.root.geometry("405x677")
        self.root.configure(background="#ffffff")

        back_img = Image.open("Library Images/menu_bar_img.png")
        back_img = back_img.resize((33, 33))
        self.back_img_button = ImageTk.PhotoImage(back_img)

        button_back = tk.Button(self.root, image=self.back_img_button,
                                bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
        button_back.place(x=15, y=8)

        label_issue_books = tk.Label(self.root, text="Issued Books",
                                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
        label_issue_books.place(x=50, y=2)

        # frame for canvas(used for divider) and scrollbar

        frame = tk.Frame(self.root, bg='#ffffff')
        frame.pack(fill="both", expand=True, pady=(63, 0))

        canvas = tk.Canvas(frame, bg="#ffffff", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = tk.Frame(canvas, bg="#ffffff")
        window = canvas.create_window((0, 0), window=content_frame, anchor="nw")

        for book in self.books:
            if book["status"] == "Issued":
                # ID & Title
                tk.Label(content_frame, text=f"{book['id']}. {book['title']}",
                         font=('Calibri', 16, 'bold'), bg="#ffffff", fg='#323232',
                         anchor="w", ).pack(anchor="w", padx=12, pady=(0, 3))

                # Author
                tk.Label(content_frame, text=f"Author: {book['author']}",
                         font=("Calibri", 13, "bold"), bg="#ffffff", fg="#6f6f6f",
                         anchor="w", ).pack(anchor="w", padx=35)

                # Status
                status_color = "green" if book["status"] == "Available" else "red"
                tk.Label(content_frame, text=f"{book['status']}",
                         font=('Calibri', 15, 'bold'), fg=status_color, bg="#ffffff",
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

    def list_authors(self):
        self.clean_window()
        self.root.title("Authors")
        self.root.resizable(False, False)
        self.root.geometry("405x677")
        self.root.configure(background="#ffffff")

        back_img = Image.open("Library Images/menu_bar_img.png")
        back_img = back_img.resize((33, 33))
        self.back_img_button = ImageTk.PhotoImage(back_img)

        button_back = tk.Button(self.root, image=self.back_img_button,
                                bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
        button_back.place(x=15, y=8)

        label_authors = tk.Label(self.root, text="Authors",
                                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
        label_authors.place(x=50, y=2)

        # frame for canvas(used for divider) and scrollbar

        frame = tk.Frame(self.root, bg='#ffffff')
        frame.pack(fill="both", expand=True, pady=(54, 0))

        canvas = tk.Canvas(frame, bg="#ffffff", highlightthickness=0)
        canvas.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        canvas.configure(yscrollcommand=scrollbar.set)

        content_frame = tk.Frame(canvas, bg="#ffffff")
        window = canvas.create_window((0, 0), window=content_frame, anchor="nw")

        authors = set(book['author'] for book in self.books)
        for author in authors:
            tk.Label(content_frame, text=f"Author: {author}",
                     font=('Calibri', 15, 'bold'), bg="#ffffff", fg='#323232',
                     anchor="w", ).pack(anchor="w", padx=12, pady=(11, 15))

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

    def add_book(self):
      if self.add_win is None or not tk.Toplevel.winfo_exists(self.add_win):
        self.add_win = tk.Toplevel(self.root)
        self.add_win.title("Add Book")
        self.add_win.geometry("375x354")
        self.add_win.configure(bg="#ffffff")
        self.add_win.resizable(False, False)

        label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
        entry_style = {
            "font": ("Segoe UI", 12),
            "bg": "#f5f6fa",
            "fg": "#2d3436",
            "relief": "flat",
            "bd": 0,
            "highlightthickness": 1,
            "highlightbackground": "#dcdde1",
            "highlightcolor": "#00cec9"
        }

        label_main = tk.Label(self.add_win, text="Add Book",
                                   bg='#ffffff', fg='#323232', font=('Segoe UI', 18, 'bold'))
        label_main.place(x=130, y=16)
        label = tk.Label(self.add_win, text="Enter Title:", **label_style)
        label.pack(fill="x", padx=(29, 0), pady=(80, 7))
        self.entry = tk.Entry(self.add_win, **entry_style)
        self.entry.pack(fill="x", padx=(30, 30), ipady=8)

        label2 = tk.Label(self.add_win, text="Enter Author:", **label_style)
        label2.pack(fill="x", padx=(29, 0), pady=(24, 7))
        self.entry2 = tk.Entry(self.add_win, **entry_style)
        self.entry2.pack(fill="x", padx=(30, 30), ipady=8)

        add_button_img_1 = Image.open("Library Images/Add Book.jpg")
        add_button_img_1 = add_button_img_1.resize((111, 97))
        self.add_button_img_1 = ImageTk.PhotoImage(add_button_img_1)

        add_button_1 = tk.Button(self.add_win, image=self.add_button_img_1,
                               bg='#ffffff', relief='flat', bd=0, command=self.do_add_book, activebackground='#ffffff')
        add_button_1.place(x=131, y=258)
      else:
          self.add_win.lift()
          self.add_win.focus_force()

    def do_add_book(self):
        title = self.entry.get()
        author = self.entry2.get()
        if not title or not author:
            messagebox.showwarning("Warning", "Both fields are required.")
            return
        new_book = {
            "id" : generate_id(self.books),
            "title" : title,
            "author" : author,
            "status" : "Available",
        }
        self.books.append(new_book)
        messagebox.showinfo("Success", "Book Added.")
        save_books(self.books)
        self.add_win.destroy()
        self.dashboard()



    def issue_book(self):
      if self.issue_win is None or not tk.Toplevel.winfo_exists(self.issue_win):
        self.issue_win = tk.Toplevel(self.root)
        self.issue_win.title("Issue Book")
        self.issue_win.geometry("375x256")
        self.issue_win.configure(bg="#ffffff")
        self.issue_win.resizable(False, False)

        label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
        entry_style = {
            "font": ("Segoe UI", 12),
            "bg": "#f5f6fa",
            "fg": "#2d3436",
            "relief": "flat",
            "bd": 0,
            "highlightthickness": 1,
            "highlightbackground": "#dcdde1",
            "highlightcolor": "#00cec9"
        }

        label_main_2 = tk.Label(self.issue_win, text="Issue Book",
                                  bg='#ffffff', fg='#323232', font=('Segoe UI', 18, 'bold'))
        label_main_2.place(x=130, y=16)

        label = tk.Label(self.issue_win, text="Enter Book ID to Issue:", **label_style)
        label.pack(fill="x", padx=(29, 0), pady=(80, 7))
        self.entry_issue = tk.Entry(self.issue_win, **entry_style)
        self.entry_issue.pack(fill="x", padx=(30, 30), ipady=8)

        issue_button_img_2 = Image.open("Library Images/Issue Book.jpg")
        issue_button_img_2 = issue_button_img_2.resize((111, 97))
        self.issue_button_img_2 = ImageTk.PhotoImage(issue_button_img_2)

        issue_button_2 = tk.Button(self.issue_win, image=self.issue_button_img_2,
                                 bg='#ffffff', relief='flat', bd=0, command=self.do_issue_book, activebackground='#ffffff')
        issue_button_2.place(x=130, y=158)
      else:
          self.issue_win.lift()
          self.issue_win.focus_force()

    def do_issue_book(self):
        new_issue = self.entry_issue.get()
        if not new_issue:
            messagebox.showwarning("Warning", "Please enter a Book ID to Issue.")
            return
        if not new_issue.isdigit():
            messagebox.showwarning("Warning", "Only numbers are allowed.")
            return
        new_issue = int(new_issue)
        result = find_book_by_id(self.books, new_issue)
        if not result:
            messagebox.showwarning("Warning", f"Book not found with ID: {new_issue}")
        elif result["status"] == "Issued":
            messagebox.showwarning("Warning", f"Book already issued with ID: {new_issue}")
        else:
            result["status"] = "Issued"
            save_books(self.books)
            messagebox.showinfo("Success", "Book Issued.")

            self.issue_win.destroy()
            self.dashboard()


    def return_book(self):
      if self.return_win is None or not tk.Toplevel.winfo_exists(self.return_win):
        self.return_win = tk.Toplevel(self.root)
        self.return_win.title("Return Book")
        self.return_win.geometry("375x256")
        self.return_win.configure(bg="#ffffff")
        self.return_win.resizable(False, False)

        label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
        entry_style = {
            "font": ("Segoe UI", 12),
            "bg": "#f5f6fa",
            "fg": "#2d3436",
            "relief": "flat",
            "bd": 0,
            "highlightthickness": 1,
            "highlightbackground": "#dcdde1",
            "highlightcolor": "#00cec9"
        }

        label_main_3 = tk.Label(self.return_win, text="Return Book",
                                bg='#ffffff', fg='#323232', font=('Segoe UI', 18, 'bold'))
        label_main_3.place(x=130, y=16)

        label = tk.Label(self.return_win, text="Enter Book ID to Return:", **label_style)
        label.pack(fill="x", padx=(29, 0), pady=(80, 7))
        self.entry_return = tk.Entry(self.return_win, **entry_style)
        self.entry_return.pack(fill="x", padx=(30, 30), ipady=8)

        return_button_img_1 = Image.open("Library Images/Return Book.jpg")
        return_button_img_1 = return_button_img_1.resize((111, 97))
        self.return_button_img_1 = ImageTk.PhotoImage(return_button_img_1)

        return_button_1 = tk.Button(self.return_win, image=self.return_button_img_1,
                                  bg='#ffffff', relief='flat', bd=0, command=self.do_return_book, activebackground="#ffffff")
        return_button_1.place(x=130, y=158)
      else:
          self.return_win.lift()
          self.return_win.focus_force()

    def do_return_book(self):
        new_return = self.entry_return.get()
        if not new_return:
            messagebox.showwarning("Warning", "Please enter a Book ID to Return.")
            return
        if not new_return.isdigit():
            messagebox.showwarning("Warning", "Only numbers are allowed.")
            return
        new_return = int(new_return)
        result = find_book_by_id(self.books, new_return)
        if not result:
            messagebox.showwarning("Warning", f"Book not found with ID: {new_return}")
        elif result["status"] == "Available":
            messagebox.showwarning("Warning", f"Book already returned with ID: {new_return}")
        else:
            result["status"] = "Available"
            save_books(self.books)
            messagebox.showinfo("Success", "Book Returned.")

            self.return_win.destroy()
            self.dashboard()

    def logout(self):
          if messagebox.askokcancel("Logout", "Do you want to logout?"):
              self.show_home_page()


    def clean_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


root = tk.Tk()
play = LibraryManagementSystem(root)
root.mainloop()