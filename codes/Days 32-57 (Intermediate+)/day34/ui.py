import tkinter as t

THEME_COLOR = "#375362"


class QuizInterFace():

    def __init__(self, quiz):
        self.quiz = quiz


        self.window = t.Tk()
        self.window.title('Quizzler App!')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)


        self.score_label = t.Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)


        self.canvas =  t.Canvas(width=300, height=250, bg='white')
        self.canvas_text = self.canvas.create_text(150, 125, text='TESTE', fill=THEME_COLOR, font=('Arial', 20, 'italic'), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=30)


        right_img = t.PhotoImage(file='true.png')
        self.right_button = t.Button(image=right_img, highlightthickness=0, command=self.right_button)
        self.right_button.grid(column=0, row=2)
        wrong_img = t.PhotoImage(file='false.png')
        self.wrong_button = t.Button(image = wrong_img, highlightthickness=0, command= self.wrong_button)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_label.config(text=f'Score: {self.quiz.score}')
            self.quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=self.quiz_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text='End of the quiz!')
            self.right_button.config(state= 'disable')
            self.wrong_button.config(state= 'disable')

    def right_button(self):
        self.check(self.quiz.check_answer('True'))

    def wrong_button(self):
        self.check(self.quiz.check_answer('False'))

    def check(self, right_wrong):
        if right_wrong:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)