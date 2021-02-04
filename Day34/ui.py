from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")
TRUE_IMG = "images/true.png"
FALSE_IMG = "images/false.png"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            100,
            text="STARTING TEXT",
            font=FONT,
            width=300)
        self.canvas.grid(column=1, row=2, columnspan=2, pady=30)

        # true button
        self.true_image = PhotoImage(file=TRUE_IMG)
        self.true_button = Button(
            image=self.true_image,
            highlightthickness=0,
            borderwidth=0,
            command=self.user_true)
        self.true_button.grid(column=2, row=3)

        # False button
        self.false_image = PhotoImage(file=FALSE_IMG)
        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            borderwidth=0,
            command=self.user_false)
        self.false_button.grid(column=1, row=3)

        # Score label

        self.score_label = Label(text=f"Score: {0}", bg=THEME_COLOR, fg="white", font=FONT)
        self.score_label.grid(column=2, row=1)

        self.get_question()

        self.window.mainloop()

    def get_question(self):



        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text, fill = "black")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz", fill = "black")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")


    def user_true(self):
        is_right = self.quiz.check_answer("True")

        self.give_feedback(is_right)

    def user_false(self):
        is_right = self.quiz.check_answer("False")

        self.give_feedback(is_right)

    def give_feedback(self, is_right):

        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.question_text, fill="white")
        else:
            self.canvas.config(bg="red")
            self.canvas.itemconfig(self.question_text, fill="white")
        self.window.after(1000, self.get_question)
