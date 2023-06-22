import colorgram
import random as rd
import turtle as t

#colect thhe collors from a image.
colors = colorgram.extract('image.jpg', 40)
colors_list = []

for i in colors:
    if i.rgb.r <= 200 or  i.rgb.g <= 200 or i.rgb.b <= 200:
        color = (i.rgb.r, i.rgb.g, i.rgb.b) 
        colors_list.append(color)

#Set the color mode to rgb and create my object.
t.colormode(255)
turtle = t.Turtle()
turtle.speed(9)
turtle.hideturtle()

#set my first point in thhe location that i want.
turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

#print the dots
for i in range(10):
    for j in range(10):
        turtle.pendown()
        turtle.dot(20, rd.choice(colors_list))
        turtle.penup()
        turtle.forward(50)

    #set the dot in the right point in thhe next line.
    turtle.setheading(90)
    turtle.forward(50)  
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)
    
screen = t.Screen()
screen.exitonclick()