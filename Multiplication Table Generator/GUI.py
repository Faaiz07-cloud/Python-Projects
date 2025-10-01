import tkinter as tk

# ---------------------------- backend --------------------------------
def generate_table():
    for row in frame2.winfo_children():
        row.destroy()
    try:
      user = int(entry1.get())
      upto = int(entry2.get())

      header_font = ("Arial", 13, "bold")
      header_bg = "#4A90E2"
      header_fg = "white"

      tk.Label(frame2, text="EXPRESSION", font=header_font,
               bg=header_bg, fg=header_fg, padx=40, pady=11).grid(row=0, column=0, sticky="nsew")

      tk.Label(frame2, text="RESULT", font=header_font,
               bg=header_bg, fg=header_fg, padx=40, pady=11).grid(row=0, column=1, sticky="nsew")

      for i in range(1, upto + 1):
          expression = f"{user} × {i}"
          result = user * i

          # for separate row visibility
          row_bg = "#FFFFFF" if i % 2 == 1 else "#F9F9F9"

          expression_label = tk.Label(frame2, text=expression,
                                      font=("Arial", 13,),
                                      bg=row_bg, padx=70, pady=10)
          expression_label.grid(row=i, column=0, padx=(0, 2), pady=(0, 1), sticky="ew")

          result_label = tk.Label(frame2, text=result,
                                  font=("Arial", 13),
                                  bg=row_bg, padx=70, pady=10)
          result_label.grid(row=i, column=1, padx=(2, 0), pady=(0, 1), sticky="ew")

      frame2.grid_columnconfigure(0, weight=1)
      frame2.grid_columnconfigure(1, weight=1)

    except ValueError:
        for row in frame2.winfo_children():
            row.destroy()

        tk.Label(frame2, text="⚠️ Please enter valid numbers!",
                 font=("Arial", 13, "bold"), fg="red", bg="#F0F0F0").pack(pady=20)

# ------------------------------ GUI ---------------------------------
root = tk.Tk()
root.title("Multiplication Table Generator")
root.geometry("1000x650")
root.resizable(True, True)
root.configure(background="#E0E0E0")

title = tk.Label(root,
                text="Multiplication Table Generator",
                font=("Arial", 25, "bold"),
                bg="#E0E0E0",
                fg="#2c3f53")
title.pack(pady=(25,0))

frame = tk.Frame(root, bg="#E0E0E0")
frame.pack(pady=(15,0))

label1 = tk.Label(frame,
                  text="Table for",
                  font=("Arial", 15, "bold"),
                  bg="#E0E0E0",
                  fg="#2c3f53")
label1.grid(row=0, column=0, padx=10)

entry1 = tk.Entry(frame,
                  width=6,
                  font=("Arial", 20, "bold"),
                  bg="#ffffff",
                  fg="black",
                  bd=1,
                  relief="solid")
entry1.grid(row=0, column=1, padx=10)

label2 = tk.Label(frame,
                  text="Up to",
                  font=("Arial", 15, "bold"),
                  bg="#E0E0E0",
                  fg="#2c3f53")
label2.grid(row=0, column=2, padx=10)

entry2 = tk.Entry(frame,
                  width=6,
                  font=("Arial", 20, "bold"),
                  bg="#ffffff",
                  fg="black",
                  bd=1,
                  relief="solid")
entry2.grid(row=0, column=3, padx=10)

button = tk.Button(frame,
                   text="Generate Table",
                   font=("Arial", 15, "bold"),
                   bg="#1877F2",
                   fg="white",
                   width=14,
                   height=1,
                   relief="flat",
                   activebackground="#1877F2",
                   activeforeground="white",
                   command=generate_table)
button.grid(row=0, column=4, padx=10)

frame2 = tk.Frame(root, bg="#F0F0F0", padx=20, pady=15)
frame2.pack(pady=(40, 0))

root.mainloop()