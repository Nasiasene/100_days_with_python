import time
import turtle as t
from class_player import Player

screen = t.Screen()
screen.setup(600, 600)
screen.tracer(0)


player = Player()



game_over = False
while game_over == False:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()