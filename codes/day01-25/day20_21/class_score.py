from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("/Users/davit/Documents/100days_python.py/100_days_with_python/codes/day20_21/data.txt") as file:
            self.high_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(0, 265)
        self.write(arg = f"Score: {self.score} High Score: {self.high_score}", align = 'center', font = ('Times', 20, 'normal'))

    def increase(self, att = 0):
        if att == 0:
            self.score += 1
        self.clear()
        self.write(arg = f"Score: {self.score} High Score: {self.high_score}", align = 'center', font = ('Times', 20, 'normal'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/davit/Documents/100days_python.py/100_days_with_python/codes/day20_21/data.txt", mode = 'w') as file:
                file.write(f"{self.score}")
        self.score = 0
        self.increase(1)

'''
    def game_over(self):
        self.goto(0, 0)
        self.color('red')
        self.write("Game Over!", align = 'center', font = ('Times', 30, 'normal'))
'''