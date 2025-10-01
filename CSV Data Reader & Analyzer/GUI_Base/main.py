import csv
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox

class CsvAnalyzer:
     def __init__(self, root):
         self.root = root
         self.root.title("CSV Data Analyzer")
         self.root.resizable(False, False)
         self.root.configure(background="#ffffff")
         self.root.geometry('400x635')
         self.path = None

         self.show_home_page()

     def show_home_page(self):
         self.clean_window()
         self.root.title("CSV Data Analyzer")
         self.root.resizable(False, False)
         self.root.configure(background="#ffffff")
         self.root.geometry('400x635')

         home_img = Image.open("Images/starting_img.png")
         home_img = home_img.resize((255, 185))
         self.home_img = ImageTk.PhotoImage(home_img)

         label_home_screen = tk.Label(self.root, image=self.home_img, bg='#ffffff')
         label_home_screen.place(x=69, y=65)

         label2 = tk.Label(self.root, text="CSV Data Analyzer", bg='#ffffff',fg='#323232',
                           font=('Segoe UI', 22, 'bold'))
         label2.place(x=67, y=255)

         start_img = Image.open("Images/start3.png")
         start_img = start_img.resize((124, 94))
         self.start_img_button = ImageTk.PhotoImage(start_img)

         button_start = tk.Button(self.root, image=self.start_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
         button_start.place(x=138, y=475)


     def dashboard(self):
         self.clean_window()
         self.root.title("Dashboard")
         self.root.resizable(False, False)
         self.root.configure(background="#ffffff")
         self.root.geometry('400x678')

         back_img = Image.open("Images/back2.png")
         back_img = back_img.resize((24, 25))
         self.back_img_button = ImageTk.PhotoImage(back_img)

         button_back = tk.Button(self.root, image=self.back_img_button,
                                 bg='#ffffff', relief='flat', bd=0, command=self.show_home_page)
         button_back.place(x=15, y=12)

         label_file_select = tk.Label(self.root, text="Select File",
                                      bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
         label_file_select.place(x=44, y=2)

         # for dashed rectangle frame
         canvas = tk.Canvas(self.root, width=350, height=160, bg="#ffffff", highlightthickness=0)
         canvas.place(x=26, y=55)

         canvas.create_rectangle(
             10, 10, 340, 150,  # Coords: (10,10) to (w-10,h-10)
             outline="#808080",
             width=2,
             dash=(5, 3))

         browse_img = Image.open("Images/browse2.png")
         browse_img = browse_img.resize((75, 73))
         self.broswe_img = ImageTk.PhotoImage(browse_img)

         button_browse = tk.Button(self.root, image=self.broswe_img,
                                   bg='#ffffff', relief='flat', bd=0, command=self.open_folder)
         button_browse.place(x=162, y=73)

         label_choose_file = tk.Label(self.root, text="Choose File", bg='#ffffff', fg="#323232",
                                      font=('Segoe UI', 11, 'bold'))
         label_choose_file.place(x=157, y=147)

         self.label_show_path = tk.Label(self.root, text="", bg='#ffffff', fg="#323232", font=('Segoe UI', 9, 'bold'))
         self.label_show_path.place(x=92, y=172)

         label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
         entry_style = {
             "font": ("Segoe UI", 12),
             "bg": "#f5f6fa",
             "fg": "#2d3436",
             "relief": "flat",
             "bd": 0,
             "highlightthickness": 1,
             "highlightbackground": "#dcdde1",
             "highlightcolor": "#00cec9"
         }

         column_name_label = tk.Label(self.root, text="Column Name", **label_style)
         column_name_label.pack(fill="x", padx=(141,0), pady=(233, 7))
         self.column_name_entry = tk.Entry(self.root, **entry_style)
         self.column_name_entry.pack(fill="x", padx=(34,31), ipady=8)

         analyze_img = Image.open("Images/start3.png")
         analyze_img = analyze_img.resize((124, 94))
         self.analyze_img = ImageTk.PhotoImage(analyze_img)

         button_analyze = tk.Button(self.root, image=self.analyze_img,
                                     bg='#ffffff', relief='flat', bd=0, command=self.analyze_csv)
         button_analyze.place(x=139, y=317)

         self.output_box = tk.Text(
             self.root,
             height=11, width=37,
             font=("Segoe UI", 11, "bold"),
             bg="#f5f6fa",
             fg="#2d3436",
             relief="flat",
             bd=0,
             highlightthickness=1,
             highlightbackground="#dcdde1",
             highlightcolor="#00cec9"
         )
         self.output_box.place(x=34, y=419)

     def open_folder(self):
         self.path = filedialog.askopenfilename()
         if self.path:
             self.label_show_path.config(text=self.path)

     def analyze_csv(self):
         if not self.path:
             messagebox.showwarning("Warning", "No file selected! Please select a file.")
         else:
              self.start_analyzing()

     def start_analyzing(self):
          values = []
          column_name =  self.column_name_entry.get()

          with open(self.path, 'r', newline='', encoding='utf-8') as file:
              reader = csv.DictReader(file)
              if not column_name in reader.fieldnames:
                  messagebox.showwarning("Warning", f"Column name '{column_name}' does not exist!")

              for row in reader:
                  if row[column_name]:
                      try:
                          values.append(float(row[column_name]))
                      except ValueError:
                          pass

              if not values:
                  messagebox.showwarning("Warning", f"No numerical values found in '{column_name}' !")
                  return

              total = sum(values)
              average = total / len(values)
              maximum = max(values)
              minimum = min(values)

              self.output_box.delete("1.0", tk.END)
              self.output_box.insert(tk.END, f"\n Analysis for column: {column_name}\n\n")
              self.output_box.insert(tk.END, f"    Total: {total}\n\n")
              self.output_box.insert(tk.END, f"    Average: {average}\n\n")
              self.output_box.insert(tk.END, f"    Maximum: {maximum}\n\n")
              self.output_box.insert(tk.END, f"    Minimum: {minimum}\n\n")
              messagebox.showinfo("Success", f"Successfully analysed the data of column: {column_name}!")

     def clean_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
run = CsvAnalyzer(root)
root.mainloop()