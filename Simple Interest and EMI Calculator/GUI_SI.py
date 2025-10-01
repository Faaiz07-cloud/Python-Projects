# ------------------------Simple Interest GUI ----------------------

import tkinter as tk

def calculate():
    p = float(principal_amount_entry.get())
    r = float(annual_interest_entry.get())
    t = float(years_entry.get())
    si = (p * r * t) / 100
    final_amount = p + si

    result_label.config(text=f"After {t} years, your investment will be worth\n${final_amount} with simple interest")


root = tk.Tk()
root.title("Simple Interest Calculator")
root.geometry("500x500")
root.resizable(False, False)
root.configure(background="#f5f5f5")

title = tk.Label(root, text="Simple Interest Calculator",
                 font=("Verdana", 20, "bold"),
                 bg="#f5f5f5",
                 fg="#117df2")
title.pack(pady=(26,0))

principal_amount_label = tk.Label(root, text="Principal Amount ($):",
                 font=("Arial", 12, "bold"),
                 bg="#f5f5f5",
                 fg="#3a3a3b")
principal_amount_label.pack(pady=(15,0))

principal_amount_entry = tk.Entry(root, font=("Arial", 19,),
                                  bd=1,
                                  relief="solid",
                                  width=25,
                                  bg="#ffffff")
principal_amount_entry.pack(pady=(15,0))

annual_interest_label = tk.Label(root, text="Annual Interest Rate (%):",
                 font=("Arial", 12, "bold"),
                 bg="#f5f5f5",
                 fg="#3a3a3b")
annual_interest_label.pack(pady=(15,0))

annual_interest_entry = tk.Entry(root, font=("Arial", 19),
                                  bd=1,
                                  relief="solid",
                                  width=25,
                                  bg="#ffffff")
annual_interest_entry.pack(pady=(15,0))

years_label = tk.Label(root, text="Number of Years:",
                 font=("Arial", 12, "bold"),
                 bg="#f5f5f5",
                 fg="#3a3a3b")
years_label.pack(pady=(15,0))

years_entry = tk.Entry(root, font=("Arial", 19),
                                  bd=1,
                                  relief="solid",
                                  width=25,
                                  bg="#ffffff")
years_entry.pack(pady=(15,0))

button = tk.Button(root, text="Calculate",
                   width=29,
                   bg="#117df2",
                   fg="white",
                   font=("Arial", 15, "bold"),
                   activebackground="#117df2",
                   activeforeground="white",
                   height=1,
                   relief="ridge",
                   command=calculate)
button.pack(pady=(26,0))

result_label = tk.Label(root, text="",
                 font=("Arial", 12,),
                 bg="#f5f5f5",
                 fg="#3a3a3b")
result_label.pack(pady=(23,0))

root.mainloop()