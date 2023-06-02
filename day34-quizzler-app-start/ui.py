from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ["Arial", 20, "italic"]


class QuizInterface:

    def __int__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.tile("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)
        self.right_img = PhotoImage("./images/true.png")
        self.wrong_img = PhotoImage("./images/false.png")
        self.right_button = Button(image=self.right_img, highlightthickness=0, compound=self.check_right)
        self.wrong_button = Button(image=self.wrong_img, highlightthickness=0, compound=self.check_wrong)
        self.right_button.grid(row=2, column=1)
        self.wrong_button.grid(row=2, column=0)
        self.question_text = self.canvas.create_text(150, 125, "question", fill=THEME_COLOR, font=FONT, width=280)
        self.next_question()

        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quizzlor.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def check_right(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def check_wrong(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.next_question)
