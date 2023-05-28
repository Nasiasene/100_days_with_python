from turtle import Turtle

FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.hideturtle()
        self.penup()
        self.color('black')
        self.goto(x = -280, y = 255)
        self.write(f"Level: {self.player_score}", font = FONT)

    def increase(self):
        self.clear()
        self.player_score += 1
        self.write(f"Level: {self.player_score}", font = FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align = 'center', font = FONT)