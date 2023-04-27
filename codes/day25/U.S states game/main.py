import pandas as pd 
import turtle as t


df = pd.read_csv("50_states.csv")
states = df['state'].to_list()
coords_x = df['x'].to_list()
coords_y = df['y'].to_list()


image = "blank_states_img.gif"
screen = t.Screen()
screen.title("U.S States Game!")
screen.addshape(image)
t.shape(image)


points = 0
right_answers = []
game_over = False
while game_over == False:
    answer_state = screen.textinput(title=f'{points}/50 Guess the State', prompt="What's another state's name?").title()

    if answer_state in states and answer_state not in right_answers:
        right_answers.append(answer_state)
        points += 1
        index = states.index(answer_state)
        x_cord = coords_x[index]
        y_cord = coords_y[index]
        text = t.Turtle()
        text.hideturtle()
        text.penup()
        text.color('black')
        text.goto(x_cord, y_cord)
        text.write(f"{answer_state}")

    new_states = []
    if answer_state == 'Exit' or points == 50:
        screen.tracer(0)
        if points != 50:
            for i in states:
                
                if i not in right_answers:
                    new_states.append(i)
                    index = states.index(i)
                    x_cord = coords_x[index]
                    y_cord = coords_y[index]
                    text = t.Turtle()
                    text.hideturtle()
                    text.penup()
                    text.color('red')
                    text.goto(x_cord, y_cord)
                    text.write(f"{i}")
                    screen.update()
        print(new_states)
        game_over = True
    

t.mainloop