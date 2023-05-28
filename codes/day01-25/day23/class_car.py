import random as rd
from turtle import Turtle

COLORS = ['red', 'orange', 'black', 'yellow', 'green', 'blue', 'purple', 'cyan', 'lightgreen', 'turquoise', 'skyblue']
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color(rd.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.setheading(180)
        self.goto(x = 312, y = rd.randint(-250, 250))

    def move(self, cnst):
        self.forward(STARTING_MOVE_DISTANCE + (MOVE_INCREMENT * cnst))
   
