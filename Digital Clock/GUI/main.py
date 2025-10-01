import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time
from datetime import datetime
from zoneinfo import ZoneInfo
import requests
import threading
from playsound import playsound


# Class
class DigitalClock:
    def __init__(self, root):
        self.root = root
        self.add_alarm_window = None
        self.alarms = {}
        self.splash_page()
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        # agar add_alarm_window open hai to close karo
        if self.add_alarm_window and tk.Toplevel.winfo_exists(self.add_alarm_window):
            self.add_alarm_window.destroy()
        self.root.destroy()

    def splash_page(self):
        self.clean_window()
        self.root.geometry("330x625+530+50")
        self.root.overrideredirect(True)
        self.root.config(bg="#ffc109")
        self.root.resizable(False, False)

        img_1 = Image.open("DigitalClock Images/splash.png")
        img_1 = img_1.resize((280, 185))
        self.splash_img = ImageTk.PhotoImage(img_1)

        label = tk.Label(self.root, image=self.splash_img, bg="#ffc109")
        label.pack(pady=(210, 0))

        self.root.after(800, self.dashboard)

    def dashboard(self):
        self.clean_window()
        self.root.geometry("330x625+530+50")
        self.root.overrideredirect(False)
        self.root.title("Clock")
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)

        img_2 = Image.open("DigitalClock Images/splash2.png")
        img_2 = img_2.resize((180,180))
        self.splash_img_2 = ImageTk.PhotoImage(img_2)

        label_2 = tk.Label(self.root, image=self.splash_img_2, bg="#ffffff")
        label_2.pack(pady=(8, 0))

        label_name = tk.Label(self.root, text="Clock", font=("Segoe UI", 16, "bold"),
                              bg="#ffffff", fg="#222222")
        label_name.place(x=135, y=173)

        label_name2 = tk.Label(self.root, text="X", font=("Segoe UI", 19, "bold"),
                              bg="#ffffff", fg="#f8c027")
        label_name2.place(x=192, y=170)

        self.label_time = tk.Label(self.root, font=("Segoe UI", 34, "bold"),
                              bg="#ffffff", fg="#111111")
        self.label_time.place(x=95, y=210)

        self.label_am_pm = tk.Label(self.root, font=("Segoe UI", 13, "bold"),
                              bg="#ffffff", fg="#111111")
        self.label_am_pm.place(x=215, y=236)

        self.label_date = tk.Label(self.root, font=("Segoe UI", 12, "bold"),
                                   bg="#ffffff", fg="#666666")
        self.label_date.place(x=90, y=274)

        self.temp = tk.Label(self.root, font=("Segoe UI", 12, "bold"),
                                   bg="#ffffff", fg="#666666")
        self.temp.place(x=219, y=274)

        self.divider = tk.Frame(self.root, bg="#dcdde1", height=1, width=400)
        self.divider.place(x=0, y=315)

        alarms_words = tk.Label(self.root, text="Alarms", font=("Segoe UI", 11, "bold"),
                                   bg="#ffffff", fg="#222222")
        alarms_words.place(x=16, y=324)

        self.alarm_frame = tk.Frame(self.root, bg="#ffffff")
        self.alarm_frame.place(x=20, y=360)

        if not self.alarms:
            self.no_alarm_label = tk.Label(self.root, text="No Alarm set!",
                                           font=("Segoe UI", 13, "bold"),
                                           bg="#ffffff", fg="#666666")
            self.no_alarm_label.place(x=105, y=420)
        else:
            for alarm, lbl in self.alarms.items():
                lbl.pack(anchor="w", pady=(5, 0))

        add_button_img = Image.open("DigitalClock Images/add-button.png")
        add_button_img = add_button_img.resize((60, 60))
        self.add_button_img = ImageTk.PhotoImage(add_button_img)

        add_button = tk.Button(self.root, image=self.add_button_img,
                               bg='#ffffff', relief='flat', bd=0, command=self.add_page,
                               activebackground='#ffffff')
        add_button.place(x=255, y=552)

        self.date_time_show()
        self.weather()

    def date_time_show(self):
        now = datetime.now()
        self.label_time.config(text=now.strftime("%I:%M"))
        self.label_am_pm.config(text=now.strftime("%p"))
        self.label_date.config(text=now.strftime("%a, %b %#d"))
        self.root.after(1000, self.date_time_show)

        current_time = now.strftime("%I:%M %p")

        if current_time in self.alarms:

            lbl =  self.alarms[current_time]
            lbl.destroy()
            del self.alarms[current_time]
            threading.Thread(target=self.play_alarm).start()
            self.root.after(2000, lambda: messagebox.showinfo("Alarm!", f"Alarm {current_time} is on!"))

            if not self.alarms:
                    self.no_alarm_label = tk.Label(self.root, text="No Alarm set!", font=("Segoe UI", 13, "bold"),
                                        bg="#ffffff", fg="#666666")
                    self.no_alarm_label.place(x=105, y=420)

    def play_alarm(self):
            playsound(r"C:\Users\faaiz\PycharmProjects\Digital Clock\GUI\DigitalClock Images\alarm.mp3")

    def weather(self):
        API_KEY = "9b79470a00144c322ffe1422b9e54079"
        URL = f"https://api.openweathermap.org/data/2.5/weather?q=Lahore&appid={API_KEY}&units=metric"
        response = requests.get(URL)
        if response.status_code == 200:
            data = response.json()
            temperature = data["main"]["temp"]
            temperature = int(temperature)
        img_1 = Image.open("DigitalClock Images/sunny.png")
        img_1 = img_1.resize((28, 28))
        self.splash_img = ImageTk.PhotoImage(img_1)

        label = tk.Label(self.root, image=self.splash_img, bg="#ffffff")
        label.place(x=188, y=272,)
        self.temp.config(text=f"{temperature}°C")

    def add_page(self):
        if self.add_alarm_window is None or not tk.Toplevel.winfo_exists(self.add_alarm_window):
            self.add_alarm_window = tk.Toplevel(self.root)
            self.add_alarm_window.overrideredirect(False)
            self.add_alarm_window.title('Alarm')
            self.add_alarm_window.geometry("248x55+530+100")
            self.add_alarm_window.resizable(False, False)
            self.add_alarm_window.config(bg="#ffffff")

            label_style = {"font": ("Calibri", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
            entry_style = {
                "font": ("Calibri", 18),
                "bg": "#f5f6fa",
                "fg": "#2d3436",
                "relief": "flat",
                "bd": 0,
                "width" : 8,
                "highlightthickness": 1,
                "highlightbackground": "#dcdde1",
                "highlightcolor": "#00cec9"
            }

            label_alarm = tk.Label(self.add_alarm_window, text="Set Alarm", **label_style)
            label_alarm.place(x=14, y=10)
            self.alarm_entry = tk.Entry(self.add_alarm_window, **entry_style)
            self.alarm_entry.place(x=90, y=8,)

            add_button_img_2 = Image.open("DigitalClock Images/add-button.png")
            add_button_img_2 = add_button_img_2.resize((42, 42))
            self.add_button_img_2 = ImageTk.PhotoImage(add_button_img_2)

            add_button_2 = tk.Button(self.add_alarm_window, image=self.add_button_img_2,
                                   bg='#ffffff', relief='flat', bd=0, command=self.add,
                                   activebackground='#ffffff')
            add_button_2.place(x=193, y=2)

        else:
            self.add_alarm_window.lift()
            self.add_alarm_window.focus_force()

    def add(self):
        alarm_time = self.alarm_entry.get()
        if not alarm_time:
            messagebox.showwarning("Warning", "Please enter Time.")
            return

        if alarm_time in self.alarms:
            messagebox.showinfo("Info", f"Alarm already set for {alarm_time}")
            return

        if hasattr(self, "no_alarm_label") and self.no_alarm_label.winfo_exists():
            self.no_alarm_label.destroy()

        if alarm_time:
            lbl = tk.Label(self.alarm_frame, text=alarm_time, font=("Calibri", 15, "bold"),
                           bg="#ffffff", fg="#333333",)
            lbl.pack(anchor="w", pady=(5,0))
            self.alarms[alarm_time] = lbl
            messagebox.showinfo("Success", f"Alarm set for {alarm_time}.")
            self.add_alarm_window.destroy()


    def clean_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
run = DigitalClock(root)
root.mainloop()