import turtle as t

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


    def create_snake(self):
        pos = [0,0]
        for i in range (3):
            shape = t.Turtle("square")
            shape.color("green")
            shape.penup()
            shape.goto(x = pos[0], y = pos[1])
            self.snake.append(shape)
            pos[0] -= 20

    
    def move(self):
        for i in range((len(self.snake) - 1), 0, -1):
            cord_x = self.snake[i - 1].xcor()
            cord_y = self.snake[i - 1].ycor()
            self.snake[i].goto(cord_x, cord_y)
        self.head.forward(20)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)


    