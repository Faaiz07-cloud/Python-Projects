# ------------------------EMI GUI ----------------------

import tkinter as tk

def calculate():
    p = float(loan_entry.get())  # Principal
    r = float(annual_interest_rate_entry.get())  # Annual Interest Rate
    t = int(years_entry.get())  # Years

    # --- EMI Calculation ---
    monthly_rate = r / (12 * 100)  # monthly interest rate
    months = t * 12  # total number of months

    emi_value = (p * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)

    total_payment = emi_value * months
    total_interest = total_payment - p

    # --- Result Output ---
    result_label.config(
        text=f"Your monthly EMI will be: ${emi_value:,.2f}\n"
             f"Total payment after {t} years will be: ${total_payment:,.2f}\n"
             f"Out of which interest is: ${total_interest:,.2f}"
    )

root = tk.Tk()
root.title("EMI Calculator")
root.geometry("500x500")
root.resizable(False, False)
root.configure(background="#f5f5f5")

title = tk.Label(root, text="EMI Calculator",
                 font=("Verdana", 20, "bold"),
                 bg="#f5f5f5",
                 fg="#117df2")
title.pack(pady=(26,0))

loan_label = tk.Label(root, text="Enter Loan Amount:",
                 font=("Arial", 12, "bold"),
                 bg="#f5f5f5",
                 fg="#3a3a3b")
loan_label.pack(pady=(15,0))

loan_entry = tk.Entry(root, font=("Arial", 19,),
                                  bd=1,
                                  relief="solid",
                                  width=25,
                                  bg="#ffffff")
loan_entry.pack(pady=(15,0))

annual_interest_rate_label = tk.Label(root, text="Enter Annual Interest Rate (%):",
                 font=("Arial", 12, "bold"),
                 bg="#f5f5f5",
                 fg="#3a3a3b")
annual_interest_rate_label.pack(pady=(15,0))

annual_interest_rate_entry = tk.Entry(root, font=("Arial", 19),
                                  bd=1,
                                  relief="solid",
                                  width=25,
                                  bg="#ffffff")
annual_interest_rate_entry.pack(pady=(15,0))

years_label = tk.Label(root, text="Enter Loan Tenure (in years):",
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