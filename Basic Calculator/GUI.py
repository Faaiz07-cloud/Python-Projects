import tkinter as tk

# ------------------------------- Backend ------------------------------
def click(button_text):
    if button_text == "C":
        entry_var.set("")
    elif button_text == "=":
        try:
            result = str(eval(entry_var.get()))
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    else:
        entry_var.set(entry_var.get() + button_text)

# -------------------------------- GUI ---------------------------------
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("320x415")
root.resizable(False, False)
root.configure(background="#F5F5F5")

entry_var = tk.StringVar()

entry = tk.Entry(root,
                 textvariable=entry_var,
                 font=("Arial", 18),
                 bd=1,
                 relief="sunken",
                 justify="right")
entry.pack(fill="x", ipadx=8, ipady=10, padx=5, pady=(17, 13))

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

frame = tk.Frame(root, bg="#F5F5F5")
frame.pack(expand=True, fill="both")

# Default button colors
btn_bg = "#E0E0E0"
btn_fg = "#333333"
btn_active = "#BDBDBD"

for r, row in enumerate(buttons):
    for c, b in enumerate(row):
        # Special colors for C and =
        if b == "C":
            color_bg = "#EF5350"      # Red
            active_color = "#E53935"
            color_fg = "white"
        elif b == "=":
            color_bg = "#66BB6A"      # Green
            active_color = "#43A047"
            color_fg = "white"
        else:
            color_bg = btn_bg
            active_color = btn_active
            color_fg = btn_fg

        btn = tk.Button(
            frame, text=b,
            font=("Arial", 14, "bold"),
            fg=color_fg, bg=color_bg, activebackground=active_color,
            relief="solid", bd=1,
            command=lambda x=b: click(x)
        )
        btn.grid(row=r, column=c, sticky="nsew",
                 padx=5, pady=5, ipadx=5, ipady=15)

for i in range(4):
    frame.grid_rowconfigure(i, weight=1)
    frame.grid_columnconfigure(i, weight=1)

root.mainloop()


