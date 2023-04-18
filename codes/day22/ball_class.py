from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup() 

    def move(self):
        coord_x = self.xcor() + 10
        coord_y = self.ycor() + 10
        self.goto(coord_x, coord_y)

    def bounce(self, corner):
        if corner == 0:
            coord_x = self.xcor() + 10
            coord_y = self.ycor() - 10
        else:
            coord_x = self.xcor() - 10
            coord_y = self.ycor() + 10
        self.goto(coord_x, coord_y)
        
    
