import time
import turtle as t
from class_paddle import Paddle
from class_ball import Ball
from class_score import Score


screen = t.Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong Game!')
screen.tracer(0)


player1 = Paddle(350)
player2 = Paddle(-350)


ball = Ball()


score_board = Score()

line = t.Turtle()
line.right(90)
line.goto(0, 300)
line.color('white')
for i in range(20):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)


screen.listen()
screen.onkey(player1.up, 'Up')
screen.onkey(player1.down, 'Down')
screen.onkey(player2.up, 'w')
screen.onkey(player2.down, 's')


game_over = False
speed = 0.1
while game_over == False:

    time.sleep(speed)

    screen.update()
    ball.move()
    if ball.ycor() == 280 or ball.ycor() == -280:
        ball.bounce(0)
        speed *= 0.9

    if (ball.distance(player1) < 50 and ball.xcor() > 320) or (ball.distance(player2) < 50 and ball.xcor() < -320):
        ball.bounce(1)
        speed *= 0.9

    if ball.xcor() > 380:
        ball.restart()
        score_board.increase(1)
        speed = 0.1

    if ball.xcor() < -380:
        ball.restart()
        score_board.increase(2)
        speed = 0.1


screen.exitonclick()