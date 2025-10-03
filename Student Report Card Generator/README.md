# 🎓 Student Report Card Generator (Tkinter)

A Python GUI application built with **Tkinter** that allows you to easily generate, display, and save **student report cards**.  
The app calculates the **total marks, percentage, and grade** based on entered scores for each subject and automatically saves the report to your **Downloads** folder.

---

## ✨ Features
- 📝 Enter **student’s name** and marks for all subjects
- ✅ Validates marks input (only allows `0–100`)
- 📊 Automatically calculates:
  - Total Marks
  - Percentage
  - Grade (A+, A, B, C, D, E, F)
- 📄 Displays the report neatly in a **text box**
- 💾 Saves the report to a `Student_Report.txt` file in the **Downloads** folder
- ⚠️ Shows **error messages** for invalid input
- 🎨 Clean and user-friendly GUI using Tkinter

---

## 🖥️ Preview of the App
- Enter the student’s name and marks for each subject.
- Click **"Generate Report"** to see:
  - The formatted report inside the app.
  - The same report automatically saved to a `.txt` file in your Downloads folder.

---

## 📝 Grade Criteria
| Percentage (%) | Grade |
|----------------|-------|
| 90 and above   | A+    |
| 80 – 89        | A     |
| 70 – 79        | B     |
| 60 – 69        | C     |
| 50 – 59        | D     |
| 33 – 49        | E     |
| Below 33       | F     |

---

## 📦 Requirements
- Python 3.8 or later  
- Built-in modules:
  - `tkinter` (for GUI)
  - `pathlib` (to save file in Downloads)
  - `messagebox` (for pop-up messages)

No external libraries are needed!

---

## ▶️ How to Run
1. **Clone** or **download** this repository.
2. Open the project folder in a terminal or command prompt.
3. Run the Python file:
```bash
   python Main.py
