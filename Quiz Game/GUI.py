import tkinter as tk
from PIL import Image, ImageTk

quiz = [
    {"q": "Capital of France?", "options": ["Paris", "Rome", "Berlin", "Madrid"], "answer": "Paris"},
    {"q": "2+2?", "options": ["2", "3", "4", "5"], "answer": "4"},
    {"q": "Largest planet in our solar system?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Jupiter"},
    {"q": "5 * 6 = ?", "options": ["11", "30", "56", "26"], "answer": "30"},
    {"q": "Which gas do plants absorb?", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Helium"], "answer": "Carbon Dioxide"},
    {"q": "Fastest land animal?", "options": ["Tiger", "Cheetah", "Horse", "Lion"], "answer": "Cheetah"},
    {"q": "H2O is chemical formula of?", "options": ["Oxygen", "Water", "Hydrogen", "Salt"], "answer": "Water"},
    {"q": "Square root of 81?", "options": ["9", "8", "7", "6"], "answer": "9"},
    {"q": "Which continent is Egypt in?", "options": ["Asia", "Europe", "Africa", "South America"], "answer": "Africa"},
    {"q": "National language of Pakistan?", "options": ["Urdu", "Punjabi", "Sindhi", "English"], "answer": "Urdu"}
]

class QuizApp():
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x570")
        self.root.title("Quiz Game")
        self.root.configure(background="#ffffff")
        self.root.resizable(False, False)

        self.q_index = 0
        self.score = 0
        self.show_home_page()

    def show_home_page(self):
        self.clear_screen()

        bg = Image.open("bg_img.jpg")
        bg = bg.resize((380, 225))
        self.bg_img = ImageTk.PhotoImage(bg)

        bg_label = tk.Label(self.root, image=self.bg_img, bg="#ffffff")
        bg_label.pack(pady=(35, 0))

        button_start = tk.Button(self.root, text="START",
                                 width=9, height=1, bd=1, font=("Calibri", 18, "bold"),
                                 bg="#feb100", fg="#001e40", relief="flat", activebackground="green",
                                 activeforeground="white", command=self.start_quiz)
        button_start.pack(pady=(140, 0))

    def start_quiz(self):
        self.q_index = 0
        self.score = 0
        self.clear_screen()
        self.load_question()

    def load_question(self):
        if self.q_index < len(quiz):
            q_data = quiz[self.q_index]
            self.root.configure(background="#ffffff")

            bg = Image.open("bg_img.jpg")
            bg = bg.resize((375, 210))
            self.bg_img = ImageTk.PhotoImage(bg)

            photo_label = tk.Label(self.root, image=self.bg_img, bg="#ffffff")
            photo_label.pack(pady=(0, 0))

            content_frame = tk.Frame(self.root, bg="white", bd=1, relief="flat",
                                     highlightbackground="#ffffff", highlightthickness=1)
            content_frame.pack(fill="both", expand=True, padx=15, pady=(2, 8))

            self.question_label = tk.Label(
                content_frame,
                text=f"Q{self.q_index + 1}. {q_data['q']}",
                font=("Arial", 19, "bold"),
                bg="white",
                fg="#001e40",
                wraplength=340,
                justify="center",
            )
            self.question_label.pack(pady=(20, 10))

            self.var = tk.StringVar()
            self.buttons = []
            for i, option in enumerate(q_data['options']):
                btn = tk.Radiobutton(
                    content_frame,
                    text=option,
                    variable=self.var,
                    value=option,
                    font=("Arial", 11, "bold"),
                    bg="#fecd52",
                    fg="#001e40",
                    activebackground="#3498db",
                    activeforeground="white",
                    indicatoron=0,
                    width=30,
                    pady=10,
                    relief="flat",
                    bd=0,
                    highlightthickness=0,
                    selectcolor="#d5f5e3",
                    command=lambda opt=option: self.check_answer(opt)  # 👈 direct agla question
                )
                btn.pack(pady=6)
                self.buttons.append(btn)
        else:
            self.show_result()

    def check_answer(self, selected):
        q_data = quiz[self.q_index]

        if selected == q_data["answer"]:
            self.score += 1
        self.q_index += 1
        self.clear_screen()
        self.load_question()

    def show_result(self):
        self.clear_screen()
        result_text = f"Quiz Completed!\n\nYour Score: {self.score}/{len(quiz)}"
        label = tk.Label(self.root, text=result_text, font=("Arial", 18, "bold"),
                         bg="white", fg="#001e40", justify="center")
        label.pack(pady=100)

        restart_btn = tk.Button(self.root, text="Play Again",
                                width=9, height=1, bd=1, font=("Comic Sans MS", 17, "bold"),
                                bg="green", fg="white", relief="flat", activebackground="#3498db",
                                activeforeground="white",
                                command=self.start_quiz)
        restart_btn.pack(pady=20)

        exit_btn = tk.Button(self.root, text="Exit",
                             width=9, height=1, bd=1, font=("Comic Sans MS", 13, "bold"),

                             bg="#e74c3c", fg="white", relief="flat", activebackground="red",
                             activeforeground="white",
                             command=self.root.destroy)
        exit_btn.pack()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

root = tk.Tk()
app = QuizApp(root)
root.mainloop()