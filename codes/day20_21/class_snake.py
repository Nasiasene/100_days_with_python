import turtle as t
POSITIONS = [(0,0), (-20, 0), (-40, 0)]

class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]


    def create_snake(self):
        for position in POSITIONS:
            self.increase(position)

    def increase(self, position):
        shape = t.Turtle("square")
        shape.color('black', "green")
        shape.penup()
        shape.goto(position)
        self.snake.append(shape)
    
    def extend_snake(self):
        self.increase(self.snake[-1].position())

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


    