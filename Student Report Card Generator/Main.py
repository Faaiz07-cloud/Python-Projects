import tkinter as tk
from tkinter import messagebox
from pathlib import Path

# ---------- Functions ----------
def generate_report():
    try:
        # get inputs
        name = entry_student_name.get()
        if not name.strip():
            messagebox.showerror("Error", "Please enter a student name")
            return

        marks = {}
        for subject, mark in entries.items():
            value = mark.get()
            if not value.isdigit() or not (0 <= int(value) <= 100):
                messagebox.showerror("Error", f"Invalid marks for {subject}. Enter 0-100")
                return
            marks[subject] = int(value)

        total = sum(marks.values())
        percentage = total / len(subjects)

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        elif percentage >= 33:
            grade = "E"
        else:
            grade = "F"

        # format report
        report = f"Student Report Card\n"
        report += f"Name: {name}\n\n"
        for s, m in marks.items():
            report += f"{s}: {m}\n"
        report += f"\nTotal: {total}\n"
        report += f"Percentage: {percentage:.2f}%\n"
        report += f"Grade: {grade}\n"

        # show in textbox
        text_box.config(state="normal")
        text_box.delete(1.0, tk.END)
        text_box.insert(tk.END, report)
        text_box.config(state="disabled")

        # save file
        save_path = Path.home() / "Downloads" / "Student_Report.txt"
        with open(save_path, "w") as file:
            file.write(report)
        messagebox.showinfo("Success", f"Report saved to {save_path}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------- UI ----------
root = tk.Tk()
root.geometry("750x750")
root.title("Student Report Card Generator")

# ========== Top Frame ==========
top_frame = tk.Frame(root, pady=15)
top_frame.pack()
tk.Label(top_frame, text="🎓 Welcome to Report Card Generator 🎓",
         font=("Arial", 22, "bold"), fg="blue").pack()

# ========== Name Frame ==========
name_frame = tk.Frame(root, pady=10)
name_frame.pack(fill="x", padx=40)
tk.Label(name_frame, text="Enter Student Name:", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10, sticky="w")
entry_student_name = tk.Entry(name_frame, width=40)
entry_student_name.grid(row=0, column=1, padx=10)

# ========== Subjects Frame ==========
subjects_frame = tk.LabelFrame(root, text="Subjects", font=("Arial", 14, "bold"), padx=20, pady=20, fg="green")
subjects_frame.pack(padx=30, pady=20, fill="x")

subjects = ["English", "Urdu", "Maths", "Physics", "Chemistry"]
entries = {}

# arrange subjects in grid
for i, subject in enumerate(subjects):
    tk.Label(subjects_frame, text=subject, font=("Arial", 13)).grid(row=i, column=0, pady=6, sticky="w")
    subject_entry = tk.Entry(subjects_frame, width=15)
    subject_entry.grid(row=i, column=1, pady=6, padx=10)
    entries[subject] = subject_entry

# ========== Button Frame ==========
button_frame = tk.Frame(root, pady=15)
button_frame.pack()
tk.Button(button_frame, text="Generate Report", font=("Arial", 12, "bold"),
          bg="green", fg="white", width=20, command=generate_report).pack()

# ========== Report Frame ==========
report_frame = tk.LabelFrame(root, text="Generated Report", font=("Arial", 14, "bold"), fg="purple", padx=20, pady=20)
report_frame.pack(padx=30, pady=20, fill="both", expand=True)

text_box = tk.Text(report_frame, width=70, height=15, font=("Consolas", 12))
text_box.pack(fill="both", expand=True)
text_box.config(state="disabled")

root.mainloop()
