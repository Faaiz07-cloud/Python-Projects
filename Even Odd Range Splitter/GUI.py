import tkinter as tk
from tkinter import ttk

# -------------------------- back-end functions ---------------------
def add_placeholder(entry, text):
    entry.insert(0, text)
    entry.config(fg="grey")
    entry.bind("<FocusIn>", lambda e: (entry.delete(0, "end"), entry.config(fg="black")))
    entry.bind("<FocusOut>", lambda e: (entry.insert(0, text), entry.config(fg="grey")) if entry.get() == "" else None)

def process():
    start = entry_start.get()
    end = entry_end.get()
    even_list = []
    odd_list = []

    for i in range (int(start), int(end) + 1):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    for row in tree.get_children():
        tree.delete(row)

    from itertools import zip_longest
    for even , odd in zip_longest(even_list, odd_list, fillvalue=""):
        tree.insert('', "end", values=(even, odd))

# -------------------------- back-end functions ---------------------

# ------------------------------  GUI  ---------------------------------
root = tk.Tk()
root.geometry("600x620")
root.title("Even Odd Range Splitter")
root.resizable(False, False)
root.config(bg="#f0f4c3")

# Main Title
title = tk.Label(root, text="Even Odd Range Splitter", font=("Arial", 27, "bold"))
title.config(bg="#f0f4c3", fg="#e91e63", highlightthickness=2, highlightbackground="#e91e63")
title.pack(pady=(40,0))

# Range Title
range_title = tk.Label(root, text="Enter your Range", font=("Arial", 22, "bold"))
range_title.config(bg="#f0f4c3", fg="#3f51b5")
range_title.pack(pady=(25,0))

# Frame for entries
frame = tk.Frame(root, bg="#f0f4c3")
frame.pack()

entry_start = tk.Entry(frame, width=20, font=("Arial", 14))
entry_start.grid(row=0, column=0, padx=12, pady=(20,0), sticky="ew")
add_placeholder(entry_start, "Start")

entry_end = tk.Entry(frame, width=21, font=("Arial", 14))
entry_end.grid(row=0, column=1, padx=12, pady=(20,0), sticky="ew")
add_placeholder(entry_end, "End")

# Button
button = tk.Button(text="Submit",
                   command=process,
                   font=("Arial", 14, " bold"),
                   relief="groove", width=8, height=1,
                   bg="#4caf50", fg="white",
                   activebackground="#45a049",
                   activeforeground="white")
button.pack(pady=(25,0))

# TreeView
style = ttk.Style()
style.theme_use("vista")
style.configure("Treeview.Heading", font=("Arial", 13, "bold"))
style.configure("Treeview", font=("Arial", 12))

columns = ("Even", "Odd")
tree = ttk.Treeview(root, columns=columns, show="headings", height=12)
tree.heading("Even", text="Even")
tree.heading("Odd", text="Odd")
tree.column("Even", width=220, anchor="center")
tree.column("Odd", width=220, anchor="center")
tree.pack(pady=(30,0))

root.mainloop()
# ------------------------------------- GUI -----------------------------