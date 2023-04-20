from turtle import Turtle

STARTING_POS = (0, -280)
MOVE_DIST = 10
FINISH_LINE = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(STARTING_POS)
