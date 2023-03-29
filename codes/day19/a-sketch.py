import turtle as t

turtle = t.Turtle()
screen = t.Screen()
turtle.shapesize(1.3)
turtle.pensize(2)

def move_forward():
    turtle.forward(20)

def turn_right():
    turtle.right(10)

def turn_left():
    turtle.left(10)

def move_backward():
    turtle.back(20)

def clear():
    turtle.home()
    turtle.clear()

def turn_down():
    turtle.down()

def turn_up():
    turtle.up()

screen.listen() #wait an enter by the user.
screen.onkey(move_forward, 'Up') #when i pass a function as a parameter i dont need to use: ()
screen.onkey(turn_right, 'Right')
screen.onkey(turn_left, 'Left')
screen.onkey(move_backward, 'Down')
screen.onkey(clear, 'c')
screen.onkey(turn_down, 'w')
screen.onkey(turn_up, 'u')

screen.exitonclick()