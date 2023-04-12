import turtle as t
import time
from class_snake import Snake

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game!")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

end_game = False
while end_game == False:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    









screen.exitonclick()