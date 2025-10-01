import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox

from virtualenv.config.convert import convert


class UnitConverter:
      def __init__(self, root):
          self.root = root
          self.root.title("Unit Converter")
          self.root.resizable(False, False)
          self.root.geometry("375x630")
          self.root.configure(background="#ffffff")

          self.show_home_screen()

      def show_home_screen(self):
          self.clean_window()
          self.root.title("Unit Converter")
          self.root.resizable(False, False)
          self.root.geometry("375x630")
          self.root.configure(background="#ffffff")

          home_img = Image.open("Unit Converter Images/starting_img.png")
          home_img = home_img.resize((265, 190))
          self.home_img = ImageTk.PhotoImage(home_img)

          label_home_screen = tk.Label(self.root, image=self.home_img, bg='#ffffff')
          label_home_screen.place(x=56, y=60)

          label2 = tk.Label(self.root, text="Convert", bg='#ffffff', fg='#323232',
                            font=('Segoe UI', 23, 'bold'))
          label2.place(x=90, y=256)

          label3 = tk.Label(self.root, text="Lab", bg='#ffffff', fg='#7698B5',
                            font=('Segoe UI', 31, 'bold'))
          label3.place(x=208, y=249)

          start_img = Image.open("Unit Converter Images/start.png")
          start_img = start_img.resize((124, 94))
          self.start_img_button = ImageTk.PhotoImage(start_img)

          button_start = tk.Button(self.root, image=self.start_img_button,
                                   bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
          button_start.place(x=124, y=475)

      def dashboard(self):
          self.clean_window()
          self.root.title("Dashboard")
          self.root.resizable(False, False)
          self.root.geometry("375x662")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.show_home_screen)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Dashboard",
                                       bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          frame = Image.open("Unit Converter Images/rounded-rectangle.png")
          frame = frame.resize((335, 185))
          self.frame = ImageTk.PhotoImage(frame)

          label = tk.Label(self.root, image=self.frame, bg="#ffffff")
          label.place(x=14, y=50)

          conversion_img = Image.open("Unit Converter Images/transfer.png")
          conversion_img = conversion_img.resize((90, 90))
          self.conversion_img = ImageTk.PhotoImage(conversion_img)

          label_conversion_img = tk.Label(self.root, image=self.conversion_img, bg="#323232")
          label_conversion_img.place(x=45, y=93)

          label_app_name = tk.Label(self.root, text="Convert Lab", font=('Segoe UI', 23, 'bold')
                                    ,bg='#323232', fg='#ffffff')
          label_app_name.place(x=131, y=113)

          label7 = tk.Label(self.root, text="Select", bg="#ffffff", fg="#6f6f6f",
                            font=("Calibri", 14, "bold"))
          label7.place(x=24, y=245)

          button = tk.Button(self.root, text="More", bg="#ffffff", fg="#6f6f6f", font=("Calibri", 14, "bold"),
                             relief="flat", bd=0, command=self.more)
          button.place(x=293, y=243)

          length_img = Image.open("Unit Converter Images/length.png")
          length_img = length_img.resize((355, 130))
          self.length_img = ImageTk.PhotoImage(length_img)

          length_button = tk.Button(self.root, image=self.length_img, bg="#ffffff",
                                    relief='flat', bd=0, highlightcolor="#ffffff", highlightthickness=0, activebackground="#ffffff", activeforeground="#ffffff", command=self.length_menu)
          length_button.place(x=10, y=280)

          weight_img = Image.open("Unit Converter Images/Weight.png")
          weight_img = weight_img.resize((355, 130))
          self.weight_img = ImageTk.PhotoImage(weight_img)

          weight_button = tk.Button(self.root, image=self.weight_img, bg="#ffffff",
                                    relief='flat', bd=0, highlightcolor="#ffffff", highlightthickness=0, activebackground="#ffffff", activeforeground="#ffffff", command=self.weight_menu)
          weight_button.place(x=10, y=399)

          temp_img = Image.open("Unit Converter Images/Temperature.png")
          temp_img = temp_img.resize((355, 130))
          self.temp_img = ImageTk.PhotoImage(temp_img)

          temp_button = tk.Button(self.root, image=self.temp_img, bg="#ffffff",
                                    relief='flat', bd=0, highlightcolor="#ffffff", highlightthickness=0, activebackground="#ffffff", activeforeground="#ffffff", command=self.temp_menu)
          temp_button.place(x=10, y=518)

      def more(self):
          self.clean_window()
          self.root.title("More")
          self.root.resizable(False, False)
          self.root.geometry("375x662")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="More",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          time_img = Image.open("Unit Converter Images/Time.png")
          time_img = time_img.resize((355, 130))
          self.time_img = ImageTk.PhotoImage(time_img)

          time_button = tk.Button(self.root, image=self.time_img, bg="#ffffff",
                                    relief='flat', bd=0, highlightcolor="#ffffff", highlightthickness=0,
                                    activebackground="#ffffff", activeforeground="#ffffff", command=self.time_menu)
          time_button.place(x=10, y=47)

          area_img = Image.open("Unit Converter Images/Area.png")
          area_img = area_img.resize((355, 130))
          self.area_img = ImageTk.PhotoImage(area_img)

          area_button = tk.Button(self.root, image=self.area_img, bg="#ffffff",
                                  relief='flat', bd=0, highlightcolor="#ffffff", highlightthickness=0,
                                  activebackground="#ffffff", activeforeground="#ffffff", command=self.area_menu)
          area_button.place(x=10, y=166)

          volume_img = Image.open("Unit Converter Images/Volume.png")
          volume_img = volume_img.resize((355, 130))
          self.volume_img = ImageTk.PhotoImage(volume_img)

          volume_button = tk.Button(self.root, image=self.volume_img, bg="#ffffff",
                                  relief='flat', bd=0, highlightcolor="#ffffff", highlightthickness=0,
                                  activebackground="#ffffff", activeforeground="#ffffff", command=self.volume_menu)
          volume_button.place(x=10, y=285)

          speed_img = Image.open("Unit Converter Images/Speed.png")
          speed_img = speed_img.resize((355, 130))
          self.speed_img = ImageTk.PhotoImage(speed_img)

          speed_button = tk.Button(self.root, image=self.speed_img, bg="#ffffff",
                                    relief='flat', bd=0, highlightcolor="#ffffff", highlightthickness=0,
                                    activebackground="#ffffff", activeforeground="#ffffff", command=self.speed_menu)
          speed_button.place(x=10, y=404)

          energy_img = Image.open("Unit Converter Images/Energy.png")
          energy_img = energy_img.resize((355, 130))
          self.energy_img = ImageTk.PhotoImage(energy_img)

          energy_button = tk.Button(self.root, image=self.energy_img, bg="#ffffff",
                                   relief='flat', bd=0, highlightcolor="#ffffff", highlightthickness=0,
                                   activebackground="#ffffff", activeforeground="#ffffff", command=self.energy_menu)
          energy_button.place(x=10, y=523)

      def length_menu(self):
          self.clean_window()
          self.root.title("Length Converter")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Length",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          img1 = Image.open("Unit Converter Images/Length Menu/1.png")
          img1 = img1.resize((320, 85))
          self.img1 = ImageTk.PhotoImage(img1)

          button1 = tk.Button(self.root, image=self.img1, bg="#ffffff", relief='flat', bd=0, activebackground="#ffffff", command=self.ft__m)
          button1.place(x=26, y=58)

          img2 = Image.open("Unit Converter Images/Length Menu/2.png")
          img2 = img2.resize((320, 85))
          self.img2 = ImageTk.PhotoImage(img2)

          button2 = tk.Button(self.root, image=self.img2, bg="#ffffff", relief='flat', bd=0, activebackground="#ffffff", command=self.in__m)
          button2.place(x=26, y=150)

          img3 = Image.open("Unit Converter Images/Length Menu/3.png")
          img3 = img3.resize((320, 85))
          self.img3 = ImageTk.PhotoImage(img3)

          button3 = tk.Button(self.root, image=self.img3, bg="#ffffff", relief='flat', bd=0, activebackground="#ffffff", command=self.km__m)
          button3.place(x=26, y=242)

          img4 = Image.open("Unit Converter Images/Length Menu/4.png")
          img4 = img4.resize((320, 85))
          self.img4 = ImageTk.PhotoImage(img4)

          button4 = tk.Button(self.root, image=self.img4, bg="#ffffff", relief='flat', bd=0, activebackground="#ffffff", command=self.cm__in)
          button4.place(x=26, y=334)

          img5 = Image.open("Unit Converter Images/Length Menu/5.png")
          img5 = img5.resize((320, 85))
          self.img5 = ImageTk.PhotoImage(img5)

          button5 = tk.Button(self.root, image=self.img5, bg="#ffffff", relief='flat', bd=0, activebackground="#ffffff", command=self.mi__km)
          button5.place(x=26, y=426)

          img6 = Image.open("Unit Converter Images/Length Menu/6.png")
          img6 = img6.resize((320, 85))
          self.img6 = ImageTk.PhotoImage(img6)

          button6 = tk.Button(self.root, image=self.img6, bg="#ffffff", relief='flat', bd=0, activebackground="#ffffff", command=self.m__yd)
          button6.place(x=26, y=518)

      def weight_menu(self):
          self.clean_window()
          self.root.title("Weight Converter")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Weight",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          img1 = Image.open("Unit Converter Images/Weight Menu/1.png")
          img1 = img1.resize((320, 85))
          self.img1 = ImageTk.PhotoImage(img1)

          button1 = tk.Button(self.root, image=self.img1, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command= self.kg__lb)
          button1.place(x=26, y=58)

          img2 = Image.open("Unit Converter Images/Weight Menu/2.png")
          img2 = img2.resize((320, 85))
          self.img2 = ImageTk.PhotoImage(img2)

          button2 = tk.Button(self.root, image=self.img2, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.g__kg)
          button2.place(x=26, y=150)

          img3 = Image.open("Unit Converter Images/Weight Menu/3.png")
          img3 = img3.resize((320, 85))
          self.img3 = ImageTk.PhotoImage(img3)

          button3 = tk.Button(self.root, image=self.img3, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.kg__mg)
          button3.place(x=26, y=242)

          img4 = Image.open("Unit Converter Images/Weight Menu/4.png")
          img4 = img4.resize((320, 85))
          self.img4 = ImageTk.PhotoImage(img4)

          button4 = tk.Button(self.root, image=self.img4, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.oz__g)
          button4.place(x=26, y=334)

          img5 = Image.open("Unit Converter Images/Weight Menu/5.png")
          img5 = img5.resize((320, 85))
          self.img5 = ImageTk.PhotoImage(img5)

          button5 = tk.Button(self.root, image=self.img5, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.ton__kg)
          button5.place(x=26, y=426)

          img6 = Image.open("Unit Converter Images/Weight Menu/6.png")
          img6 = img6.resize((320, 85))
          self.img6 = ImageTk.PhotoImage(img6)

          button6 = tk.Button(self.root, image=self.img6, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.lb__oz)
          button6.place(x=26, y=518)

      def temp_menu(self):
          self.clean_window()
          self.root.title("Temperature Converter")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.dashboard)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Temperature",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          img1 = Image.open("Unit Converter Images/Temp Menu/1.png")
          img1 = img1.resize((320, 85))
          self.img1 = ImageTk.PhotoImage(img1)

          button1 = tk.Button(self.root, image=self.img1, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.c__f)
          button1.place(x=26, y=58)

          img2 = Image.open("Unit Converter Images/Temp Menu/2.png")
          img2 = img2.resize((320, 85))
          self.img2 = ImageTk.PhotoImage(img2)

          button2 = tk.Button(self.root, image=self.img2, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.c__k)
          button2.place(x=26, y=150)

          img3 = Image.open("Unit Converter Images/Temp Menu/3.png")
          img3 = img3.resize((320, 85))
          self.img3 = ImageTk.PhotoImage(img3)

          button3 = tk.Button(self.root, image=self.img3, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.f__k)
          button3.place(x=26, y=242)

          img4 = Image.open("Unit Converter Images/Temp Menu/4.png")
          img4 = img4.resize((320, 85))
          self.img4 = ImageTk.PhotoImage(img4)

          button4 = tk.Button(self.root, image=self.img4, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.c__r)
          button4.place(x=26, y=334)

          img5 = Image.open("Unit Converter Images/Temp Menu/5.png")
          img5 = img5.resize((320, 85))
          self.img5 = ImageTk.PhotoImage(img5)

          button5 = tk.Button(self.root, image=self.img5, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.f__r)
          button5.place(x=26, y=426)

          img6 = Image.open("Unit Converter Images/Temp Menu/6.png")
          img6 = img6.resize((320, 85))
          self.img6 = ImageTk.PhotoImage(img6)

          button6 = tk.Button(self.root, image=self.img6, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.k__r)
          button6.place(x=26, y=518)

      def time_menu(self):
          self.clean_window()
          self.root.title("Time Converter")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.more)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Time",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)


          img1 = Image.open("Unit Converter Images/Time Menu/1.png")
          img1 = img1.resize((320, 85))
          self.img1 = ImageTk.PhotoImage(img1)

          button1 = tk.Button(self.root, image=self.img1, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.hr__min)
          button1.place(x=26, y=58)

          img2 = Image.open("Unit Converter Images/Time Menu/2.png")
          img2 = img2.resize((320, 85))
          self.img2 = ImageTk.PhotoImage(img2)

          button2 = tk.Button(self.root, image=self.img2, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.hr__sec)
          button2.place(x=26, y=150)

          img3 = Image.open("Unit Converter Images/Time Menu/3.png")
          img3 = img3.resize((320, 85))
          self.img3 = ImageTk.PhotoImage(img3)

          button3 = tk.Button(self.root, image=self.img3, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.sec__min)
          button3.place(x=26, y=242)

          img4 = Image.open("Unit Converter Images/Time Menu/4.png")
          img4 = img4.resize((320, 85))
          self.img4 = ImageTk.PhotoImage(img4)

          button4 = tk.Button(self.root, image=self.img4, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.day__hr)
          button4.place(x=26, y=334)

          img5 = Image.open("Unit Converter Images/Time Menu/5.png")
          img5 = img5.resize((320, 85))
          self.img5 = ImageTk.PhotoImage(img5)

          button5 = tk.Button(self.root, image=self.img5, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.wk__day)
          button5.place(x=26, y=426)

          img6 = Image.open("Unit Converter Images/Time Menu/6.png")
          img6 = img6.resize((320, 85))
          self.img6 = ImageTk.PhotoImage(img6)

          button6 = tk.Button(self.root, image=self.img6, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.mon__day)
          button6.place(x=26, y=518)

      def area_menu(self):
          self.clean_window()
          self.root.title("Area Converter")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.more)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Area",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          img1 = Image.open("Unit Converter Images/Area Menu/1.png")
          img1 = img1.resize((320, 85))
          self.img1 = ImageTk.PhotoImage(img1)

          button1 = tk.Button(self.root, image=self.img1, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.m2__ft2)
          button1.place(x=26, y=58)

          img2 = Image.open("Unit Converter Images/Area Menu/2.png")
          img2 = img2.resize((320, 85))
          self.img2 = ImageTk.PhotoImage(img2)

          button2 = tk.Button(self.root, image=self.img2, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.km2__ha)
          button2.place(x=26, y=150)

          img3 = Image.open("Unit Converter Images/Area Menu/3.png")
          img3 = img3.resize((320, 85))
          self.img3 = ImageTk.PhotoImage(img3)

          button3 = tk.Button(self.root, image=self.img3, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.ac__m2)
          button3.place(x=26, y=242)

          img4 = Image.open("Unit Converter Images/Area Menu/4.png")
          img4 = img4.resize((320, 85))
          self.img4 = ImageTk.PhotoImage(img4)

          button4 = tk.Button(self.root, image=self.img4, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.yd2__ft2)
          button4.place(x=26, y=334)

          img5 = Image.open("Unit Converter Images/Area Menu/5.png")
          img5 = img5.resize((320, 85))
          self.img5 = ImageTk.PhotoImage(img5)

          button5 = tk.Button(self.root, image=self.img5, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.in2__cm2)
          button5.place(x=26, y=426)

          img6 = Image.open("Unit Converter Images/Area Menu/6.png")
          img6 = img6.resize((320, 85))
          self.img6 = ImageTk.PhotoImage(img6)

          button6 = tk.Button(self.root, image=self.img6, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.mi2__ac)
          button6.place(x=26, y=518)

      def volume_menu(self):
          self.clean_window()
          self.root.title("Volume Converter")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.more)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Volume",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          img1 = Image.open("Unit Converter Images/Volume Menu/1.png")
          img1 = img1.resize((320, 85))
          self.img1 = ImageTk.PhotoImage(img1)

          button1 = tk.Button(self.root, image=self.img1, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.l__ml)
          button1.place(x=26, y=58)

          img2 = Image.open("Unit Converter Images/Volume Menu/2.png")
          img2 = img2.resize((320, 85))
          self.img2 = ImageTk.PhotoImage(img2)

          button2 = tk.Button(self.root, image=self.img2, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.l__gal)
          button2.place(x=26, y=150)

          img3 = Image.open("Unit Converter Images/Volume Menu/3.png")
          img3 = img3.resize((320, 85))
          self.img3 = ImageTk.PhotoImage(img3)

          button3 = tk.Button(self.root, image=self.img3, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.m3__l)
          button3.place(x=26, y=242)

          img4 = Image.open("Unit Converter Images/Volume Menu/4.png")
          img4 = img4.resize((320, 85))
          self.img4 = ImageTk.PhotoImage(img4)

          button4 = tk.Button(self.root, image=self.img4, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.cm3__ml)
          button4.place(x=26, y=334)

          img5 = Image.open("Unit Converter Images/Volume Menu/5.png")
          img5 = img5.resize((320, 85))
          self.img5 = ImageTk.PhotoImage(img5)

          button5 = tk.Button(self.root, image=self.img5, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.in3__cm3)
          button5.place(x=26, y=426)

          img6 = Image.open("Unit Converter Images/Volume Menu/6.png")
          img6 = img6.resize((320, 85))
          self.img6 = ImageTk.PhotoImage(img6)

          button6 = tk.Button(self.root, image=self.img6, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.ft3__gal)
          button6.place(x=26, y=518)


      def speed_menu(self):
          self.clean_window()
          self.root.title("Speed Converter")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.more)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Speed",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          img1 = Image.open("Unit Converter Images/Speed Menu/1.png")
          img1 = img1.resize((320, 85))
          self.img1 = ImageTk.PhotoImage(img1)

          button1 = tk.Button(self.root, image=self.img1, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.kmh__mph)
          button1.place(x=26, y=58)

          img2 = Image.open("Unit Converter Images/Speed Menu/2.png")
          img2 = img2.resize((320, 85))
          self.img2 = ImageTk.PhotoImage(img2)

          button2 = tk.Button(self.root, image=self.img2, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.ms__kmh)
          button2.place(x=26, y=150)

          img3 = Image.open("Unit Converter Images/Speed Menu/3.png")
          img3 = img3.resize((320, 85))
          self.img3 = ImageTk.PhotoImage(img3)

          button3 = tk.Button(self.root, image=self.img3, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.ms__mph)
          button3.place(x=26, y=242)

          img4 = Image.open("Unit Converter Images/Speed Menu/4.png")
          img4 = img4.resize((320, 85))
          self.img4 = ImageTk.PhotoImage(img4)

          button4 = tk.Button(self.root, image=self.img4, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.kn__kmh)
          button4.place(x=26, y=334)

          img5 = Image.open("Unit Converter Images/Speed Menu/5.png")
          img5 = img5.resize((320, 85))
          self.img5 = ImageTk.PhotoImage(img5)

          button5 = tk.Button(self.root, image=self.img5, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.fts__ms)
          button5.place(x=26, y=426)

          img6 = Image.open("Unit Converter Images/Speed Menu/6.png")
          img6 = img6.resize((320, 85))
          self.img6 = ImageTk.PhotoImage(img6)

          button6 = tk.Button(self.root, image=self.img6, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.mach__kmh)
          button6.place(x=26, y=518)

      def energy_menu(self):
          self.clean_window()
          self.root.title("Energy Converter")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.more)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Energy",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          img1 = Image.open("Unit Converter Images/Energy Menu/1.png")
          img1 = img1.resize((320, 85))
          self.img1 = ImageTk.PhotoImage(img1)

          button1 = tk.Button(self.root, image=self.img1, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.j__ev)
          button1.place(x=26, y=58)

          img2 = Image.open("Unit Converter Images/Energy Menu/2.png")
          img2 = img2.resize((320, 85))
          self.img2 = ImageTk.PhotoImage(img2)

          button2 = tk.Button(self.root, image=self.img2, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.j__cal)
          button2.place(x=26, y=150)

          img3 = Image.open("Unit Converter Images/Energy Menu/3.png")
          img3 = img3.resize((320, 85))
          self.img3 = ImageTk.PhotoImage(img3)

          button3 = tk.Button(self.root, image=self.img3, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.j__kwh)
          button3.place(x=26, y=242)

          img4 = Image.open("Unit Converter Images/Energy Menu/4.png")
          img4 = img4.resize((320, 85))
          self.img4 = ImageTk.PhotoImage(img4)

          button4 = tk.Button(self.root, image=self.img4, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.kwh__cal)
          button4.place(x=26, y=334)

          img5 = Image.open("Unit Converter Images/Energy Menu/5.png")
          img5 = img5.resize((320, 85))
          self.img5 = ImageTk.PhotoImage(img5)

          button5 = tk.Button(self.root, image=self.img5, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.j__wh)
          button5.place(x=26, y=426)

          img6 = Image.open("Unit Converter Images/Energy Menu/6.png")
          img6 = img6.resize((320, 85))
          self.img6 = ImageTk.PhotoImage(img6)

          button6 = tk.Button(self.root, image=self.img6, bg="#ffffff", relief='flat', bd=0,
                              activebackground="#ffffff", command=self.btu__j)
          button6.place(x=26, y=518)

      # Length conversions
      def ft__m(self):
          self.clean_window()
          self.root.title("Length Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.length_menu)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Length Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

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

          result_style = {
              "font": ("Segoe UI", 13, "bold"),
              "bg": "#f5f6fa",
              "fg": "#27ae60",
              "relief": "flat",
              "anchor": "center",
              "bd": 1
          }

          def f_to_m():
               feet = entry.get()
               if not feet:
                   messagebox.showwarning("Warning", "Please enter a Value.")
                   return
               if not feet.isdigit():
                   messagebox.showwarning("Warning", "Please enter a Number.")
                   return
               feet = float(feet)
               meters = feet / 3.28084

               result_label.configure(text=f"{feet:.2f} feet = {meters:.2f} meters")
               result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def m_to_f():
              meters = entry2.get()
              if not meters:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not meters.isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              meters = float(meters)
              feet = meters * 3.28084

              result_label.configure(text=f"{meters:.2f} meters = {feet:.2f} feet")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          label = tk.Label(self.root, text="Feet to Meters", **label_style)
          label.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry = tk.Entry(self.root, **entry_style)
          entry.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img = Image.open("Unit Converter Images/convert.png")
          convert_img = convert_img.resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)

          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                   bg='#ffffff', relief='flat', bd=0, command=f_to_m)
          convert_button.place(x=245, y=158)


          label2 = tk.Label(self.root, text="Meters to Feet", **label_style)
          label2.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry2 = tk.Entry(self.root, **entry_style)
          entry2.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img2 = Image.open("Unit Converter Images/convert.png")
          convert_img2 = convert_img2.resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)

          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                   bg='#ffffff', relief='flat', bd=0, command=m_to_f)
          convert_button2.place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)
      # --------------------------------------------------------------------------------------------

      def in__m(self):
          self.clean_window()
          self.root.title("Length Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.length_menu)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Length Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

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

          result_style = {
              "font": ("Segoe UI", 13, "bold"),
              "bg": "#f5f6fa",
              "fg": "#27ae60",
              "relief": "flat",
              "anchor": "center",
              "bd": 1
          }

          # ---------------- Conversion Functions ----------------
          def in_to_m():
              inches = entry.get()
              if not inches:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not inches.isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              inches = float(inches)
              meters = inches * 0.0254  # ✅ 1 inch = 0.0254 meters

              result_label.configure(text=f"{inches:.2f} inches = {meters:.4f} meters")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def m_to_in():
              meters = entry2.get()
              if not meters:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not meters.isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              meters = float(meters)
              inches = meters / 0.0254  # ✅ 1 meter = 39.3701 inches

              result_label.configure(text=f"{meters:.2f} meters = {inches:.2f} inches")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # ---------------- Widgets ----------------
          label = tk.Label(self.root, text="Inches to Meters", **label_style)
          label.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry = tk.Entry(self.root, **entry_style)
          entry.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img = Image.open("Unit Converter Images/convert.png")
          convert_img = convert_img.resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)

          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=in_to_m)
          convert_button.place(x=245, y=158)

          label2 = tk.Label(self.root, text="Meters to Inches", **label_style)
          label2.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry2 = tk.Entry(self.root, **entry_style)
          entry2.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img2 = Image.open("Unit Converter Images/convert.png")
          convert_img2 = convert_img2.resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)

          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=m_to_in)
          convert_button2.place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)
      # --------------------------------------------------------------------------------------------

      def km__m(self):
          self.clean_window()
          self.root.title("Length Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.length_menu)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Length Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

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

          result_style = {
              "font": ("Segoe UI", 13, "bold"),
              "bg": "#f5f6fa",
              "fg": "#27ae60",
              "relief": "flat",
              "anchor": "center",
              "bd": 1
          }

          def km_to_m():
              km = entry.get()
              if not km:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not km.isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              km = float(km)
              meters = km * 1000
              result_label.configure(text=f"{km:.2f} kilometers = {meters:.2f} meters")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def m_to_km():
              meters = entry2.get()
              if not meters:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not meters.isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              meters = float(meters)
              km = meters / 1000
              result_label.configure(text=f"{meters:.2f} meters = {km:.2f} kilometers")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          label = tk.Label(self.root, text="Kilometers to Meters", **label_style)
          label.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry = tk.Entry(self.root, **entry_style)
          entry.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img = Image.open("Unit Converter Images/convert.png")
          convert_img = convert_img.resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)

          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=km_to_m)
          convert_button.place(x=245, y=158)

          label2 = tk.Label(self.root, text="Meters to Kilometers", **label_style)
          label2.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry2 = tk.Entry(self.root, **entry_style)
          entry2.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img2 = Image.open("Unit Converter Images/convert.png")
          convert_img2 = convert_img2.resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)

          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=m_to_km)
          convert_button2.place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ------------------------------------------------------------------------------------------------

      def cm__in(self):
          self.clean_window()
          self.root.title("Length Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.length_menu)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Length Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

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

          result_style = {
              "font": ("Segoe UI", 13, "bold"),
              "bg": "#f5f6fa",
              "fg": "#27ae60",
              "relief": "flat",
              "anchor": "center",
              "bd": 1
          }

          def cm_to_in():
              cm = entry.get()
              if not cm:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not cm.isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              cm = float(cm)
              inches = cm / 2.54
              result_label.configure(text=f"{cm:.2f} centimeters = {inches:.2f} inches")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def in_to_cm():
              inches = entry2.get()
              if not inches:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not inches.isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              inches = float(inches)
              cm = inches * 2.54
              result_label.configure(text=f"{inches:.2f} inches = {cm:.2f} centimeters")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          label = tk.Label(self.root, text="Centimeters to Inches", **label_style)
          label.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry = tk.Entry(self.root, **entry_style)
          entry.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img = Image.open("Unit Converter Images/convert.png")
          convert_img = convert_img.resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)

          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=cm_to_in)
          convert_button.place(x=245, y=158)

          label2 = tk.Label(self.root, text="Inches to Centimeters", **label_style)
          label2.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry2 = tk.Entry(self.root, **entry_style)
          entry2.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img2 = Image.open("Unit Converter Images/convert.png")
          convert_img2 = convert_img2.resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)

          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=in_to_cm)
          convert_button2.place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ------------------------------------------------------------------------------------------------

      def mi__km(self):
          self.clean_window()
          self.root.title("Length Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.length_menu)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Length Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

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

          result_style = {
              "font": ("Segoe UI", 13, "bold"),
              "bg": "#f5f6fa",
              "fg": "#27ae60",
              "relief": "flat",
              "anchor": "center",
              "bd": 1
          }

          def mi_to_km():
              miles = entry.get()
              if not miles:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not miles.isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              miles = float(miles)
              km = miles * 1.60934
              result_label.configure(text=f"{miles:.2f} miles = {km:.2f} kilometers")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def km_to_mi():
              km = entry2.get()
              if not km:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not km.isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              km = float(km)
              miles = km / 1.60934
              result_label.configure(text=f"{km:.2f} kilometers = {miles:.2f} miles")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          label = tk.Label(self.root, text="Miles to Kilometers", **label_style)
          label.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry = tk.Entry(self.root, **entry_style)
          entry.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img = Image.open("Unit Converter Images/convert.png")
          convert_img = convert_img.resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)

          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=mi_to_km)
          convert_button.place(x=245, y=158)

          label2 = tk.Label(self.root, text="Kilometers to Miles", **label_style)
          label2.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry2 = tk.Entry(self.root, **entry_style)
          entry2.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img2 = Image.open("Unit Converter Images/convert.png")
          convert_img2 = convert_img2.resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)

          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=km_to_mi)
          convert_button2.place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ------------------------------------------------------------------------------------------------

      def m__yd(self):
          self.clean_window()
          self.root.title("Length Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.length_menu)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Length Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

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

          result_style = {
              "font": ("Segoe UI", 13, "bold"),
              "bg": "#f5f6fa",
              "fg": "#27ae60",
              "relief": "flat",
              "anchor": "center",
              "bd": 1
          }

          def m_to_yd():
              meters = entry.get()
              if not meters:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not meters.isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              meters = float(meters)
              yards = meters * 1.09361
              result_label.configure(text=f"{meters:.2f} meters = {yards:.2f} yards")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def yd_to_m():
              yards = entry2.get()
              if not yards:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not yards.isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              yards = float(yards)
              meters = yards / 1.09361
              result_label.configure(text=f"{yards:.2f} yards = {meters:.2f} meters")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          label = tk.Label(self.root, text="Meters to Yards", **label_style)
          label.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry = tk.Entry(self.root, **entry_style)
          entry.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img = Image.open("Unit Converter Images/convert.png")
          convert_img = convert_img.resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)

          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=m_to_yd)
          convert_button.place(x=245, y=158)

          label2 = tk.Label(self.root, text="Yards to Meters", **label_style)
          label2.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry2 = tk.Entry(self.root, **entry_style)
          entry2.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img2 = Image.open("Unit Converter Images/convert.png")
          convert_img2 = convert_img2.resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)

          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=yd_to_m)
          convert_button2.place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)
      # Length conversions

      # Weight conversions
      def kg__lb(self):
          self.clean_window()
          self.root.title("Weight Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          # Back Button
          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.weight_menu)
          button_back.place(x=15, y=8)

          # Dashboard Label
          label_dashboard = tk.Label(self.root, text="Weight Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          # Styles
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
          result_style = {
              "font": ("Segoe UI", 13, "bold"),
              "bg": "#f5f6fa",
              "fg": "#27ae60",
              "relief": "flat",
              "anchor": "center",
              "bd": 1
          }

          # Conversion Functions
          def kg_to_lb():
              kg = entry.get()
              if not kg:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not kg.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              kg = float(kg)
              lb = kg * 2.20462
              result_label.configure(text=f"{kg:.2f} kg = {lb:.2f} lb")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def lb_to_kg():
              lb = entry2.get()
              if not lb:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not lb.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              lb = float(lb)
              kg = lb / 2.20462
              result_label.configure(text=f"{lb:.2f} lb = {kg:.2f} kg")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # KG → LB
          label = tk.Label(self.root, text="Kilograms to Pounds", **label_style)
          label.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry = tk.Entry(self.root, **entry_style)
          entry.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img = Image.open("Unit Converter Images/convert.png")
          convert_img = convert_img.resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)

          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=kg_to_lb)
          convert_button.place(x=245, y=158)

          # LB → KG
          label2 = tk.Label(self.root, text="Pounds to Kilograms", **label_style)
          label2.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry2 = tk.Entry(self.root, **entry_style)
          entry2.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img2 = Image.open("Unit Converter Images/convert.png")
          convert_img2 = convert_img2.resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)

          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=lb_to_kg)
          convert_button2.place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)

      #-------------------------------------------------------------------------------------------

      def g__kg(self):
          self.clean_window()
          self.root.title("Weight Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          # Back Button
          back_img = Image.open("Unit Converter Images/menu_bar_img.png")
          back_img = back_img.resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)

          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.weight_menu)
          button_back.place(x=15, y=8)

          # Dashboard Label
          label_dashboard = tk.Label(self.root, text="Weight Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          # Styles
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
          result_style = {
              "font": ("Segoe UI", 13, "bold"),
              "bg": "#f5f6fa",
              "fg": "#27ae60",
              "relief": "flat",
              "anchor": "center",
              "bd": 1
          }

          # Conversion Functions
          def g_to_kg():
              grams = entry.get()
              if not grams:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not grams.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              grams = float(grams)
              kg = grams / 1000
              result_label.configure(text=f"{grams:.2f} g = {kg:.2f} kg")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def kg_to_g():
              kg = entry2.get()
              if not kg:
                  messagebox.showwarning("Warning", "Please enter a Value.")
                  return
              if not kg.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Please enter a Number.")
                  return
              kg = float(kg)
              grams = kg * 1000
              result_label.configure(text=f"{kg:.2f} kg = {grams:.2f} g")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # G → KG
          label = tk.Label(self.root, text="Grams to Kilograms", **label_style)
          label.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry = tk.Entry(self.root, **entry_style)
          entry.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img = Image.open("Unit Converter Images/convert.png")
          convert_img = convert_img.resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)

          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=g_to_kg)
          convert_button.place(x=245, y=158)

          # KG → G
          label2 = tk.Label(self.root, text="Kilograms to Grams", **label_style)
          label2.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry2 = tk.Entry(self.root, **entry_style)
          entry2.pack(fill="x", padx=(30, 30), ipady=8)

          convert_img2 = Image.open("Unit Converter Images/convert.png")
          convert_img2 = convert_img2.resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)

          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=kg_to_g)
          convert_button2.place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)

      #-------------------------------------------------------------------------------------------

      def kg__mg(self):
          self.clean_window()
          self.root.title("Weight Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          # Back Button
          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.weight_menu)
          button_back.place(x=15, y=8)

          # Dashboard Label
          label_dashboard = tk.Label(self.root, text="Weight Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          # Styles
          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # Conversion Functions
          def kg_to_mg():
              kg = entry_kg.get()
              if not kg or not kg.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              kg = float(kg)
              mg = kg * 1_000_000
              result_label.configure(text=f"{kg:.2f} kg = {mg:.0f} mg")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def mg_to_kg():
              mg = entry_mg.get()
              if not mg or not mg.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              mg = float(mg)
              kg = mg / 1_000_000
              result_label.configure(text=f"{mg:.0f} mg = {kg:.2f} kg")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # KG → MG
          label_kg = tk.Label(self.root, text="Kilograms to Milligrams", **label_style)
          label_kg.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_kg = tk.Entry(self.root, **entry_style)
          entry_kg.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)
          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=kg_to_mg)
          convert_button.place(x=245, y=158)

          # MG → KG
          label_mg = tk.Label(self.root, text="Milligrams to Kilograms", **label_style)
          label_mg.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_mg = tk.Entry(self.root, **entry_style)
          entry_mg.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=mg_to_kg)
          convert_button2.place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)

      #-------------------------------------------------------------------------------------------
      def oz__g(self):
          self.clean_window()
          self.root.title("Weight Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.weight_menu)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Weight Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def oz_to_g():
              oz = entry_oz.get()
              if not oz or not oz.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              oz = float(oz)
              g = oz * 28.3495
              result_label.configure(text=f"{oz:.2f} oz = {g:.2f} g")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def g_to_oz():
              g = entry_g.get()
              if not g or not g.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              g = float(g)
              oz = g / 28.3495
              result_label.configure(text=f"{g:.2f} g = {oz:.2f} oz")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # OZ → G
          label_oz = tk.Label(self.root, text="Ounces to Grams", **label_style)
          label_oz.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_oz = tk.Entry(self.root, **entry_style)
          entry_oz.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)
          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=oz_to_g)
          convert_button.place(x=245, y=158)

          # G → OZ
          label_g = tk.Label(self.root, text="Grams to Ounces", **label_style)
          label_g.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_g = tk.Entry(self.root, **entry_style)
          entry_g.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=g_to_oz)
          convert_button2.place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      #-------------------------------------------------------------------------------------------
      def ton__kg(self):
          self.clean_window()
          self.root.title("Weight Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.weight_menu)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Weight Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def ton_to_kg():
              ton = entry_ton.get()
              if not ton or not ton.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              ton = float(ton)
              kg = ton * 1000
              result_label.configure(text=f"{ton:.2f} ton = {kg:.2f} kg")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def kg_to_ton():
              kg = entry_kg.get()
              if not kg or not kg.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              kg = float(kg)
              ton = kg / 1000
              result_label.configure(text=f"{kg:.2f} kg = {ton:.2f} ton")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # Ton → KG
          label_ton = tk.Label(self.root, text="Tons to Kilograms", **label_style)
          label_ton.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_ton = tk.Entry(self.root, **entry_style)
          entry_ton.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)
          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=ton_to_kg)
          convert_button.place(x=245, y=158)

          # KG → Ton
          label_kg = tk.Label(self.root, text="Kilograms to Tons", **label_style)
          label_kg.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_kg = tk.Entry(self.root, **entry_style)
          entry_kg.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=kg_to_ton)
          convert_button2.place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      #-------------------------------------------------------------------------------------------

      def lb__oz(self):
          self.clean_window()
          self.root.title("Weight Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.weight_menu)
          button_back.place(x=15, y=8)

          label_dashboard = tk.Label(self.root, text="Weight Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def lb_to_oz():
              lb = entry_lb.get()
              if not lb or not lb.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              lb = float(lb)
              oz = lb * 16
              result_label.configure(text=f"{lb:.2f} lb = {oz:.2f} oz")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def oz_to_lb():
              oz = entry_oz.get()
              if not oz or not oz.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              oz = float(oz)
              lb = oz / 16
              result_label.configure(text=f"{oz:.2f} oz = {lb:.2f} lb")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # LB → OZ
          label_lb = tk.Label(self.root, text="Pounds to Ounces", **label_style)
          label_lb.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_lb = tk.Entry(self.root, **entry_style)
          entry_lb.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)
          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=lb_to_oz)
          convert_button.place(x=245, y=158)

          # OZ → LB
          label_oz = tk.Label(self.root, text="Ounces to Pounds", **label_style)
          label_oz.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_oz = tk.Entry(self.root, **entry_style)
          entry_oz.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=oz_to_lb)
          convert_button2.place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)
      # Weight conversions

      # Temperature conversions
      def c__f(self):
          self.clean_window()
          self.root.title("Temp Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          # Back Button
          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.temp_menu)
          button_back.place(x=15, y=8)

          # Dashboard Label
          label_dashboard = tk.Label(self.root, text="Temp Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          # Styles
          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # Conversion Functions
          def c_to_f():
              c = entry_c.get()
              if not c or not c.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Please enter a valid number.")
                  return
              c = float(c)
              f = (c * 9 / 5) + 32
              result_label.configure(text=f"{c:.2f} °C = {f:.2f} °F")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def f_to_c():
              f = entry_f.get()
              if not f or not f.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Please enter a valid number.")
                  return
              f = float(f)
              c = (f - 32) * 5 / 9
              result_label.configure(text=f"{f:.2f} °F = {c:.2f} °C")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # Celsius → Fahrenheit
          label_c = tk.Label(self.root, text="Celsius to Fahrenheit", **label_style)
          label_c.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_c = tk.Entry(self.root, **entry_style)
          entry_c.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)
          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=c_to_f)
          convert_button.place(x=245, y=158)

          # Fahrenheit → Celsius
          label_f = tk.Label(self.root, text="Fahrenheit to Celsius", **label_style)
          label_f.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_f = tk.Entry(self.root, **entry_style)
          entry_f.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=f_to_c)
          convert_button2.place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)
      # ------------------------------------------------------------------------------------------------
      def c__k(self):
          self.clean_window()
          self.root.title("Temp Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          # Back Button
          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.temp_menu)
          button_back.place(x=15, y=8)

          # Dashboard Label
          label_dashboard = tk.Label(self.root, text="Temp Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          # Styles
          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # Conversion Functions
          def c_to_k():
              c = entry_c.get()
              if not c or not c.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              c = float(c)
              k = c + 273.15
              result_label.configure(text=f"{c:.2f} °C = {k:.2f} K")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def k_to_c():
              k = entry_k.get()
              if not k or not k.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              k = float(k)
              c = k - 273.15
              result_label.configure(text=f"{k:.2f} K = {c:.2f} °C")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # Celsius → Kelvin
          label_c = tk.Label(self.root, text="Celsius to Kelvin", **label_style)
          label_c.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_c = tk.Entry(self.root, **entry_style)
          entry_c.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)
          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=c_to_k)
          convert_button.place(x=245, y=158)

          # Kelvin → Celsius
          label_k = tk.Label(self.root, text="Kelvin to Celsius", **label_style)
          label_k.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_k = tk.Entry(self.root, **entry_style)
          entry_k.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=k_to_c)
          convert_button2.place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)

      # ------------------------------------------------------------------------------------------------
      def f__k(self):
          self.clean_window()
          self.root.title("Temp Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          # Back Button
          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.temp_menu)
          button_back.place(x=15, y=8)

          # Dashboard Label
          label_dashboard = tk.Label(self.root, text="Temp Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          # Styles
          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # Conversion Functions
          def f_to_k():
              f = entry_f.get()
              if not f or not f.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              f = float(f)
              k = (f - 32) * 5 / 9 + 273.15
              result_label.configure(text=f"{f:.2f} °F = {k:.2f} K")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def k_to_f():
              k = entry_k.get()
              if not k or not k.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              k = float(k)
              f = (k - 273.15) * 9 / 5 + 32
              result_label.configure(text=f"{k:.2f} K = {f:.2f} °F")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # Fahrenheit → Kelvin
          label_f = tk.Label(self.root, text="Fahrenheit to Kelvin", **label_style)
          label_f.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_f = tk.Entry(self.root, **entry_style)
          entry_f.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)
          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=f_to_k)
          convert_button.place(x=245, y=158)

          # Kelvin → Fahrenheit
          label_k = tk.Label(self.root, text="Kelvin to Fahrenheit", **label_style)
          label_k.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_k = tk.Entry(self.root, **entry_style)
          entry_k.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=k_to_f)
          convert_button2.place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)

      # ------------------------------------------------------------------------------------------------
      def c__r(self):
          self.clean_window()
          self.root.title("Temp Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          # Back Button
          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.temp_menu)
          button_back.place(x=15, y=8)

          # Dashboard Label
          label_dashboard = tk.Label(self.root, text="Temp Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          # Styles
          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # Conversion Functions
          def c_to_r():
              c = entry_c.get()
              if not c or not c.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              c = float(c)
              r = c * 0.8
              result_label.configure(text=f"{c:.2f} °C = {r:.2f} °R")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def r_to_c():
              r = entry_r.get()
              if not r or not r.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              r = float(r)
              c = r / 0.8
              result_label.configure(text=f"{r:.2f} °R = {c:.2f} °C")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # Celsius → Reaumur
          label_c = tk.Label(self.root, text="Celsius to Reaumur", **label_style)
          label_c.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_c = tk.Entry(self.root, **entry_style)
          entry_c.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)
          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=c_to_r)
          convert_button.place(x=245, y=158)

          # Reaumur → Celsius
          label_r = tk.Label(self.root, text="Reaumur to Celsius", **label_style)
          label_r.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_r = tk.Entry(self.root, **entry_style)
          entry_r.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=r_to_c)
          convert_button2.place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)

      # ------------------------------------------------------------------------------------------------
      def f__r(self):
          self.clean_window()
          self.root.title("Temp Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          # Back Button
          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.temp_menu)
          button_back.place(x=15, y=8)

          # Dashboard Label
          label_dashboard = tk.Label(self.root, text="Temp Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          # Styles
          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # Conversion Functions
          def f_to_r():
              f = entry_f.get()
              if not f or not f.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              f = float(f)
              r = (f - 32) * 4 / 9
              result_label.configure(text=f"{f:.2f} °F = {r:.2f} °R")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def r_to_f():
              r = entry_r.get()
              if not r or not r.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              r = float(r)
              f = r * 9 / 4 + 32
              result_label.configure(text=f"{r:.2f} °R = {f:.2f} °F")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # Fahrenheit → Reaumur
          label_f = tk.Label(self.root, text="Fahrenheit to Reaumur", **label_style)
          label_f.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_f = tk.Entry(self.root, **entry_style)
          entry_f.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)
          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=f_to_r)
          convert_button.place(x=245, y=158)

          # Reaumur → Fahrenheit
          label_r = tk.Label(self.root, text="Reaumur to Fahrenheit", **label_style)
          label_r.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_r = tk.Entry(self.root, **entry_style)
          entry_r.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=r_to_f)
          convert_button2.place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)

      # ------------------------------------------------------------------------------------------------
      def k__r(self):
          self.clean_window()
          self.root.title("Temp Conversions")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          # Back Button
          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.temp_menu)
          button_back.place(x=15, y=8)

          # Dashboard Label
          label_dashboard = tk.Label(self.root, text="Temp Conversions",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          # Styles
          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # Conversion Functions
          def k_to_r():
              k = entry_k.get()
              if not k or not k.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              k = float(k)
              r = (k - 273.15) * 0.8
              result_label.configure(text=f"{k:.2f} K = {r:.2f} °R")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def r_to_k():
              r = entry_r.get()
              if not r or not r.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              r = float(r)
              k = r / 0.8 + 273.15
              result_label.configure(text=f"{r:.2f} °R = {k:.2f} K")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # Kelvin → Reaumur
          label_k = tk.Label(self.root, text="Kelvin to Reaumur", **label_style)
          label_k.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_k = tk.Entry(self.root, **entry_style)
          entry_k.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)
          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=k_to_r)
          convert_button.place(x=245, y=158)

          # Reaumur → Kelvin
          label_r = tk.Label(self.root, text="Reaumur to Kelvin", **label_style)
          label_r.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_r = tk.Entry(self.root, **entry_style)
          entry_r.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=r_to_k)
          convert_button2.place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)
      # Temperature conversions

      # Time conversions
      def hr__min(self):
          self.clean_window()
          self.root.title("Time Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          # Back Button
          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.time_menu)
          button_back.place(x=15, y=8)

          # Dashboard Label
          label_dashboard = tk.Label(self.root, text="Time Conversion",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          # Styles
          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # Conversion Functions
          def hr_to_min():
              hr = entry_hr.get()
              if not hr or not hr.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              hr = float(hr)
              minutes = hr * 60
              result_label.configure(text=f"{hr:.2f} Hours = {minutes:.2f} Minutes")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def min_to_hr():
              minutes = entry_min.get()
              if not minutes or not minutes.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              minutes = float(minutes)
              hr = minutes / 60
              result_label.configure(text=f"{minutes:.2f} Minutes = {hr:.2f} Hours")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # Hours → Minutes
          label_hr = tk.Label(self.root, text="Hours to Minutes", **label_style)
          label_hr.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_hr = tk.Entry(self.root, **entry_style)
          entry_hr.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)
          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=hr_to_min)
          convert_button.place(x=245, y=158)

          # Minutes → Hours
          label_min = tk.Label(self.root, text="Minutes to Hours", **label_style)
          label_min.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_min = tk.Entry(self.root, **entry_style)
          entry_min.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=min_to_hr)
          convert_button2.place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________________
      def hr__sec(self):
          self.clean_window()
          self.root.title("Time Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          # Back Button
          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          button_back = tk.Button(self.root, image=self.back_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command=self.time_menu)
          button_back.place(x=15, y=8)

          # Dashboard Label
          label_dashboard = tk.Label(self.root, text="Time Conversion",
                                     bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold'))
          label_dashboard.place(x=50, y=2)

          # Styles
          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # Conversion Functions
          def hr_to_sec():
              hr = entry_hr.get()
              if not hr or not hr.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              hr = float(hr)
              sec = hr * 3600
              result_label.configure(text=f"{hr:.2f} Hours = {sec:.2f} Seconds")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def sec_to_hr():
              sec = entry_sec.get()
              if not sec or not sec.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter a valid number.")
                  return
              sec = float(sec)
              hr = sec / 3600
              result_label.configure(text=f"{sec:.2f} Seconds = {hr:.2f} Hours")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # Hours → Seconds
          label_hr = tk.Label(self.root, text="Hours to Seconds", **label_style)
          label_hr.pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_hr = tk.Entry(self.root, **entry_style)
          entry_hr.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button = ImageTk.PhotoImage(convert_img)
          convert_button = tk.Button(self.root, image=self.convert_img_button,
                                     bg='#ffffff', relief='flat', bd=0, command=hr_to_sec)
          convert_button.place(x=245, y=158)

          # Seconds → Hours
          label_sec = tk.Label(self.root, text="Seconds to Hours", **label_style)
          label_sec.pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_sec = tk.Entry(self.root, **entry_style)
          entry_sec.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          convert_button2 = tk.Button(self.root, image=self.convert_img_button2,
                                      bg='#ffffff', relief='flat', bd=0, command=sec_to_hr)
          convert_button2.place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________________

      def sec__min(self):
          self.clean_window()
          self.root.title("Time Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.time_menu).place(x=15, y=8)

          tk.Label(self.root, text="Time Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def sec_to_min():
              val = entry_sec.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              mins = float(val) / 60
              result_label.configure(text=f"{val} Seconds = {mins:.2f} Minutes")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def min_to_sec():
              val = entry_min.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              sec = float(val) * 60
              result_label.configure(text=f"{val} Minutes = {sec:.2f} Seconds")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Seconds to Minutes", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_sec = tk.Entry(self.root, **entry_style)
          entry_sec.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button3 = ImageTk.PhotoImage(convert_img)
          tk.Button(self.root, image=self.convert_img_button3,
                    bg='#ffffff', relief='flat', bd=0, command=sec_to_min).place(x=245, y=158)

          tk.Label(self.root, text="Minutes to Seconds", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_min = tk.Entry(self.root, **entry_style)
          entry_min.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button4 = ImageTk.PhotoImage(convert_img2)
          tk.Button(self.root, image=self.convert_img_button4,
                    bg='#ffffff', relief='flat', bd=0, command=min_to_sec).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________________

      def day__hr(self):
          self.clean_window()
          self.root.title("Time Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.time_menu).place(x=15, y=8)

          tk.Label(self.root, text="Time Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def day_to_hr():
              val = entry_day.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              hr = float(val) * 24
              result_label.configure(text=f"{val} Days = {hr:.2f} Hours")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def hr_to_day():
              val = entry_hr.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              days = float(val) / 24
              result_label.configure(text=f"{val} Hours = {days:.2f} Days")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Days to Hours", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_day = tk.Entry(self.root, **entry_style)
          entry_day.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button5 = ImageTk.PhotoImage(convert_img)
          tk.Button(self.root, image=self.convert_img_button5,
                    bg='#ffffff', relief='flat', bd=0, command=day_to_hr).place(x=245, y=158)

          tk.Label(self.root, text="Hours to Days", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_hr = tk.Entry(self.root, **entry_style)
          entry_hr.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button6 = ImageTk.PhotoImage(convert_img2)
          tk.Button(self.root, image=self.convert_img_button6,
                    bg='#ffffff', relief='flat', bd=0, command=hr_to_day).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________________

      def wk__day(self):
          self.clean_window()
          self.root.title("Time Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.time_menu).place(x=15, y=8)

          tk.Label(self.root, text="Time Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def wk_to_day():
              val = entry_wk.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              days = float(val) * 7
              result_label.configure(text=f"{val} Weeks = {days:.2f} Days")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def day_to_wk():
              val = entry_day.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              weeks = float(val) / 7
              result_label.configure(text=f"{val} Days = {weeks:.2f} Weeks")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Weeks to Days", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_wk = tk.Entry(self.root, **entry_style)
          entry_wk.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button7 = ImageTk.PhotoImage(convert_img)
          tk.Button(self.root, image=self.convert_img_button7,
                    bg='#ffffff', relief='flat', bd=0, command=wk_to_day).place(x=245, y=158)

          tk.Label(self.root, text="Days to Weeks", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_day = tk.Entry(self.root, **entry_style)
          entry_day.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button8 = ImageTk.PhotoImage(convert_img2)
          tk.Button(self.root, image=self.convert_img_button8,
                    bg='#ffffff', relief='flat', bd=0, command=day_to_wk).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________________

      def mon__day(self):
          self.clean_window()
          self.root.title("Time Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.time_menu).place(x=15, y=8)

          tk.Label(self.root, text="Time Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def mon_to_day():
              val = entry_mon.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              days = float(val) * 30
              result_label.configure(text=f"{val} Months = {days:.2f} Days (approx)")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def day_to_mon():
              val = entry_day.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              mon = float(val) / 30
              result_label.configure(text=f"{val} Days = {mon:.2f} Months (approx)")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Months to Days", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_mon = tk.Entry(self.root, **entry_style)
          entry_mon.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button9 = ImageTk.PhotoImage(convert_img)
          tk.Button(self.root, image=self.convert_img_button9,
                    bg='#ffffff', relief='flat', bd=0, command=mon_to_day).place(x=245, y=158)

          tk.Label(self.root, text="Days to Months", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_day = tk.Entry(self.root, **entry_style)
          entry_day.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button10 = ImageTk.PhotoImage(convert_img2)
          tk.Button(self.root, image=self.convert_img_button10,
                    bg='#ffffff', relief='flat', bd=0, command=day_to_mon).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)
      # Time conversion

      # Area conversions
      def m2__ft2(self):
          self.clean_window()
          self.root.title("Area Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.area_menu).place(x=15, y=8)

          tk.Label(self.root, text="Area Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          # Styles
          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # Conversion functions
          def m2_to_ft2():
              val = entry_m2.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              ft2 = float(val) * 10.7639
              result_label.configure(text=f"{val} m² = {ft2:.2f} ft²")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def ft2_to_m2():
              val = entry_ft2.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              m2 = float(val) / 10.7639
              result_label.configure(text=f"{val} ft² = {m2:.2f} m²")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # m² → ft²
          tk.Label(self.root, text="Square Meter to Square Feet", **label_style).pack(fill="x", padx=(29, 0),
                                                                                      pady=(80, 7))
          entry_m2 = tk.Entry(self.root, **entry_style)
          entry_m2.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button1 = ImageTk.PhotoImage(convert_img)
          tk.Button(self.root, image=self.convert_img_button1,
                    bg='#ffffff', relief='flat', bd=0, command=m2_to_ft2).place(x=245, y=158)

          # ft² → m²
          tk.Label(self.root, text="Square Feet to Square Meter", **label_style).pack(fill="x", padx=(29, 0),
                                                                                      pady=(90, 7))
          entry_ft2 = tk.Entry(self.root, **entry_style)
          entry_ft2.pack(fill="x", padx=(30, 30), ipady=8)
          convert_img2 = Image.open("Unit Converter Images/convert.png").resize((105, 55))
          self.convert_img_button2 = ImageTk.PhotoImage(convert_img2)
          tk.Button(self.root, image=self.convert_img_button2,
                    bg='#ffffff', relief='flat', bd=0, command=ft2_to_m2).place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)

      # _____________________________________________________________________________________

      def km2__ha(self):
          self.clean_window()
          self.root.title("Area Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.area_menu).place(x=15, y=8)

          tk.Label(self.root, text="Area Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def km2_to_ha():
              val = entry_km2.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              ha = float(val) * 100
              result_label.configure(text=f"{val} km² = {ha:.2f} hectares")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def ha_to_km2():
              val = entry_ha.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              km2 = float(val) / 100
              result_label.configure(text=f"{val} hectares = {km2:.2f} km²")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Square Kilometer to Hectare", **label_style).pack(fill="x", padx=(29, 0),
                                                                                      pady=(80, 7))
          entry_km2 = tk.Entry(self.root, **entry_style);
          entry_km2.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=km2_to_ha).place(x=245, y=158)

          tk.Label(self.root, text="Hectare to Square Kilometer", **label_style).pack(fill="x", padx=(29, 0),
                                                                                      pady=(90, 7))
          entry_ha = tk.Entry(self.root, **entry_style);
          entry_ha.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=ha_to_km2).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # _____________________________________________________________________________________

      def ac__m2(self):
          self.clean_window()
          self.root.title("Area Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.area_menu).place(x=15, y=8)

          tk.Label(self.root, text="Area Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def ac_to_m2():
              val = entry_ac.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              m2 = float(val) * 4046.86
              result_label.configure(text=f"{val} acres = {m2:.2f} m²")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def m2_to_ac():
              val = entry_m2.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              ac = float(val) / 4046.86
              result_label.configure(text=f"{val} m² = {ac:.2f} acres")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Acre to Square Meter", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_ac = tk.Entry(self.root, **entry_style);
          entry_ac.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=ac_to_m2).place(x=245, y=158)

          tk.Label(self.root, text="Square Meter to Acre", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_m2 = tk.Entry(self.root, **entry_style);
          entry_m2.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=m2_to_ac).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # _____________________________________________________________________________________

      def yd2__ft2(self):
          self.clean_window()
          self.root.title("Area Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.area_menu).place(x=15, y=8)

          tk.Label(self.root, text="Area Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def yd2_to_ft2():
              val = entry_yd2.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              ft2 = float(val) * 9
              result_label.configure(text=f"{val} yd² = {ft2:.2f} ft²")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def ft2_to_yd2():
              val = entry_ft2.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              yd2 = float(val) / 9
              result_label.configure(text=f"{val} ft² = {yd2:.2f} yd²")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Square Yard to Square Feet", **label_style).pack(fill="x", padx=(29, 0),
                                                                                     pady=(80, 7))
          entry_yd2 = tk.Entry(self.root, **entry_style);
          entry_yd2.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=yd2_to_ft2).place(x=245, y=158)

          tk.Label(self.root, text="Square Feet to Square Yard", **label_style).pack(fill="x", padx=(29, 0),
                                                                                     pady=(90, 7))
          entry_ft2 = tk.Entry(self.root, **entry_style);
          entry_ft2.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=ft2_to_yd2).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # _____________________________________________________________________________________

      def in2__cm2(self):
          self.clean_window()
          self.root.title("Area Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.area_menu).place(x=15, y=8)

          tk.Label(self.root, text="Area Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def in2_to_cm2():
              val = entry_in2.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              cm2 = float(val) * 6.4516
              result_label.configure(text=f"{val} in² = {cm2:.2f} cm²")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def cm2_to_in2():
              val = entry_cm2.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              in2 = float(val) / 6.4516
              result_label.configure(text=f"{val} cm² = {in2:.2f} in²")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Square Inch to Square Centimeter", **label_style).pack(fill="x", padx=(29, 0),
                                                                                           pady=(80, 7))
          entry_in2 = tk.Entry(self.root, **entry_style);
          entry_in2.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=in2_to_cm2).place(x=245, y=158)

          tk.Label(self.root, text="Square Centimeter to Square Inch", **label_style).pack(fill="x", padx=(29, 0),
                                                                                           pady=(90, 7))
          entry_cm2 = tk.Entry(self.root, **entry_style);
          entry_cm2.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=cm2_to_in2).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # _____________________________________________________________________________________

      def mi2__ac(self):
          self.clean_window()
          self.root.title("Area Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.area_menu).place(x=15, y=8)

          tk.Label(self.root, text="Area Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def mi2_to_ac():
              val = entry_mi2.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              ac = float(val) * 640
              result_label.configure(text=f"{val} mi² = {ac:.2f} acres")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def ac_to_mi2():
              val = entry_ac.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              mi2 = float(val) / 640
              result_label.configure(text=f"{val} acres = {mi2:.2f} mi²")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Square Mile to Acre", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_mi2 = tk.Entry(self.root, **entry_style);
          entry_mi2.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=mi2_to_ac).place(x=245, y=158)

          tk.Label(self.root, text="Acre to Square Mile", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_ac = tk.Entry(self.root, **entry_style);
          entry_ac.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=ac_to_mi2).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)
      # Area conversions

      # Volume conversions
      def l__ml(self):
          self.clean_window()
          self.root.title("Volume Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.volume_menu).place(x=15, y=8)

          tk.Label(self.root, text="Volume Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # Conversion functions
          def l_to_ml():
              val = entry_l.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              ml = float(val) * 1000
              result_label.configure(text=f"{val} L = {ml:.2f} mL")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def ml_to_l():
              val = entry_ml.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              l = float(val) / 1000
              result_label.configure(text=f"{val} mL = {l:.2f} L")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # Liters → Milliliters
          tk.Label(self.root, text="Liters to Milliliters", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_l = tk.Entry(self.root, **entry_style);
          entry_l.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=l_to_ml).place(x=245, y=158)

          # Milliliters → Liters
          tk.Label(self.root, text="Milliliters to Liters", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_ml = tk.Entry(self.root, **entry_style);
          entry_ml.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=ml_to_l).place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)

      # ____________________________________________________________________________________________

      def l__gal(self):
          self.clean_window()
          self.root.title("Volume Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.volume_menu).place(x=15, y=8)

          tk.Label(self.root, text="Volume Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # 1 liter = 0.264172 gallons (US)
          def l_to_gal():
              val = entry_l.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              gal = float(val) * 0.264172
              result_label.configure(text=f"{val} L = {gal:.2f} gal")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def gal_to_l():
              val = entry_gal.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              l = float(val) / 0.264172
              result_label.configure(text=f"{val} gal = {l:.2f} L")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # Liters → Gallons
          tk.Label(self.root, text="Liters to Gallons", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_l = tk.Entry(self.root, **entry_style);
          entry_l.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=l_to_gal).place(x=245, y=158)

          # Gallons → Liters
          tk.Label(self.root, text="Gallons to Liters", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_gal = tk.Entry(self.root, **entry_style);
          entry_gal.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=gal_to_l).place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)

      # ____________________________________________________________________________________________

      def m3__l(self):
          self.clean_window()
          self.root.title("Volume Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.volume_menu).place(x=15, y=8)

          tk.Label(self.root, text="Volume Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # 1 m³ = 1000 liters
          def m3_to_l():
              val = entry_m3.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              l = float(val) * 1000
              result_label.configure(text=f"{val} m³ = {l:.2f} L")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def l_to_m3():
              val = entry_l.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              m3 = float(val) / 1000
              result_label.configure(text=f"{val} L = {m3:.3f} m³")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Cubic Meter to Liter", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_m3 = tk.Entry(self.root, **entry_style);
          entry_m3.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=m3_to_l).place(x=245, y=158)

          tk.Label(self.root, text="Liter to Cubic Meter", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_l = tk.Entry(self.root, **entry_style);
          entry_l.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=l_to_m3).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ____________________________________________________________________________________________

      def cm3__ml(self):
          self.clean_window()
          self.root.title("Volume Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.volume_menu).place(x=15, y=8)

          tk.Label(self.root, text="Volume Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # 1 cm³ = 1 ml
          def cm3_to_ml():
              val = entry_cm3.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              ml = float(val) * 1
              result_label.configure(text=f"{val} cm³ = {ml:.2f} mL")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def ml_to_cm3():
              val = entry_ml.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              cm3 = float(val) * 1
              result_label.configure(text=f"{val} mL = {cm3:.2f} cm³")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Cubic Centimeter to Milliliter", **label_style).pack(fill="x", padx=(29, 0),
                                                                                         pady=(80, 7))
          entry_cm3 = tk.Entry(self.root, **entry_style);
          entry_cm3.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=cm3_to_ml).place(x=245, y=158)

          tk.Label(self.root, text="Milliliter to Cubic Centimeter", **label_style).pack(fill="x", padx=(29, 0),
                                                                                         pady=(90, 7))
          entry_ml = tk.Entry(self.root, **entry_style);
          entry_ml.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=ml_to_cm3).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ____________________________________________________________________________________________

      def in3__cm3(self):
          self.clean_window()
          self.root.title("Volume Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.volume_menu).place(x=15, y=8)

          tk.Label(self.root, text="Volume Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # 1 in³ = 16.387 cm³
          def in3_to_cm3():
              val = entry_in3.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              cm3 = float(val) * 16.387
              result_label.configure(text=f"{val} in³ = {cm3:.2f} cm³")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def cm3_to_in3():
              val = entry_cm3.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              in3 = float(val) / 16.387
              result_label.configure(text=f"{val} cm³ = {in3:.2f} in³")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Cubic Inch to Cubic Centimeter", **label_style).pack(fill="x", padx=(29, 0),
                                                                                         pady=(80, 7))
          entry_in3 = tk.Entry(self.root, **entry_style);
          entry_in3.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=in3_to_cm3).place(x=245, y=158)

          tk.Label(self.root, text="Cubic Centimeter to Cubic Inch", **label_style).pack(fill="x", padx=(29, 0),
                                                                                         pady=(90, 7))
          entry_cm3 = tk.Entry(self.root, **entry_style);
          entry_cm3.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=cm3_to_in3).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ____________________________________________________________________________________________

      def ft3__gal(self):
          self.clean_window()
          self.root.title("Volume Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.volume_menu).place(x=15, y=8)

          tk.Label(self.root, text="Volume Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # 1 ft³ = 7.48052 gallons
          def ft3_to_gal():
              val = entry_ft3.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              gal = float(val) * 7.48052
              result_label.configure(text=f"{val} ft³ = {gal:.2f} gal")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def gal_to_ft3():
              val = entry_gal.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              ft3 = float(val) / 7.48052
              result_label.configure(text=f"{val} gal = {ft3:.2f} ft³")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Cubic Feet to Gallons", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_ft3 = tk.Entry(self.root, **entry_style);
          entry_ft3.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=ft3_to_gal).place(x=245, y=158)

          tk.Label(self.root, text="Gallons to Cubic Feet", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_gal = tk.Entry(self.root, **entry_style);
          entry_gal.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=gal_to_ft3).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)
      # Volume conversions

      # Speed conversions
      def kmh__mph(self):
          self.clean_window()
          self.root.title("Speed Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.speed_menu).place(x=15, y=8)

          tk.Label(self.root, text="Speed Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def kmh_to_mph():
              val = entry_kmh.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              mph = float(val) * 0.621371
              result_label.configure(text=f"{val} km/h = {mph:.2f} mph")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def mph_to_kmh():
              val = entry_mph.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              kmh = float(val) / 0.621371
              result_label.configure(text=f"{val} mph = {kmh:.2f} km/h")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Kilometers/hour to Miles/hour", **label_style).pack(fill="x", padx=(29, 0),
                                                                                        pady=(80, 7))
          entry_kmh = tk.Entry(self.root, **entry_style);
          entry_kmh.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=kmh_to_mph).place(x=245, y=158)

          tk.Label(self.root, text="Miles/hour to Kilometers/hour", **label_style).pack(fill="x", padx=(29, 0),
                                                                                        pady=(90, 7))
          entry_mph = tk.Entry(self.root, **entry_style);
          entry_mph.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=mph_to_kmh).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________

      def ms__kmh(self):
          self.clean_window()
          self.root.title("Speed Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.speed_menu).place(x=15, y=8)

          tk.Label(self.root, text="Speed Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def ms_to_kmh():
              val = entry_ms.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              kmh = float(val) * 3.6
              result_label.configure(text=f"{val} m/s = {kmh:.2f} km/h")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def kmh_to_ms():
              val = entry_kmh.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              ms = float(val) / 3.6
              result_label.configure(text=f"{val} km/h = {ms:.2f} m/s")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Meters/second to Kilometers/hour", **label_style).pack(fill="x", padx=(29, 0),
                                                                                           pady=(80, 7))
          entry_ms = tk.Entry(self.root, **entry_style);
          entry_ms.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=ms_to_kmh).place(x=245, y=158)

          tk.Label(self.root, text="Kilometers/hour to Meters/second", **label_style).pack(fill="x", padx=(29, 0),
                                                                                           pady=(90, 7))
          entry_kmh = tk.Entry(self.root, **entry_style);
          entry_kmh.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=kmh_to_ms).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________

      def ms__mph(self):
          self.clean_window()
          self.root.title("Speed Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.speed_menu).place(x=15, y=8)

          tk.Label(self.root, text="Speed Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def ms_to_mph():
              val = entry_ms.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              mph = float(val) * 2.23694
              result_label.configure(text=f"{val} m/s = {mph:.2f} mph")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def mph_to_ms():
              val = entry_mph.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              ms = float(val) / 2.23694
              result_label.configure(text=f"{val} mph = {ms:.2f} m/s")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Meters/second to Miles/hour", **label_style).pack(fill="x", padx=(29, 0),
                                                                                      pady=(80, 7))
          entry_ms = tk.Entry(self.root, **entry_style);
          entry_ms.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=ms_to_mph).place(x=245, y=158)

          tk.Label(self.root, text="Miles/hour to Meters/second", **label_style).pack(fill="x", padx=(29, 0),
                                                                                      pady=(90, 7))
          entry_mph = tk.Entry(self.root, **entry_style);
          entry_mph.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=mph_to_ms).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________

      def kn__kmh(self):
          self.clean_window()
          self.root.title("Speed Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.speed_menu).place(x=15, y=8)

          tk.Label(self.root, text="Speed Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def kn_to_kmh():
              val = entry_kn.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              kmh = float(val) * 1.852
              result_label.configure(text=f"{val} knots = {kmh:.2f} km/h")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def kmh_to_kn():
              val = entry_kmh.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              kn = float(val) / 1.852
              result_label.configure(text=f"{val} km/h = {kn:.2f} knots")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Knots to Kilometers/hour", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_kn = tk.Entry(self.root, **entry_style);
          entry_kn.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=kn_to_kmh).place(x=245, y=158)

          tk.Label(self.root, text="Kilometers/hour to Knots", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_kmh = tk.Entry(self.root, **entry_style);
          entry_kmh.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=kmh_to_kn).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________

      def fts__ms(self):
          self.clean_window()
          self.root.title("Speed Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.speed_menu).place(x=15, y=8)

          tk.Label(self.root, text="Speed Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def fts_to_ms():
              val = entry_fts.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              ms = float(val) * 0.3048
              result_label.configure(text=f"{val} ft/s = {ms:.2f} m/s")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def ms_to_fts():
              val = entry_ms.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              fts = float(val) / 0.3048
              result_label.configure(text=f"{val} m/s = {fts:.2f} ft/s")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Feet/second to Meters/second", **label_style).pack(fill="x", padx=(29, 0),
                                                                                       pady=(80, 7))
          entry_fts = tk.Entry(self.root, **entry_style);
          entry_fts.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=fts_to_ms).place(x=245, y=158)

          tk.Label(self.root, text="Meters/second to Feet/second", **label_style).pack(fill="x", padx=(29, 0),
                                                                                       pady=(90, 7))
          entry_ms = tk.Entry(self.root, **entry_style);
          entry_ms.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=ms_to_fts).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________

      def mach__kmh(self):
          self.clean_window()
          self.root.title("Speed Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.speed_menu).place(x=15, y=8)

          tk.Label(self.root, text="Speed Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          def mach_to_kmh():
              val = entry_mach.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              kmh = float(val) * 1234.8  # Mach 1 ≈ 1234.8 km/h (sea level, 20°C)
              result_label.configure(text=f"{val} Mach = {kmh:.2f} km/h")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def kmh_to_mach():
              val = entry_kmh.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              mach = float(val) / 1234.8
              result_label.configure(text=f"{val} km/h = {mach:.2f} Mach")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Mach to Kilometers/hour", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_mach = tk.Entry(self.root, **entry_style);
          entry_mach.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=mach_to_kmh).place(x=245, y=158)

          tk.Label(self.root, text="Kilometers/hour to Mach", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_kmh = tk.Entry(self.root, **entry_style);
          entry_kmh.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=kmh_to_mach).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)
      # Speed conversions

      # Energy conversions
      def j__ev(self):
          self.clean_window()
          self.root.title("Energy Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.energy_menu).place(x=15, y=8)

          tk.Label(self.root, text="Energy Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          J_TO_EV = 6.242e+18  # 1 Joule = ~6.242e+18 eV

          def j_to_ev():
              val = entry_j.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              ev = float(val) * J_TO_EV
              result_label.configure(text=f"{val} J = {ev:.2e} eV")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def ev_to_j():
              val = entry_ev.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              j = float(val) / J_TO_EV
              result_label.configure(text=f"{val} eV = {j:.6e} J")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Joules to Electronvolts", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_j = tk.Entry(self.root, **entry_style);
          entry_j.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=j_to_ev).place(x=245, y=158)

          tk.Label(self.root, text="Electronvolts to Joules", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_ev = tk.Entry(self.root, **entry_style);
          entry_ev.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=ev_to_j).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________

      def j__cal(self):
          self.clean_window()
          self.root.title("Energy Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.energy_menu).place(x=15, y=8)

          tk.Label(self.root, text="Energy Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          J_TO_CAL = 0.239006  # 1 Joule = 0.239006 calories

          def j_to_cal():
              val = entry_j.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              cal = float(val) * J_TO_CAL
              result_label.configure(text=f"{val} J = {cal:.4f} cal")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def cal_to_j():
              val = entry_cal.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              j = float(val) / J_TO_CAL
              result_label.configure(text=f"{val} cal = {j:.4f} J")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Joules to Calories", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_j = tk.Entry(self.root, **entry_style);
          entry_j.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=j_to_cal).place(x=245, y=158)

          tk.Label(self.root, text="Calories to Joules", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_cal = tk.Entry(self.root, **entry_style);
          entry_cal.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=cal_to_j).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________

      def j__kwh(self):
          self.clean_window()
          self.root.title("Energy Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.energy_menu).place(x=15, y=8)

          tk.Label(self.root, text="Energy Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          J_TO_KWH = 2.77778e-7  # 1 Joule = 2.77778 × 10⁻⁷ kWh

          def j_to_kwh():
              val = entry_j.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              kwh = float(val) * J_TO_KWH
              result_label.configure(text=f"{val} J = {kwh:.8f} kWh")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def kwh_to_j():
              val = entry_kwh.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              j = float(val) / J_TO_KWH
              result_label.configure(text=f"{val} kWh = {j:.2f} J")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Joules to Kilowatt-hours", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_j = tk.Entry(self.root, **entry_style);
          entry_j.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=j_to_kwh).place(x=245, y=158)

          tk.Label(self.root, text="Kilowatt-hours to Joules", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_kwh = tk.Entry(self.root, **entry_style);
          entry_kwh.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=kwh_to_j).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________

      def kwh__cal(self):
          self.clean_window()
          self.root.title("Energy Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.energy_menu).place(x=15, y=8)

          tk.Label(self.root, text="Energy Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          KWH_TO_CAL = 860420.65  # 1 kWh = ~860,420.65 calories

          def kwh_to_cal():
              val = entry_kwh.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              cal = float(val) * KWH_TO_CAL
              result_label.configure(text=f"{val} kWh = {cal:.2f} cal")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def cal_to_kwh():
              val = entry_cal.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              kwh = float(val) / KWH_TO_CAL
              result_label.configure(text=f"{val} cal = {kwh:.8f} kWh")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Kilowatt-hour to Calorie", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_kwh = tk.Entry(self.root, **entry_style);
          entry_kwh.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=kwh_to_cal).place(x=245, y=158)

          tk.Label(self.root, text="Calorie to Kilowatt-hour", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_cal = tk.Entry(self.root, **entry_style);
          entry_cal.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=cal_to_kwh).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________

      def j__wh(self):
          self.clean_window()
          self.root.title("Energy Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.energy_menu).place(x=15, y=8)

          tk.Label(self.root, text="Energy Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          J_TO_WH = 1 / 3600  # 1 Joule = 0.000277... Wh

          def j_to_wh():
              val = entry_j.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              wh = float(val) * J_TO_WH
              result_label.configure(text=f"{val} J = {wh:.6f} Wh")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def wh_to_j():
              val = entry_wh.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              j = float(val) * 3600
              result_label.configure(text=f"{val} Wh = {j:.2f} J")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          tk.Label(self.root, text="Joule to Watt-hour", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_j = tk.Entry(self.root, **entry_style);
          entry_j.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=j_to_wh).place(x=245, y=158)

          tk.Label(self.root, text="Watt-hour to Joule", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_wh = tk.Entry(self.root, **entry_style);
          entry_wh.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=wh_to_j).place(x=245, y=323)

          result_label = tk.Label(self.root, text="", **result_style)

      # ___________________________________________________________________________________

      def btu__j(self):
          self.clean_window()
          self.root.title("Energy Conversion")
          self.root.resizable(False, False)
          self.root.geometry("375x627")
          self.root.configure(background="#ffffff")

          back_img = Image.open("Unit Converter Images/menu_bar_img.png").resize((33, 33))
          self.back_img_button = ImageTk.PhotoImage(back_img)
          tk.Button(self.root, image=self.back_img_button,
                    bg='#ffffff', relief='flat', bd=0, command=self.energy_menu).place(x=15, y=8)

          tk.Label(self.root, text="Energy Conversion",
                   bg='#ffffff', fg='#323232', font=('Segoe UI', 20, 'bold')).place(x=50, y=2)

          # Styles
          label_style = {"font": ("Segoe UI", 12, "bold"), "bg": "#ffffff", "anchor": "w", "fg": "#353b48"}
          entry_style = {"font": ("Segoe UI", 12), "bg": "#f5f6fa", "fg": "#2d3436",
                         "relief": "flat", "bd": 0, "highlightthickness": 1,
                         "highlightbackground": "#dcdde1", "highlightcolor": "#00cec9"}
          result_style = {"font": ("Segoe UI", 13, "bold"), "bg": "#f5f6fa",
                          "fg": "#27ae60", "relief": "flat", "anchor": "center", "bd": 1}

          # Conversion constants
          BTU_TO_J = 1055.06  # 1 BTU = 1055.06 J

          # Functions
          def btu_to_j():
              val = entry_btu.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              j = float(val) * BTU_TO_J
              result_label.configure(text=f"{val} BTU = {j:.2f} J")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          def j_to_btu():
              val = entry_j.get()
              if not val or not val.replace('.', '', 1).isdigit():
                  messagebox.showwarning("Warning", "Enter valid number")
                  return
              btu = float(val) / BTU_TO_J
              result_label.configure(text=f"{val} J = {btu:.6f} BTU")
              result_label.pack(fill="x", padx=30, pady=(160, 0), ipady=12)

          # BTU → Joule
          tk.Label(self.root, text="BTU to Joule", **label_style).pack(fill="x", padx=(29, 0), pady=(80, 7))
          entry_btu = tk.Entry(self.root, **entry_style);
          entry_btu.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button1 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button1, bg='#ffffff', relief='flat', bd=0,
                    command=btu_to_j).place(x=245, y=158)

          # Joule → BTU
          tk.Label(self.root, text="Joule to BTU", **label_style).pack(fill="x", padx=(29, 0), pady=(90, 7))
          entry_j = tk.Entry(self.root, **entry_style);
          entry_j.pack(fill="x", padx=(30, 30), ipady=8)
          self.convert_img_button2 = ImageTk.PhotoImage(
              Image.open("Unit Converter Images/convert.png").resize((105, 55)))
          tk.Button(self.root, image=self.convert_img_button2, bg='#ffffff', relief='flat', bd=0,
                    command=j_to_btu).place(x=245, y=323)

          # Result Label
          result_label = tk.Label(self.root, text="", **result_style)
      # Energy conversions

      # Clean Screen
      def clean_window(self):
          for widget in self.root.winfo_children():
              widget.destroy()

root = tk.Tk()
run = UnitConverter(root)
root.mainloop()