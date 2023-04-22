import turtle as t
import time
from class_snake import Snake
from class_food import Food
from class_score import Scoreboard


screen = t.Screen()
screen.setup(600, 600)
screen.colormode(255)
screen.bgcolor(172, 176, 116)
screen.title("Snake Game!")
screen.tracer(0)


food = Food()
snake = Snake()
score = Scoreboard()


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')


while True:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    if snake.head.distance(food) < 18:
        food.new_loc()
        snake.extend_snake()
        score.increase()
    
    if snake.head.xcor() > 285 or snake.head.xcor() < -290 or snake.head.ycor() > 285 or snake.head.ycor() < -290:
        score.reset()
        snake.reset()

    for seg in snake.snake[1:]:
        if snake.head.distance(seg) < 10:
            score.reset()
            snake.reset()


screen.exitonclick()