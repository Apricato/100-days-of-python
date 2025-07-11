from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)



        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 125, 
            text="placeholder", 
            width=  280, 
            fill=THEME_COLOR, 
            font=("Arial", 20, "italic"), 
            wid=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_image = PhotoImage(file=r"Day 34\quizzler-app-start\images\true.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        
        false_image = PhotoImage(file=r"Day 34\quizzler-app-start\images\false.png")
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        self.get_next(get_next_question())

        self.window.mainloop()

def get_next_question(self):
    self.canvas.config(bg="white")
    self.score_label.config(text=f"Score: {self.quiz.score}")
    q_text = self.quiz.next_question()
    self.canvas.itemconfig(self.question_text, text= q_text)

