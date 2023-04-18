from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.movex = 10
        self.movey = 10

    def move(self):
        coord_x = self.xcor() + self.movex
        coord_y = self.ycor() + self.movey
        self.goto(coord_x, coord_y)

    def bounce(self, xy):
        if xy == 0:
            self.movey = - self.movey
        else:
            self.movex = - self.movex

    def restart(self):
        self.movex = - self.movex
        self.goto(0, 0)