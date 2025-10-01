# ---------- File Organizer Script UI ----------

# Modules
import os
import shutil
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk


Categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Audio": [".mp3", ".wav", ".m4a", ".flac"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".csv"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".c", ".cs"],
}

class FileOrganizer:
    def __init__(self, root):
        self.root = root
        self.root.title("File Organizer")
        self.root.resizable(False, False)
        self.root.configure(background='#ffffff')
        self.root.geometry('400x635')
        self.folder = None

        self.show_home_screen()

    def show_home_screen(self):
        self.clean_window()
        self.root.title("File Organizer")
        self.root.resizable(False, False)
        self.root.configure(background='#ffffff')
        self.root.geometry('400x610')

        home_img = Image.open("Images/starting img.png")
        home_img = home_img.resize((315,210))
        self.home_img = ImageTk.PhotoImage(home_img)

        label_home_screen = tk.Label(self.root, image=self.home_img, bg='#ffffff')
        label_home_screen.place(x=44, y=50)

        start_img = Image.open("Images/start.png")
        start_img = start_img.resize((115, 50))
        self.start_img_button= ImageTk.PhotoImage(start_img)

        button_start = tk.Button(self.root, image=self.start_img_button,
                                 bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
        button_start.place(x=142, y=345)

        splash_img_1 = Image.open("Images/splash.png")
        splash_img_1 = splash_img_1.resize((400,225))
        self.splash_img_1 = ImageTk.PhotoImage(splash_img_1)

        label_splash_1 = tk.Label(self.root, image=self.splash_img_1, bg='#ffffff', borderwidth=0)
        label_splash_1.place(x=0, y=400)

    def dashboard(self):
        self.clean_window()
        self.root.title("Dashboard")
        self.root.resizable(False, False)
        self.root.configure(background='#ffffff')
        self.root.geometry('400x610')

        back_img = Image.open("Images/back.png")
        back_img = back_img.resize((24, 25))
        self.back_img_button = ImageTk.PhotoImage(back_img)

        button_back = tk.Button(self.root, image=self.back_img_button,
                                 bg='#ffffff', relief='flat', bd=0, command=self.show_home_screen)
        button_back.place(x=15, y=12)

        label_file_select = tk.Label(self.root, text="Select File",
                                     bg='#ffffff',fg='#323232', font=('Segoe UI', 20, 'bold'))
        label_file_select.place(x=44, y=2)

        # for dashed rectangle frame
        canvas = tk.Canvas(self.root, width=350, height=160, bg="#ffffff", highlightthickness=0)
        canvas.place(x=26, y=55)

        canvas.create_rectangle(
            10, 10, 340, 150, # Coords: (10,10) to (w-10,h-10)
            outline="#808080",
            width=2,
            dash=(5, 3))

        browse_img = Image.open("Images/browse.png")
        browse_img = browse_img.resize((75, 73))
        self.broswe_img = ImageTk.PhotoImage(browse_img)

        button_browse = tk.Button(self.root, image= self.broswe_img,
                                bg='#ffffff', relief='flat', bd=0, command=self.open_folder)
        button_browse.place(x=162, y=73)

        label_choose_file = tk.Label(self.root, text="Choose File", bg='#ffffff',fg="#323232", font=('Segoe UI', 11, 'bold'))
        label_choose_file.place(x=157, y=147)

        self.label_show_path = tk.Label(self.root, text="", bg='#ffffff',fg="#323232", font=('Segoe UI', 9, 'bold'))
        self.label_show_path.place(x=92, y=172)

        organize_img = Image.open("Images/start.png")
        organize_img = organize_img.resize((115, 50))
        self.organize_img = ImageTk.PhotoImage(organize_img)

        button_organize = tk.Button(self.root, image=self.organize_img,
                                 bg='#ffffff', relief='flat', bd=0, command=self.start_organize)
        button_organize.place(x=146, y=275)


        splash_img = Image.open("Images/splash.png")
        splash_img = splash_img.resize((400,225))
        self.splash_img = ImageTk.PhotoImage(splash_img)

        label_splash = tk.Label(self.root, image=self.splash_img, bg='#ffffff', borderwidth=0)
        label_splash.place(x=0, y=400)


    def open_folder(self):
        self.folder = filedialog.askdirectory()
        if self.folder:
            self.label_show_path.configure(text=self.folder)

    def start_organize(self):
        folder_path = self.folder
        if folder_path:
            self.organize(folder_path)
        else:
            messagebox.showwarning("Warning", "Please choose a folder to continue.")

    def organize(self, folder_path):
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)

            if os.path.isdir(file_path):
                continue

            ext = os.path.splitext(filename)[1].lower()

            moved = False
            for category, extensions in Categories.items():
                if ext in extensions:
                    category_folder = os.path.join(folder_path, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, filename))
                    moved = True
                    break

            if not moved:
                others_folder = os.path.join(folder_path, "Others")
                os.makedirs(others_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(others_folder, filename))
        messagebox.showinfo("Success", f"File Organizing Complete!\n\nOrganized Folder:\n{folder_path}")

    def clean_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
run = FileOrganizer(root)
root.mainloop()