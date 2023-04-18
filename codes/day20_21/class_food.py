from turtle import Turtle
import random as rd

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("black", 'red')
        self.speed('fastest')
        x = rd.randint(-285, 285)
        y = rd.randint(-285, 285)
        self.goto(x, y)
        self.new_loc()

    def new_loc(self):
        x = rd.randint(-285, 285)
        y = rd.randint(-285, 285)
        self.goto(x, y)