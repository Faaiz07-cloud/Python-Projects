import os
import json
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import requests

def get_weather(city_name):
    API_KEY = "9b79470a00144c322ffe1422b9e54079"
    URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        return {
        "name": data["name"],
        "desc": data["weather"][0]["description"],
        "temp": data["main"]["temp"],
        "wind": data["wind"]["speed"],
        "humidity": data["main"]["humidity"],
        "clouds": data["clouds"]["all"],
        "lat": data["coord"]["lat"],
        "lon": data["coord"]["lon"]
    }
    else:
         return None

class Weather:
    def __init__(self, root):
        self.root = root
        self.bg_color = "#87CEFA"
        self.weather_data = None
        self.search_window = None
        self.splash_screen()

    def splash_screen(self):
        self.clean_window()
        self.root.geometry("330x630+530+50")
        self.root.overrideredirect(True)
        self.root.config(bg=self.bg_color)
        self.root.resizable(False, False)

        splash_img = Image.open("Weather App Images/splash.png")
        splash_img = splash_img.resize((206, 170))
        self.splash_img = ImageTk.PhotoImage(splash_img)

        label_splash_screen = tk.Label(self.root, image=self.splash_img, bg=self.bg_color)
        label_splash_screen.place(x=55, y=78)

        label_name = tk.Label(self.root, text="ForecastX", bg=self.bg_color, fg="#222222",
                              font=("Segoe UI", 25, 'bold'))
        label_name.place(x=85, y=318)

        label_info_1 = tk.Label(self.root, text="Plan your day smarter", bg=self.bg_color, fg="#222222",
                              font=("Segoe UI", 13,))
        label_info_1.place(x=78, y=390)

        label_info_2 = tk.Label(self.root, text="with instant weather alerts and", bg=self.bg_color, fg="#222222",
                              font=("Segoe UI", 13,))
        label_info_2.place(x=46, y=418)

        label_info_3 = tk.Label(self.root, text="updates", bg=self.bg_color, fg="#222222",
                              font=("Segoe UI", 13,))
        label_info_3.place(x=130, y=446)

        start_img = Image.open("Weather App Images/start.png")
        start_img = start_img.resize((125, 93))
        self.start_img_button = ImageTk.PhotoImage(start_img)

        button_start = tk.Button(self.root, image=self.start_img_button,
                                 bg=self.bg_color, relief='flat', bd=0,
                                 command=self.dashboard, activebackground=self.bg_color)
        button_start.place(x=102, y=505)

    def dashboard(self):
        self.clean_window()
        self.root.geometry("330x620+530+50")

        self.root.title("Dashboard")
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)

        self.detect_label = tk.Label(self.root, text="Detecting Current Location. Please wait",
                                     bg="#ffffff", fg="#555555", font=("Segoe UI", 10))
        self.detect_label.place(x=47, y=300)

        self.root.after(100, self.load_weather)

    def load_weather(self):

            if self.weather_data is None:
                location = requests.get("https://ipinfo.io/json").json()
                current_city = location.get("city")
                self.weather_data = get_weather(current_city)

            self.root.overrideredirect(False)
            self.detect_label.destroy()

            back_img = Image.open("Weather App Images/menu_bar_img.png")
            back_img = back_img.resize((32, 32))
            self.back_img_button = ImageTk.PhotoImage(back_img)

            button_back = tk.Button(self.root, image=self.back_img_button,
                                    bg='#ffffff', relief='flat', bd=0, command=self.splash_screen)
            button_back.place(x=13, y=17)

            label_dashboard = tk.Label(self.root, text="Dashboard",
                                       bg='#ffffff', fg='#222222', font=('Segoe UI', 19, 'bold'))
            label_dashboard.place(x=47, y=12)

            search_img = Image.open("Weather App Images/search.png")
            search_img =search_img.resize((110, 70))
            self.search_img_button = ImageTk.PhotoImage(search_img)

            search_button = tk.Button(self.root, image=self.search_img_button,
                                      bg='#ffffff', relief='flat', bd=0,
                                      activebackground="#ffffff", command=self.search_page)
            search_button.place(x=213, y=3)

            label_about_today = tk.Label(self.root, text="About Today",
                                         bg='#ffffff', fg='#A0A0A0', font=('Segoe UI', 15, 'bold'))
            label_about_today.place(x=23, y=67)

            self.label_name = tk.Label(self.root, text=self.weather_data['name'],
                                       bg='#ffffff', fg='#323232', font=('Segoe UI', 15, 'bold'))
            self.label_name.place(relx=0.5, y=140, anchor="center")

            sunny_img = Image.open("Weather App Images/sunny.png")
            sunny_img = sunny_img.resize((135, 125))
            self.sunny_img = ImageTk.PhotoImage(sunny_img)

            raining_img = Image.open("Weather App Images/raining.png")
            raining_img = raining_img.resize((135, 125))
            self.raining_img = ImageTk.PhotoImage(raining_img)

            clouds_img = Image.open("Weather App Images/clouds.png")
            clouds_img = clouds_img.resize((135, 125))
            self.clouds_img = ImageTk.PhotoImage(clouds_img)

            other_img = Image.open("Weather App Images/other weather.png")
            other_img = other_img.resize((135, 125))
            self.other_img = ImageTk.PhotoImage(other_img)

            desc = self.weather_data["desc"]

            if desc == "clear sky":
                weather_pic = self.sunny_img
            elif desc in ["few clouds", "scattered clouds", "broken clouds", "overcast clouds"]:
                weather_pic = self.clouds_img
            elif desc in ["light rain", "moderate rain", "heavy intensity rain"]:
                weather_pic = self.raining_img
            else:
                weather_pic = self.other_img

            self.label_img = tk.Label(self.root, image=weather_pic, bg="#ffffff")
            self.label_img.place(x=95, y=170)

            description = self.weather_data["desc"]
            description = description.title()
            self.label_desc = tk.Label(self.root, text=description,
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 14, 'bold'))
            self.label_desc.place(relx=0.5, y=320, anchor="center")

            self.label_temp = tk.Label(self.root, text=f"{self.weather_data["temp"]}°C",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 22, 'bold'))
            self.label_temp.place(relx=0.5, y=370, anchor="center")

            rain_img = Image.open("Weather App Images/rain.png")
            rain_img = rain_img.resize((93, 140))
            self.rain_img = ImageTk.PhotoImage(rain_img)

            self.label_rain = tk.Label(self.root, image=self.rain_img, bg="#ffffff")
            self.label_rain.place(x=15, y=435)

            self.label_rain_word = tk.Label(self.root, text="Rain", bg='#f5f5f5', fg='#323232', font=('Segoe UI', 13,))
            self.label_rain_word.place(x=45, y=540)

            self.label_rain_count = tk.Label(self.root, text=f"{self.weather_data['clouds']}%", bg='#f5f5f5', fg='#323232', font=('Calibiri', 16, "bold"))
            self.label_rain_count.place(x=46, y=508)


            wind_img = Image.open("Weather App Images/wind.png")
            wind_img = wind_img.resize((93, 140))
            self.wind_img = ImageTk.PhotoImage(wind_img)

            self.wind_rain = tk.Label(self.root, image=self.wind_img, bg="#ffffff")
            self.wind_rain.place(x=117, y=435)

            self.label_wind_word = tk.Label(self.root, text="Wind", bg='#f5f5f5', fg='#323232', font=('Segoe UI', 13,))
            self.label_wind_word.place(x=142, y=540)

            self.label_wind_count = tk.Label(self.root, text=f"{self.weather_data['wind']}K", bg='#f5f5f5', fg='#323232', font=('Calibiri', 16, "bold"))
            self.label_wind_count.place(x=134, y=508)



            humidity_img = Image.open("Weather App Images/humidity.png")
            humidity_img = humidity_img.resize((93, 140))
            self.humidity_img = ImageTk.PhotoImage(humidity_img)

            self.humidity_rain = tk.Label(self.root, image=self.humidity_img, bg="#ffffff")
            self.humidity_rain.place(x=219, y=435)

            self.label_humidity_word = tk.Label(self.root, text="Humidity", bg='#f5f5f5', fg='#323232', font=('Segoe UI', 13,))
            self.label_humidity_word.place(x=231, y=540)

            self.label_humidity_count = tk.Label(self.root, text=f"{self.weather_data['humidity']}%", bg='#f5f5f5', fg='#323232', font=('Calibiri', 16, "bold"))
            self.label_humidity_count.place(x=244, y=508)


    def search_page(self):
        if self.search_window is None or not tk.Toplevel.winfo_exists(self.search_window):
            self.search_window = tk.Toplevel(self.root)
            self.search_window.title("Change Location")
            self.search_window.geometry("375x256")
            self.search_window.configure(bg="#ffffff")
            self.search_window.resizable(False, False)

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

            label_main = tk.Label(self.search_window, text="Change Location",
                                    bg='#ffffff', fg='#323232', font=('Segoe UI', 18, 'bold'))
            label_main.place(x=95, y=16)

            label = tk.Label(self.search_window, text="Enter City Name:", **label_style)
            label.pack(fill="x", padx=(29, 0), pady=(80, 7))
            self.entry = tk.Entry(self.search_window, **entry_style)
            self.entry.pack(fill="x", padx=(30, 30), ipady=8)

            change = Image.open("Weather App Images/change.png")
            change = change.resize((111, 99))
            self.change = ImageTk.PhotoImage(change)

            change_button = tk.Button(self.search_window, image=self.change,
                                       bg='#ffffff', relief='flat', bd=0, command=self.do_change,
                                       activebackground='#ffffff')
            change_button.place(x=132, y=158)
        else:
            self.search_window.lift()
            self.search_window.focus_force()

    def do_change(self):
        city_name = self.entry.get().lower()
        if not city_name:
            messagebox.showerror("Error", "Enter City Name!")
            return

        self.weather_data = get_weather(city_name)

        name = self.weather_data["name"]
        self.label_name.configure(text=name)

        desc = self.weather_data["desc"]
        if desc == "clear sky":
            weather_pic = self.sunny_img
        elif desc in ["few clouds", "scattered clouds", "broken clouds", "overcast clouds"]:
            weather_pic = self.clouds_img
        elif desc in ["light rain", "moderate rain", "heavy intensity rain"]:
            weather_pic = self.raining_img
        else:
            weather_pic = self.other_img

        self.label_img.configure(image=weather_pic)


        description = self.weather_data["desc"]
        description = description.title()
        self.label_desc.configure(text=description)

        temp = self.weather_data["temp"]
        self.label_temp.configure(text=f"{temp}°C")

        clouds = self.weather_data["clouds"]
        self.label_rain_count.configure(text=f"{clouds}%")

        wind = self.weather_data["wind"]
        self.label_wind_count.configure(text=f"{wind}k")

        humidity = self.weather_data["humidity"]
        self.label_humidity_count.configure(text=f"{humidity}%")

        self.search_window.destroy()
        self.dashboard()

    def clean_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
run = Weather(root)
root.mainloop()