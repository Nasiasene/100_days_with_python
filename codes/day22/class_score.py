from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score1 = 0
        self.score2 = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(0, 200)
        self.write(arg = f"{self.score1}     {self.score2}", align = 'center', font = ('Arial', 50, 'normal'))

    def increase(self, player):
        if player == 1:
            self.score1 += 1
        else:
            self.score2 += 1
        self.clear()
        self.write(arg = f"{self.score1}     {self.score2}", align = 'center', font = ('Arial', 50, 'normal'))