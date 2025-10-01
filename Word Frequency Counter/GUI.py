import os
import tkinter as tk
from tkinter import messagebox, filedialog, ttk

# function for button
def button_pressed():
    file_name = file_name_entry.get().strip()
    if not file_name:
        messagebox.showerror("Error", "Please enter a file name")
        return
    lines = [
        "Artificial intelligence is shaping the future of technology.",
        "People around the world are adopting new digital solutions.",
        "Programming languages are evolving with modern frameworks.",
        "Students often practice coding by building simple projects.",
        "Collaboration and teamwork make software development easier.",
        "Cloud platforms allow businesses to scale quickly.",
        "Cybersecurity is becoming more important every single day.",
        "Machine learning enables computers to recognize patterns.",
        "Mobile applications help us stay connected wherever we go.",
        "Innovation continues to drive progress in every industry."
    ]

    if not os.path.isfile(file_name):
        with open(file_name, "w") as file:
            for line in lines:
                file.write(line + "\n")
            messagebox.showinfo("Success", f"{file_name} was successfully created")
    else:
        messagebox.showwarning("Warning", f"{file_name} already exists!")

    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            content = file.read()

        word_count = {}
        for word in content.split():
            word = word.lower().strip("!@#$%^&*()-}{[]|?><:")
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1

        for row in tree.get_children():
            tree.delete(row)

        for key, value in word_count.items():
            tree.insert("", "end", values=(key, value))


# GUI
root = tk.Tk()
root.geometry("540x550")
root.title("Word Frequency Counter")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

# title label
title_label = tk.Label(root, text="📝Word Frequency Counter", bg="#FFFFFF", fg="#000000",
                       font=("Times New Roman", 21, "bold"), highlightthickness=2, highlightbackground="black")
title_label.pack(pady=20)

# frame for label and entry of file
form_frame = tk.Frame(root, bg="#f5f5f5")
form_frame.pack(padx=20, pady=12, anchor="w", )

# label of file name
file_name_label = tk.Label(
    form_frame, text="Enter File Name: ",
    font=("Times New Roman", 16, "bold"),
    bg="#f5f5f5",
    fg="#000000",
)
file_name_label.grid(row=0, column=0, sticky="w", padx=(17, 0))

# entry of file
file_name_entry = tk.Entry(form_frame, bg="#FFFFFF", fg="#000000", width=22, font=("Times New Roman", 16))
file_name_entry.grid(row=0, column=1, sticky="w", padx=(7, 0))

# button styling
button_style = {"width": 12,
                "height": 2,
                "bd": 0,
                "relief": "raised"}
button = tk.Button(form_frame, text="Process File", bg="#2ecc71", fg="#ffffff", font=("Times New Roman", 11, "bold"),
                   **button_style, command=button_pressed)
button.grid(row=1, column=1, sticky="e", pady=10)

# styling for tree view
style = ttk.Style()
style.configure("Treeview.Heading", font=("Times New Roman", 12, "bold"))
style.configure("Treeview", font=("Times New Roman", 11))

# tree view
columns = ("Word", "Count")
tree = ttk.Treeview(root, columns=columns, style="Treeview", height=13, show="headings")
tree.heading("Word", text="Word")
tree.heading("Count", text="Count")
tree.column("Word", width=200, anchor="w")
tree.column("Count", width=200, anchor="w")
tree.pack(pady=(10, 0))

root.mainloop()
