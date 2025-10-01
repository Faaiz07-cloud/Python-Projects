# -------------------------  Contact Book  ----------------------------

# -------------------------  modules  --------------------------------

# module for interacting with os features - os
import os

# module for interacting with json files - json
import json

# module for making GUI - tkinter
import tkinter as tk

# from tkinter module import classes - message_box, simple_dialogue, ttk
from tkinter import messagebox, simpledialog, ttk

# -------------------------  modules  --------------------------------

Contact_File = "GUI_contacts.txt" # .txt file that stores all contacts

# -----------------------  backend  ----------------------------------

# function for load contacts from .txt file

def load_contacts():
    if os.path.exists(Contact_File):
        with open(Contact_File, "r") as f:
            return json.load(f)
    return {}

#  function for saving operations (add, update, del) into .txt file

def save_contacts(contacts):
    with open(Contact_File, "w") as f:
        json.dump(contacts, f)

# -----------------------  backend  ----------------------------------


# -------------------  GUI Functions (When Button Clicked)  -----------------------

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter name:")
    if not name:
        return
    if name in contacts:
        messagebox.showwarning("Error", "That name already exists!")
        return
    phone = simpledialog.askstring("Add Contact", "Enter phone number:")
    if phone:
        contacts[name] = phone
        refresh_list()
        messagebox.showinfo("Success", "Contact added!")

def search_contact():
    name = simpledialog.askstring("Search Contact", "Enter name:")
    if name in contacts:
        messagebox.showinfo("Found", f"{name}: {contacts[name]}")
    else:
        messagebox.showwarning("Not Found", "No such contact")

def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter name:")
    if name in contacts:
        del contacts[name]
        refresh_list()
        messagebox.showinfo("Deleted", "Contact deleted!")
    else:
        messagebox.showwarning("Not Found", "No such contact")

def update_contact():
    old_name = simpledialog.askstring("Update Contact", "Enter old name:")
    if old_name in contacts:
        new_name = simpledialog.askstring("Update Contact", "Enter new name:")
        new_phone = simpledialog.askstring("Update Contact", "Enter new phone:")
        if new_name and new_phone:
            del contacts[old_name]
            contacts[new_name] = new_phone
            refresh_list()
            messagebox.showinfo("Updated", "Contact updated!")
    else:
        messagebox.showwarning("Not Found", "No such contact")

def refresh_list():
    # Clear old items
    for row in tree.get_children():
        tree.delete(row)

    if contacts:
        for key, value in contacts.items():
            tree.insert("", tk.END, values=(key, value))
    else:
        tree.insert("", tk.END, values=("No contacts", ""))

def on_exit():
    save_contacts(contacts)
    root.destroy()


# -------------------  GUI Functions (When Button Clicked)  -----------------------


# ---------------------------------  Main GUI  ------------------------------------

contacts = load_contacts()

root = tk.Tk() # custom tkinter
root.resizable(False, False)
root.geometry("550x660")
root.config(bg="#f5f5f5")
root.title("📒 Contact Book")

# Title Label - Contact Book
Title = tk.Label(root, text="My Contact Book", font=("Arial", 25, "bold"), bg="#f5f5f5", fg="#2c3e50")
Title.pack(pady=15)

# Configuring style for displaying contacts in tree-view
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
style.configure("Treeview", font=("Arial", 10))

# Creating Treeview (Table) for displaying name, phone of contacts
columns = ("Name", "Phone")
tree = ttk.Treeview(root, columns=columns, show="headings", height=15)
tree.heading("Name", text="Name")
tree.heading("Phone", text="Phone")
tree.column("Name", width=150, anchor="w")
tree.column("Phone", width=150, anchor="w")
tree.pack(pady=10)

# Buttons Frame
Buttons_frame = tk.Frame(root, bg="#f5f5f5")
Buttons_frame.pack(pady=15)

# Buttons Style
Button_Style = {
    "width": 12,
    "height": 2,
    "relief": "ridge",
    "bd": 0,
    "font": ("Arial", 12, "bold")
}

btn_add = tk.Button(Buttons_frame, text="➕ Add", bg="#2ecc71", fg="white", command=add_contact, **Button_Style)
btn_add.grid(row=0, column=0, padx=10, pady=10)

btn_search = tk.Button(Buttons_frame, text="🔍 Search", bg="#3498db", fg="white", command=search_contact, **Button_Style)
btn_search.grid(row=0, column=1, padx=10, pady=10)

btn_delete = tk.Button(Buttons_frame, text="✏️ Update", bg="#f39c12", fg="white", command=update_contact, **Button_Style)
btn_delete.grid(row=1, column=0, padx=10, pady=10)

btn_update = tk.Button(Buttons_frame, text="🗑 Delete", bg="#e74c3c", fg="white", command=delete_contact, **Button_Style)
btn_update.grid(row=1, column=1, padx=10, pady=10)

btn_exit = tk.Button(root, text="🚪 Exit", bg="#7f8c8d", fg="white", command=on_exit, **Button_Style)
btn_exit.pack(pady=10)

refresh_list()
root.protocol("WM_DELETE_WINDOW", on_exit)
root.mainloop()

# ---------------------------------  Main GUI  ------------------------------------
