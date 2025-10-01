import os
import json
import tkinter as tk
from tkinter import messagebox, simpledialog

# -------------------------------- File Handling -------------------------------

File_Name = "GUI_tasks.json"

def load_tasks():
    if os.path.exists(File_Name):
        with open(File_Name, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(File_Name, "w") as file:
        json.dump(tasks, file, indent=4)

# -------------------------------- File Handling -------------------------------


# ------------------------------------------- Backend ------------------------------------

def refresh_listbox():
    global tasks
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, start=1):
        status = "✔️" if task["Completed"] else "❌"
        task_listbox.insert(
            tk.END, f"{i:<3} {task['Task']:<52} {status}"
        )

def add_task():
    global tasks
    task_name = simpledialog.askstring("Add Task", "Enter new Task:")
    if not task_name:
        messagebox.showwarning("Warning", "Task cannot be empty")
        return
    for task in tasks:
        if task['Task'] == task_name:
            messagebox.showerror("Error", "Task already exists")
            return
    tasks.append({"Task": task_name, "Completed": False})
    refresh_listbox()

def remove_task():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task to remove")
        return
    index = selected[0]
    confirm = messagebox.askyesno("Confirm Remove", f"Are you sure you want to remove '{tasks[index]['Task']}'?")
    if confirm:
      removed = tasks.pop(index)
      messagebox.showinfo("Removed", f"Task '{removed['Task']}' removed")
      refresh_listbox()

def mark_complete():
    selected = task_listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task to mark complete")
        return
    index = selected[0]
    confirm = messagebox.askyesno("Confirm Complete", f"Mark '{tasks[index]['Task']}' as Completed?")
    if confirm:
      tasks[index]['Completed'] = True
      messagebox.showinfo("Task Completed", f"Task '{tasks[index]['Task']}' marked as Completed")
      refresh_listbox()

def on_closing():
    save_tasks(tasks)
    root.destroy()

# ------------------------------------------- Backend ------------------------------------


# ------------------------- Tkinter GUI ------------------------------

tasks = load_tasks()
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("800x650")
root.configure(bg="#f4f6f9")
root.resizable(False, False)

# title
title_frame = tk.Frame(root, bg="#3498db", bd=1, relief="flat")
title_frame.pack(pady=(30,0))

title_label = tk.Label(title_frame, text="📝To-Do List Manager",
                       font=("Comic Sans MS", 23, "bold"),
                       bg="#3498db", fg="white")
title_label.pack(padx=20, pady=10)

# Listbox
task_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
task_frame.pack(pady=(25,0))

task_listbox = tk.Listbox(task_frame, width=60, height=18, font=("Lucida Console", 14),
                          selectbackground="#3498db", selectforeground="white",
                          relief="flat", bd=0, bg="#fdfdfd", fg="#2c3e50",
                          activestyle="dotbox")
task_listbox.pack(side="left", fill="both", padx=5, pady=5)

# Buttons frame
button_frame = tk.Frame(root, bg="#f4f6f9")
button_frame.pack(pady=(25,0))

btn_add = tk.Button(button_frame, text="➕ Add Task", width=16, height=2, command=add_task, relief="flat", bd=1 ,bg="#2ecc71", activebackground="#2ecc71", fg="white", activeforeground="white", font=("Arial", 11, "bold"))
btn_add.grid(row=0, column=0, padx=5, pady=5)

btn_remove = tk.Button(button_frame, text="❌ Remove Task", width=16, height=2, command=remove_task,relief="flat", bd=1, bg="#e74c3c",activebackground="#e74c3c", activeforeground="white", fg="white", font=("Arial", 11, "bold"))
btn_remove.grid(row=0, column=1, padx=5, pady=5)

btn_complete = tk.Button(button_frame, text="✔ Mark Complete", width=16, height=2, command=mark_complete, relief="flat", bd=1, bg="#3498db", activebackground="#3498db", activeforeground="white", fg="white", font=("Arial", 11, "bold"))
btn_complete.grid(row=0, column=2, padx=5, pady=5)

refresh_listbox()

# Closing event
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()

# ------------------------- Tkinter GUI ------------------------------