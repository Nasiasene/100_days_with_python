import time
import turtle as t
from paddle_class import Paddle
from ball_class import Ball

screen = t.Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('Pong Gmae!')
screen.tracer(0)

player1 = Paddle(350)
player2 = Paddle(-350)

ball = Ball()

screen.listen()
screen.onkey(player1.up, 'Up')
screen.onkey(player1.down, 'Down')
screen.onkey(player2.up, 'w')
screen.onkey(player2.down, 's')

game_over = False
while game_over == False:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.xcor() == 800 or ball.xcor() == -800:
        ball.bounce(0)
    elif ball.ycor() == 600 or ball.ycor() == -600:
        ball.bounce(1)
screen.exitonclick()