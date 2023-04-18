from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, coord_x = 0):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(coord_x, 0)

    def up(self):
        coord_y = self.ycor() + 20
        self.goto(self.xcor(), coord_y)

    def down(self):
        coord_y = self.ycor() - 20
        self.goto(self.xcor(), coord_y)