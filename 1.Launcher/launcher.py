import tkinter as tk
from tkinter import ttk
import subprocess

root = tk.Tk()
root.title("🚀 Project Launcher 📂")
root.geometry("600x450")
root.resizable(False, False)

# Gradient Background Function
def draw_gradient(canvas, color1, color2):
    width = 600
    height = 450
    limit = height
    (r1, g1, b1) = root.winfo_rgb(color1)
    (r2, g2, b2) = root.winfo_rgb(color2)
    r_ratio = float(r2 - r1) / limit
    g_ratio = float(g2 - g1) / limit
    b_ratio = float(b2 - b1) / limit

    for i in range(limit):
        nr = int(r1 + (r_ratio * i))
        ng = int(g1 + (g_ratio * i))
        nb = int(b1 + (b_ratio * i))
        color = "#%04x%04x%04x" % (nr, ng, nb)
        canvas.create_line(0, i, width, i, fill=color)

# Canvas for gradient
canvas = tk.Canvas(root, width=500, height=300)
canvas.pack(fill="both", expand=True)
draw_gradient(canvas, "#1e3c72", "#2a5298")  # Dark blue → Light blue gradient

# Frame on top of gradient
frame = tk.Frame(root, bg="#ffffff", bd=2, relief="ridge")
frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=200)

# Title Label
title = tk.Label(
    frame,
    text="🚀 Launch Your Project 📂",
    font=("Arial", 18, "bold"),
    bg="#ffffff",
    fg="#2c3e50"
)
title.pack(pady=15)

# Project list
projects = {
    "📁Student Report Card Generator": r"C:\Users\faaiz\PycharmProjects\Student Report Card Generator\main.py",
    "📁ATM Machine": r"C:\Users\faaiz\PycharmProjects\ATM Machine\main.py",
    "📁Contact Book": r"C:\Users\faaiz\PycharmProjects\Contact Book\GUI.py",
    "📁Word Frequency Counter": r"C:\Users\faaiz\PycharmProjects\Word Frequency Counter\GUI.py",
    "📁Rock Paper Scissors": r"C:\Users\faaiz\PycharmProjects\Rock Paper Scissors Game\GUI.py",
    "📁Even Odd Range Splitter": r"C:\Users\faaiz\PycharmProjects\Even Odd Range Splitter\GUI.py",
    "📁Number Guessing Game": r"C:\Users\faaiz\PycharmProjects\Number Guessing Game\GUI.py",
    "📁Basic Calculator": r"C:\Users\faaiz\PycharmProjects\Basic Calculator\GUI.py",
    "📁Multiplication Table Generator": r"C:\Users\faaiz\PycharmProjects\Multiplication Table Generator\GUI.py",
    "📁Simple Interest Calculator": r"C:\Users\faaiz\PycharmProjects\Simple Interest and EMI Calculator\GUI_SI.py",
    "📁EMI Calculator": r"C:\Users\faaiz\PycharmProjects\Simple Interest and EMI Calculator\GUI_EMI.py",
    "📁To-Do List Manager 1": r"C:\Users\faaiz\PycharmProjects\To-Do List Manager\GUI.py",
    "📁To-Do List Manager 2": r"C:\Users\faaiz\PycharmProjects\To-Do List Manager\GUI2.py",
    "📁Quiz Game": r"C:\Users\faaiz\PycharmProjects\Quiz Game\GUI.py",
    "📁Tic Tac Toe": r"C:\Users\faaiz\PycharmProjects\Tic Tac Toe Game\GUI.py",
    "📁Expense Tracker": r"C:\Users\faaiz\PycharmProjects\Expense Tracker\GUI_Base\main.py",
    "📁File Organizer Script": r"C:\Users\faaiz\PycharmProjects\File Organizer Script\GUI_Base\main.py",
    "📁CSV Data Analyzer": r"C:\Users\faaiz\PycharmProjects\CSV Data Reader & Analyzer\GUI_Base\main.py",
    "📁Unit Converter": r"C:\Users\faaiz\PycharmProjects\Unit Converter\GUI_Base\main.py",
    "📁Library Management System": r"C:\Users\faaiz\PycharmProjects\Library Management System\GUI_Base\main.py",
    "📁Banking System": r"C:\Users\faaiz\PycharmProjects\Banking System\GUI\main.py",
    "📁Inventory Management System": r"C:\Users\faaiz\PycharmProjects\Inventory Management System\GUI\main.py",
    "📁Weather App": r"C:\Users\faaiz\PycharmProjects\Weather App using API\GUI\main.py",
    "📁Password Manager": r"C:\Users\faaiz\PycharmProjects\Password Manager\GUI\main.py",
    "📁Digital Clock": r"C:\Users\faaiz\PycharmProjects\Digital Clock\GUI\main.py",
    "📁Chat App": r"C:\Users\faaiz\PycharmProjects\Chat App\GUI\main.py",
}

def run_project():
    choice = project_var.get()
    if choice in projects:
        subprocess.Popen(["python", projects[choice]])

# Dropdown
project_var = tk.StringVar()
project_dropdown = ttk.Combobox(
    frame,
    textvariable=project_var,
    values=list(projects.keys()),
    state="readonly",
    font=("Arial", 12)
)
project_dropdown.pack(pady=10)

# Button
btn = tk.Button(
    frame,
    text="▶ Open Project",
    command=run_project,
    font=("Arial", 12, "bold"),
    bg="#2ecc71",
    fg="white",
    activebackground="#27ae60",
    activeforeground="white",
    relief="flat",
    padx=10,
    pady=5
)
btn.pack(pady=15)

root.mainloop()