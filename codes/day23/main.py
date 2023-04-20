import time
import turtle as t
import random as rd
from class_player import Player
from class_car import CarManager
from class_scoreboard import Scoreboard


screen = t.Screen()
screen.setup(600, 600)
screen.title('Crossing Turtles!')
screen.tracer(0)


scoreboard = Scoreboard()

player = Player()
cars = []


screen.listen()
screen.onkey(player.up, 'Up')


game_over = False
increase = 0
while game_over == False:
    time.sleep(0.1)
    screen.update()
    counter = rd.randint(1, 6)

    if counter == 6:
        car = CarManager()
        cars.append(car)
    
    for car in cars:
        car.move(increase)
        if car.distance(player) < 20:
            game_over = True
            scoreboard.game_over()
            break
    
    if player.ycor() >= 300:
        scoreboard.increase()
        player.goto(0, -280)
        increase += 1


screen.exitonclick()