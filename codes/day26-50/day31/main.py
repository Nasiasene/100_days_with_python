import pandas as pd
import tkinter as t
import random as rd
BACKGROUND_COLOR = "#B1DDC6"

change_df = pd.read_csv("data/to_learn.csv")
df = pd.read_csv("data/english_words.csv")
origin = df.columns[0]
translate = df.columns[1]
dict = change_df.to_dict(orient="records")
card = {}

def new_card():
    global card, timer
    window.after_cancel(timer)
    card = rd.choice(dict)
    canvas.itemconfig(canvas_image, image=front_card)
    canvas.itemconfig(canvas_word, text = card[origin].title(), fill="black")
    canvas.itemconfig(canvas_language, text=origin, fill="black")
    timer = window.after(3000, func=change_card)

def change_card():
    canvas.itemconfig(canvas_language, text=translate, fill="white")
    canvas.itemconfig(canvas_word, text=card[translate].title(), fill="white")
    canvas.itemconfig(canvas_image, image=back_card)

def known():
    dict.remove(card)
    data_to_learn = pd.DataFrame(dict)
    data_to_learn.to_csv("data/to_learn.csv", index=False)
    new_card()


window = t.Tk()
window.title("Flash Card App!")
window.config(bg=BACKGROUND_COLOR, padx=40, pady=20)
timer = window.after(4500, func=change_card)


canvas = t.Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
front_card = t.PhotoImage(file="images/card_front.png")
back_card = t.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image= front_card)
canvas_language = canvas.create_text(400, 150, font=("Arial", 40, "italic"), text=df.columns[0])
canvas_word = canvas.create_text(400, 256, font=("Arial", 60, "bold"), text='')
canvas.grid(column=0, row=0, columnspan=2)


right_img = t.PhotoImage(file="images/right.png")
right_button = t.Button(image=right_img, highlightthickness=0, command=known)
right_button.grid(column=1, row=1)
wrong_img = t.PhotoImage(file="images/wrong.png")
wrong_button = t.Button(image=wrong_img, highlightthickness=0, command=new_card)
wrong_button.grid(column=0, row=1)


new_card()


window.mainloop()