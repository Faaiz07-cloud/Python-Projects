import os
import json
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk

# File Handling for Login & SignUp
users_file = "users2.json"

def load_users():
    if os.path.exists(users_file):
        with open(users_file, "r") as f:
            return json.load(f)
    return []

def save_users(users):
    with open(users_file, "w") as f:
        json.dump(users, f, indent=4)

# File Handling for Inventory

def get_inventory_file(username):
    if not username:
        return "inventory.json"
    return f"{username}_inventory.json"

def load_inventory(username):
    user_inventory = get_inventory_file(username)
    if os.path.exists(user_inventory):
        with open(user_inventory, "r") as f:
            return json.load(f)
    return []

def save_inventory(username, inventory):
    user_inventory = get_inventory_file(username)
    with open(user_inventory, "w") as f:
        json.dump(inventory, f, indent=4)


# Class
class Inventory:
    def __init__(self, root):
        self.root = root
        self.root.geometry("325x625")
        self.current_username = None
        self.users = load_users()
        self.inventory = []
        self.add_product_window = None
        self.product_images = None
        self.selected_image = None
        self.login_page()
        # self.dashboard()

    def login_page(self):
        self.clean_window()
        self.root.geometry("325x625")
        self.root.title("StockUp - Login")
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)

        img_1 = Image.open("Inventory Images/splash.png")
        img_1 = img_1.resize((335, 225))
        self.splash_img = ImageTk.PhotoImage(img_1)

        label = tk.Label(self.root, image=self.splash_img, bg="#ffffff")
        label.pack(pady=(30, 0))

        label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
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

        username_label = tk.Label(self.root, text="Username", **label_style)
        username_label.pack(fill="x", padx=(29, 0), pady=(12, 7))
        self.username_entry = tk.Entry(self.root, **entry_style)
        self.username_entry.pack(fill="x", padx=(30, 30), ipady=8)

        pass_label = tk.Label(self.root, text="Password", **label_style)
        pass_label.pack(fill="x", padx=(29, 0), pady=(32, 7))
        self.pass_entry = tk.Entry(self.root, **entry_style, show="*")
        self.pass_entry.pack(fill="x", padx=(30, 30), ipady=8)

        login_img = Image.open("Inventory Images/login.png")
        login_img = login_img.resize((95, 60))
        self.login_img_button = ImageTk.PhotoImage(login_img)

        login_button = tk.Button(self.root, image=self.login_img_button,
                                 bg='#ffffff', relief='flat', bd=0, command=self.login, activebackground="#ffffff")
        login_button.place(x=112, y=484)

        self.root.bind("<Return>", lambda e: self.login())

        label_2 = tk.Label(self.root, text="Don't have an account?", bg="#ffffff", font=("Segoe UI", 11))
        label_2.place(x=51, y=560)

        signup_button = tk.Button(self.root, text="SignUp", font=("Segoe UI", 11, "bold"),
                                  bg='#ffffff', relief='flat', bd=0, command=self.signup_page,
                                  activebackground="#ffffff")
        signup_button.place(x=208, y=558)

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
                    self.inventory = load_inventory(self.current_username)
                    messagebox.showinfo("Success", "You have been successfully logged in.")
                    self.dashboard()
                    return
                else:
                    messagebox.showerror("Error", "Invalid Password!")
                    return

        messagebox.showwarning("Warning", f"No account for '{username}'. Please sign up or retry.")

    def signup_page(self):
        self.clean_window()
        self.root.geometry("325x625")
        self.root.title("StockUp - SignUp")
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)

        img_1 = Image.open("Inventory Images/splash.png")
        img_1 = img_1.resize((335, 225))
        self.splash_img = ImageTk.PhotoImage(img_1)

        label = tk.Label(self.root, image=self.splash_img, bg="#ffffff")
        label.pack(pady=(30, 0))

        label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
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

        username_label = tk.Label(self.root, text="Username", **label_style)
        username_label.pack(fill="x", padx=(29, 0), pady=(12, 7))
        self.username_entry = tk.Entry(self.root, **entry_style)
        self.username_entry.pack(fill="x", padx=(30, 30), ipady=8)

        pass_label = tk.Label(self.root, text="Password", **label_style)
        pass_label.pack(fill="x", padx=(29, 0), pady=(32, 7))
        self.pass_entry = tk.Entry(self.root, **entry_style, show="*")
        self.pass_entry.pack(fill="x", padx=(30, 30), ipady=8)

        signup_img = Image.open("Inventory Images/signup.png")
        signup_img = signup_img.resize((95, 56))
        self.signup_img_button = ImageTk.PhotoImage(signup_img)

        signup_button = tk.Button(self.root, image=self.signup_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.signup, activebackground="#ffffff")
        signup_button.place(x=112, y=484)

        self.root.bind("<Return>", lambda e: self.signup())

        label_2 = tk.Label(self.root, text="Already have an account?", bg="#ffffff", font=("Segoe UI", 11))
        label_2.place(x=51, y=560)

        login_button = tk.Button(self.root, text="Login", font=("Segoe UI", 11, "bold"),
                                  bg='#ffffff', relief='flat', bd=0, command=self.login_page,
                                  activebackground="#ffffff")
        login_button.place(x=222, y=558)

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
        self.root.geometry("330x690")
        self.root.title("Dashboard")
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)

        label_hello = tk.Label(self.root, text="Hello,", font=("Segoe UI", 18, "bold"), bg="#ffffff", fg="#c5c7c2")
        label_hello.place(x=25, y=8)
        label_name = tk.Label(self.root, text=self.current_username, font=("Segoe UI", 20, "bold"),
                              bg="#ffffff", fg="#272815")
        label_name.place(x=25, y=40)

        logout_img = Image.open("Inventory Images/logout.png")
        logout_img = logout_img.resize((103, 80))
        self.logout_img_button = ImageTk.PhotoImage(logout_img)

        logout_button = tk.Button(self.root, image=self.logout_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.logout, activebackground="#ffffff")
        logout_button.place(x=209, y=10)

        frame = Image.open("Inventory Images/frame 1.png")
        frame = frame.resize((305, 87))
        self.frame = ImageTk.PhotoImage(frame)

        label_frame_pic = tk.Label(self.root, image=self.frame, bg="#ffffff")
        label_frame_pic.place(x=8, y=110)

        label_total_stock = tk.Label(self.root, text="Total Stock", bg="#2c3e50", fg="#ffffff",
                          font=("Calibri", 15, "bold"))
        label_total_stock.place(x=30, y=125)
        total_stock = sum(float(product['price']) for product in self.inventory) if self.inventory else 0
        label_amount = tk.Label(self.root, text=f"${total_stock:,.2f}", bg="#2c3e50", fg="#ffffff",
                          font=("Calibri", 20, "bold"))
        label_amount.place(x=30, y=151)

        label_recent_stock = tk.Label(self.root, text="Recent Stock", bg="#ffffff", fg="#222222", font=("Calibri", 17, "bold"))
        label_recent_stock.place(x=21, y=216)


        button = tk.Button(self.root, text="View All", bg="#ffffff", fg="#6f6f6f", font=("Calibri", 12, "bold"),
                           relief="flat", bd=0, command=self.all_stock)
        button.place(x=238, y=221)

        self.product_images = []
        y_axis = 270
        spacing = 178  # frame height + some vertical gap
        last_2_stocks = self.inventory[-2:] if self.inventory else []

        if not self.inventory:
            tk.Label(self.root, text="No recent stock!",
                              bg='#ffffff', fg='#6f6f6f', font=('Calibri', 15, 'bold')).place(x=88,y=350)

        for i, stock in enumerate(reversed(last_2_stocks)):  # reverse so latest is on top
            frame2 = tk.Frame(self.root, bg="#ffffff", width=310, height=163)
            frame2.place(x=15, y=y_axis + i * spacing)

            image = stock.get('image')
            if image and os.path.exists(image):
                    img = Image.open(image)
                    img = img.resize((120, 150))
                    self.img = ImageTk.PhotoImage(img)
                    self.product_images.append(self.img)
                    tk.Label(frame2, image=self.img, bg="#ffffff").place(x=5, y=5)
            else:
                    tk.Label(frame2, text="No Image", bg="#ffffff", fg="#888", font=("Calibri", 13, "bold")).place(x=8, y=66)

            label_name = tk.Label(frame2, text="Name:", bg="#ffffff", fg="#222222", font=("Calibri", 13, "bold"))
            label_name.place(x=150, y=16)
            name = stock.get('name')
            label_name_get = tk.Label(frame2, text=name, bg="#ffffff", fg="#222222", font=("Calibri", 13,))
            label_name_get.place(x=207, y=16)

            label_price = tk.Label(frame2, text="Price:", bg="#ffffff", fg="#222222", font=("Calibri", 13, "bold"))
            label_price.place(x=150, y=47)
            price = stock.get('price')
            label_price_get = tk.Label(frame2, text=price, bg="#ffffff", fg="#222222", font=("Calibri", 13,))
            label_price_get.place(x=207, y=47)

            label_stock = tk.Label(frame2, text="Stock:", bg="#ffffff", fg="#222222", font=("Calibri", 13, "bold"))
            label_stock.place(x=150, y=78)
            qty = stock.get('quantity')
            label_stock_get = tk.Label(frame2, text=qty, bg="#ffffff", fg="#222222", font=("Calibri", 13,))
            label_stock_get.place(x=207, y=78)

            label_supplier = tk.Label(frame2, text="Supplier:", bg="#ffffff", fg="#222222", font=("Calibri", 13, "bold"))
            label_supplier.place(x=150, y=109)
            supplier = stock.get('supplier')
            label_supplier_get = tk.Label(frame2, text=supplier, bg="#ffffff", fg="#222222", font=("Calibri", 13,))
            label_supplier_get.place(x=223, y=109)

        add_img = Image.open("Inventory Images/add.png")
        add_img = add_img.resize((60, 60))
        self.add_img_button = ImageTk.PhotoImage(add_img)

        add_button = tk.Button(self.root, image=self.add_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.add_product_page, activebackground="#ffffff")
        add_button.place(x=245, y=613)


    def add_product_page(self):
       if self.add_product_window is None or not tk.Toplevel.winfo_exists(self.add_product_window):
           self.add_product_window = tk.Toplevel(self.root)
           self.add_product_window.title("Add Product")
           self.add_product_window.geometry("325x682")
           self.add_product_window.resizable(False, False)
           self.add_product_window.config(bg="#ffffff")

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

           label_main = tk.Label(self.add_product_window, text="Add Product",
                                 bg='#ffffff', fg='#323232', font=('Segoe UI', 16, 'bold'))
           label_main.place(x=23, y=16)

           label_product_id = tk.Label(self.add_product_window, text="ID", **label_style)
           label_product_id.pack(fill="x", padx=(31, 0), pady=(65, 4))
           self.entry_product_id = tk.Entry(self.add_product_window, **entry_style)
           self.entry_product_id.pack(fill="x", padx=(30, 30), pady=(0, 18), ipady=6)

           label_product_name = tk.Label(self.add_product_window, text="Name", **label_style)
           label_product_name.pack(fill="x", padx=(31, 0), pady=(0, 4))
           self.entry_product_name = tk.Entry(self.add_product_window, **entry_style)
           self.entry_product_name.pack(fill="x", padx=(30, 30), pady=(0, 18), ipady=6)

           label_product_price = tk.Label(self.add_product_window, text="Price", **label_style)
           label_product_price.pack(fill="x", padx=(31, 0), pady=(0, 4))
           self.entry_product_price = tk.Entry(self.add_product_window, **entry_style)
           self.entry_product_price.pack(fill="x", padx=(30, 30), pady=(0, 18), ipady=6)

           label_product_quantity = tk.Label(self.add_product_window, text="Quantity", **label_style)
           label_product_quantity.pack(fill="x", padx=(31, 0), pady=(0, 4))
           self.entry_product_quantity = tk.Entry(self.add_product_window, **entry_style)
           self.entry_product_quantity.pack(fill="x", padx=(30, 30), pady=(0, 18), ipady=6)

           label_product_supplier = tk.Label(self.add_product_window, text="Supplier", **label_style)
           label_product_supplier.pack(fill="x", padx=(31, 0), pady=(0, 4))
           self.entry_product_supplier = tk.Entry(self.add_product_window, **entry_style)
           self.entry_product_supplier.pack(fill="x", padx=(30, 30), pady=(0, 18), ipady=6)

           image_upload_img = Image.open("Inventory Images/image upload.png")
           image_upload_img = image_upload_img.resize((55, 56))
           self.image_upload_img_button = ImageTk.PhotoImage(image_upload_img)

           image_upload_button = tk.Button(self.add_product_window, image=self.image_upload_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=self.select_image, activebackground="#ffffff")
           image_upload_button.place(x=130, y=465)

           self.selected_image = None
           self.img_preview = tk.Label(self.add_product_window, text="No Image Selected",
                                    bg="#f5f6fa", fg="#353b48", font=("Calibri", 12, "bold"),
                                    highlightthickness=1, highlightbackground="#dcdde1")
           self.img_preview.place(x=30, y=529, width=265, height=120)

           add_button_img = Image.open("Inventory Images/add.png")
           add_button_img = add_button_img.resize((60,60))
           self.add_button_img = ImageTk.PhotoImage(add_button_img)

           add_button = tk.Button(self.add_product_window, image=self.add_button_img,
                                    bg='#ffffff', relief='flat', bd=0, command=self.add,
                                    activebackground='#ffffff')
           add_button.place(x=248, y=7)

       else:
           self.add_product_window.lift()
           self.add_product_window.focus_force()

    def select_image(self):
        file_path = filedialog.askopenfilename(
            title="Select Product Image",
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
        )
        if file_path:
            self.selected_image = file_path
            img = Image.open(file_path)
            img = img.resize((265, 120), Image.LANCZOS)
            self.img = ImageTk.PhotoImage(img)
            self.img_preview.config(image=self.img, text="")

    def add(self):
        p_id = self.entry_product_id.get()
        p_name = self.entry_product_name.get()
        p_price = self.entry_product_price.get()
        p_quantity = self.entry_product_quantity.get()
        p_supplier = self.entry_product_supplier.get()

        if not p_id or not p_name or not p_price or not p_quantity or not p_supplier:
            messagebox.showwarning("Warning", "Please fill all fields!")
            return

        for product in self.inventory:
            if product['id'] == p_id:
                messagebox.showwarning("Warning",f"P-ID {p_id} already exists!")
                return

        try:
            float(p_price)
        except:
            messagebox.showwarning("Warning", "Please enter a valid price. Must be a number.")
            return

        new_product = {
            "id": p_id,
            "name": p_name,
            "price": p_price,
            "quantity": p_quantity,
            "supplier": p_supplier,
            "image": self.selected_image if self.selected_image else ""
        }
        self.inventory.append(new_product)
        save_inventory(self.current_username, self.inventory)
        messagebox.showinfo("Success", "Product added to inventory.")
        self.dashboard()

    def all_stock(self):
        self.clean_window()
        self.root.title("Inventory")
        self.root.resizable(False, False)
        self.root.geometry("340x680")
        self.root.configure(background="#ffffff")

        back_img = Image.open("Inventory Images/menu_bar_img.png")
        back_img = back_img.resize((33, 33))
        self.back_img_button = ImageTk.PhotoImage(back_img)

        button_back = tk.Button(self.root, image=self.back_img_button,
                                bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
        button_back.place(x=15, y=8)

        label_main = tk.Label(self.root, text="Inventory",
                              bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
        label_main.place(x=50, y=2)

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

        self.product_images = []
        y_axis = 10
        spacing = 178  # frame height + some vertical gap

        if not self.inventory:
            tk.Label(self.root, text="Inventory is empty!",
                              bg='#ffffff', fg='#6f6f6f', font=('Calibri', 17, 'bold')).pack(pady=150)

        for i, stock in enumerate(self.inventory):
            frame2 = tk.Frame(scroll_frame, bg="#ffffff", width=310, height=163)
            frame2.pack(pady=8, padx=(13,0))

            image = stock['image']
            if image and os.path.exists(image):
                img = Image.open(image)
                img = img.resize((120, 150))
                self.img = ImageTk.PhotoImage(img)
                self.product_images.append(self.img)
                tk.Label(frame2, image=self.img, bg="#ffffff").place(x=5, y=5)
            else:
                tk.Label(frame2, text="No Image", bg="#ffffff", fg="#888", font=("Calibri", 13, "bold")).place(x=8,
                                                                                                               y=66)

            label_name = tk.Label(frame2, text="Name:", bg="#ffffff", fg="#222222", font=("Calibri", 13, "bold"))
            label_name.place(x=150, y=16)
            tk.Label(frame2, text=stock['name'], bg="#ffffff", fg="#222222", font=("Calibri", 13,)).place(x=207, y=16)

            label_price = tk.Label(frame2, text="Price:", bg="#ffffff", fg="#222222", font=("Calibri", 13, "bold"))
            label_price.place(x=150, y=47)
            tk.Label(frame2, text=stock['price'], bg="#ffffff", fg="#222222", font=("Calibri", 13,)).place(x=207, y=47)

            label_stock = tk.Label(frame2, text="Stock:", bg="#ffffff", fg="#222222", font=("Calibri", 13, "bold"))
            label_stock.place(x=150, y=78)
            tk.Label(frame2, text=stock['quantity'], bg="#ffffff", fg="#222222", font=("Calibri", 13,)).place(x=207,y=78)

            label_supplier = tk.Label(frame2, text="Supplier:", bg="#ffffff", fg="#222222",font=("Calibri", 13, "bold"))
            label_supplier.place(x=150, y=109)
            tk.Label(frame2, text=stock['supplier'], bg="#ffffff", fg="#222222", font=("Calibri", 13,)).place(x=223,y=109)

    def logout(self):
        if messagebox.askokcancel("Logout", "Do you want to logout?"):
            self.login_page()

    def clean_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
run = Inventory(root)
root.mainloop()