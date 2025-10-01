import tkinter as tk
import json, os

# ----------------- File Handling -----------------
File_Name = "GUI_tasks2.json"

def load_tasks():
    if os.path.exists(File_Name):
        with open(File_Name, "r") as file:
            return json.load(file)
    return []

def save_tasks():
    with open(File_Name, "w") as file:
        json.dump(tasks, file, indent=4)

# ----------------- Functions -----------------
def add_task():
    task_text = task_entry.get().strip()
    if task_text:
        # Check if already exists
        for task in tasks:
            if task['Task'] == task_text:
                return
        tasks.append({"Task": task_text, "Completed": False})
        create_task(task_text, False)
        task_entry.delete(0, tk.END)

def create_task(text, completed):
    task_frame = tk.Frame(task_list, bg="white")
    task_frame.pack(fill="x", pady=3)

    var = tk.IntVar(value=1 if completed else 0)

    # Checkbox
    check = tk.Checkbutton(
        task_frame, variable=var, bg="white",
        command=lambda: toggle_task(var, label, text)
    )
    check.pack(side="left", padx=5)

    # Task label
    label = tk.Label(task_frame, text=text, bg="white", fg="#333",
                     font=("Arial", 12), anchor="w")
    label.pack(side="left", fill="x", expand=True, padx=(2, 0))

    # Apply completed state
    if completed:
        label.config(fg="gray", font=("Arial", 12, "overstrike"))

    # Delete button
    delete_btn = tk.Button(task_frame, text="✘", bg="white", fg="red",
                           bd=0, font=("Arial", 12, "bold"),
                           command=lambda: remove_task(task_frame, text))
    delete_btn.pack(side="right", padx=5)

def toggle_task(var, label, text):
    for task in tasks:
        if task['Task'] == text:
            task['Completed'] = bool(var.get())
            break
    if var.get():
        label.config(fg="gray", font=("Arial", 12, "overstrike"))
    else:
        label.config(fg="#333", font=("Arial", 12, "normal"))

def remove_task(frame, text):
    global tasks
    tasks = [task for task in tasks if task['Task'] != text]
    frame.destroy()

def load_all_tasks():
    for task in tasks:
        create_task(task["Task"], task["Completed"])

def on_closing():
    save_tasks()
    root.destroy()

# ----------------- Main UI -----------------
tasks = load_tasks()

root = tk.Tk()
root.title("To-Do List")
root.geometry("600x600")
root.config(bg="#2c2c54")
root.resizable(False, False)

# Main container
container = tk.Frame(root, bg="white", bd=0, relief="flat")
container.pack(pady=50, padx=40, fill="both", expand=True)

# Title
title = tk.Label(container, text="To-Do List 📝",
                 font=("Arial", 16, "bold"), fg="#2c3e50", bg="white")
title.pack(pady=12)

# Input field and add button
input_frame = tk.Frame(container, bg="white")
input_frame.pack(pady=10, padx=10, fill="x")

task_entry = tk.Entry(input_frame, font=("Arial", 12), bd=0, relief="flat",
                      highlightthickness=1, highlightbackground="#ddd")
task_entry.pack(side="left", fill="x", expand=True, ipady=6, padx=(0, 5))

add_btn = tk.Button(input_frame, text="Add", bg="#ff5e57", fg="white",
                    font=("Arial", 12, "bold"), bd=0,
                    activebackground="#ff3f34", activeforeground="white",
                    command=add_task)
add_btn.pack(side="right", ipadx=15, ipady=6)

# Task list area
task_list = tk.Frame(container, bg="white")
task_list.pack(pady=10, fill="both", expand=True)

# Load previous tasks
load_all_tasks()

# Save on closing
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
