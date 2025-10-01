import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import socket
import threading
from datetime import datetime


# ------------------ Chat App ------------------
class ChatApp:
    def __init__(self, root):
        self.root = root
        self.splash_page()


    # ---------- UI Setup ----------
    def splash_page(self):
        self.clean_window()
        self.root.geometry("330x625+530+50")
        self.root.title("Nex Chat")
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)

        img_1 = Image.open("Chat App Images/splash.png")
        img_1 = img_1.resize((245, 204))
        self.splash_img = ImageTk.PhotoImage(img_1)

        label = tk.Label(self.root, image=self.splash_img, bg="#ffffff")
        label.pack(pady=(200, 0))

        self.root.after(1200, self.dashboard)


    def dashboard(self):
        self.clean_window()
        self.root.geometry("330x625+530+50")
        self.root.title("Nex Chat")
        self.root.config(bg="#ffffff")
        self.root.resizable(False, False)

        # ----- Top Bar -----
        back_img = Image.open("Chat App Images/back.png")
        back_img = back_img.resize((45, 45))
        self.back_img_button = ImageTk.PhotoImage(back_img)

        button_back = tk.Button(self.root, image=self.back_img_button,
                                bg='#ffffff', relief='flat', bd=0, command="")
        button_back.place(x=15, y=15)

        dots_img = Image.open("Chat App Images/3 dots.png")
        dots_img = dots_img.resize((45, 45))
        self.dots_img_button = ImageTk.PhotoImage(dots_img)

        button_3_dots = tk.Button(self.root, image=self.dots_img_button,
                                  bg='#ffffff', relief='flat', bd=0, command="")
        button_3_dots.place(x=268, y=15)

        user_img = Image.open("Chat App Images/user.png")
        user_img = user_img.resize((50, 50))
        self.user_img_button = ImageTk.PhotoImage(user_img)

        label = tk.Label(self.root, image=self.user_img_button, bg="#ffffff")
        label.place(x=138, y=5)

        divider = tk.Frame(self.root, bg="#e5e5e5", height=1, width=400)
        divider.place(x=0, y=100)

        # ----- Scrollable Chat Area -----
        self.chat_canvas = tk.Canvas(self.root, bg="#ffffff", highlightthickness=0)
        self.chat_canvas.place(x=0, y=107, width=330, height=430)

        self.chat_area = tk.Frame(self.chat_canvas, bg="#ffffff")
        self.chat_window = self.chat_canvas.create_window(
            (0, 0), window=self.chat_area, anchor="nw")
        self.chat_canvas.itemconfig(self.chat_window, width=330)

        def update_scroll_region(event=None):
            self.chat_canvas.configure(scrollregion=self.chat_canvas.bbox("all"))

        self.chat_area.bind("<Configure>", update_scroll_region)

        def on_mouse_wheel(event):
            self.chat_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        self.chat_canvas.bind_all("<MouseWheel>", on_mouse_wheel)

        # ----- Networking -----
        self.sock = self.start_as_client()
        if not self.sock:
            self.sock = self.start_as_server()

        if self.sock:
            threading.Thread(target=self.receive_messages, args=(self.sock,), daemon=True).start()

        # ----- Entry Field -----
        entry_style = {
            "font": ("Segoe UI", 12),
            "bg": "#ffffff",
            "fg": "#323232",
            "insertbackground": "#00cec9",
            "relief": "flat",
            "bd": 0,
            "highlightthickness": 1,
            "highlightbackground": "#dcdcdc",
            "highlightcolor": "#00cec9",
        }
        placeholder_text = "Message..."

        def add_placeholder(event=None):
            if self.entry.get() == "":
                self.entry.insert(0, placeholder_text)
                self.entry.config(fg="#b0b0b0")

        def remove_placeholder(event=None):
            if self.entry.get() == placeholder_text:
                self.entry.delete(0, "end")
                self.entry.config(fg="#323232")

        self.entry = tk.Entry(self.root, **entry_style)
        self.entry.place(x=29, y=550, width=270, height=46)

        self.entry.bind("<Return>", lambda event: self.send_msg())
        self.entry.bind("<FocusIn>", remove_placeholder)
        self.entry.bind("<FocusOut>", add_placeholder)

        add_placeholder()

        send_img = Image.open("Chat App Images/send.png")
        send_img = send_img.resize((30, 30))
        self.send_img_button = ImageTk.PhotoImage(send_img)

        button_send = tk.Button(self.root, image=self.send_img_button,
                                bg='#ffffff', relief='flat', bd=0, command=self.send_msg)
        button_send.place(x=257, y=558)


    # ---------- Chat Display ----------
    def display_message(self, text, side):
        if side == "right":
            bg_color = "#dcf8c6"
            padx = (60, 10)
        else:
            bg_color = "#ebf2fd"
            padx = (10, 60)

        bubble = tk.Frame(self.chat_area, bg=bg_color, padx=10, pady=5)

        if side == "right":
            bubble.pack(anchor="e", padx=padx, pady=5)
        else:
            bubble.pack(anchor="w", padx=padx, pady=5)

        tk.Label(
            bubble, text=text, bg=bg_color, fg="#000000",
            font=("Segoe UI", 11), wraplength=200, justify="left"
        ).pack()

        date_time = datetime.now().strftime("%I:%M %p")
        tk.Label(
            bubble, text=date_time, bg=bg_color,
            fg="#555555", font=("Segoe UI", 8)
        ).pack(anchor="e", pady=(2, 0))

        self.chat_canvas.update_idletasks()
        self.chat_canvas.yview_moveto(1.0)


    # ---------- Sending & Receiving ----------
    def send_msg(self):
        message = self.entry.get()
        if not message.strip():
            messagebox.showwarning("Warning", "Please enter a message.")
            return
        self.entry.delete(0, "end")

        self.display_message(message, side="right")
        target = self.sock if self.sock else self.conn
        if target:
            target.sendall(message.encode("utf-8"))


    def receive_messages(self, sock):
        while True:
            try:
                data = sock.recv(1024)
                if not data:
                    break
                data = data.decode("utf-8")
                self.root.after(0, lambda: self.display_message(data, side="left"))
            except (ConnectionResetError, ConnectionAbortedError, OSError):
                messagebox.showinfo("Session Ended", "User went offline.")
                return


    # ---------- Server / Client ----------
    def start_as_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(('localhost', 54356))
        self.server_socket.listen(2)

        self.show_online_user("Faaiz Gul")

        self.wait_label = tk.Label(self.chat_canvas, text="Waiting for Connection.....",
                                   font=("Segoe UI", 11), bg="#ffffff", fg="#777777")
        self.wait_label.place(x=81, y=200)

        threading.Thread(target=self.wait_for_client, daemon=True).start()


    def wait_for_client(self):
        conn, addr = self.server_socket.accept()
        self.conn = conn
        threading.Thread(target=self.receive_messages, args=(self.conn,), daemon=True).start()
        self.root.after(0, self.remove_wait_label)


    def start_as_client(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect(('localhost', 54356))
            self.conn = client_socket
            self.show_online_user("Inam Adil")

            if client_socket:
                self.connected_label = tk.Label(self.chat_canvas, text="Connected with Faaiz Gul",
                                                font=("Segoe UI", 11), bg="#ffffff", fg="#777777")
                self.connected_label.place(x=79, y=200)
                self.root.after(5000, self.connected_label.destroy)

            return client_socket
        except (ConnectionRefusedError, OSError):
            return None


    # ---------- Helpers ----------
    def remove_wait_label(self):
        if hasattr(self, "wait_label"):
            self.wait_label.destroy()
            self.connected_label = tk.Label(self.chat_canvas, text="Connected with Inam Adil",
                                            font=("Segoe UI", 11), bg="#ffffff", fg="#777777")
            self.connected_label.place(x=79, y=200)
            self.root.after(5000, self.connected_label.destroy)


    def show_online_user(self, user_name):
        online_img = Image.open("Chat App Images/online color.png")
        online_img = online_img.resize((12, 12))
        self.online_img_button = ImageTk.PhotoImage(online_img)

        tk.Label(self.root, image=self.online_img_button, bg="#ffffff").place(x=119, y=64)
        tk.Label(self.root, text=user_name, font=("Segoe UI", 11, "bold"),
                 bg="#ffffff", fg="#323232").place(x=135, y=58)


    def clean_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# ---------- Main Loop ----------
root = tk.Tk()
run = ChatApp(root)
root.mainloop()
