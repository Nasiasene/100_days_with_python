from turtle import Turtle

STARTING_POS = (0, -280)
MOVE_DIST = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POS)
        self.setheading(90)
        
    def up(self):
        self.forward(MOVE_DIST)
