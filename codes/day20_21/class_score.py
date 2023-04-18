from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(0, 265)
        self.write(arg = f"Score: {self.score}", align = 'center', font = ('Times', 20, 'normal'))

    def increase(self):
        self.score += 1
        self.clear()
        self.write(arg = f"Score: {self.score}", align = 'center', font = ('Times', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("Game Over!", align = 'center', font = ('Times', 30, 'normal'))