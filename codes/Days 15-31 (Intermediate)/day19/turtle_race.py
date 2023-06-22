import turtle as t
import random as rd

screen = t.Screen()
screen.setup(500, 400)
guess = screen.textinput(title= 'Who will win?', prompt = 'Which turtle will win the race? \nDonatello, Leonardo, Michelangelo or Raphael? : ').lower()

colors = ['orange', 'purple', 'blue', 'red']
names = ['Michelangelo', 'Donatelo', 'Leonardo', 'Raphael']
turtles = []

count = 0 
for i in names:
    if guess == i.lower():
        guess = count
    count += 1

y = -50
for i in range (len(colors)):
    new_turtle = t.Turtle('turtle')
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x = -230, y = y)
    y += 40
    turtles.append(new_turtle)

still_run = True
while still_run:
    count = 0
    for i in turtles:
        i.forward(rd.randint(0, 10))
        if i.xcor() > 230:
            still_run = False
            turtle_winner = count
            break
        count += 1

count = 0
for i in names:
    if count == turtle_winner:
        print(f'{i} wins!')
    count +=1

if guess == turtle_winner:
    print("You're right!")
else:
    print("You're wrong")
    
screen.exitonclick()