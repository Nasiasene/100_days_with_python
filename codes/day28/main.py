import tkinter as t
import math

PINK = "#e2979c"
WINE = '#750101'
RED = "#e7305b"
GREEN = "#0fd104"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
marker =''
timer = None


def reset():
    global marker, rep

    window.after_cancel(timer)
    timer_label.config(text = 'Timer')
    canvas.itemconfig(canvas_text, text = "00:00")
    marker = ''
    rep = 0



def start_timer():
    global rep
    global marker

    if rep % 2 == 0:
        if rep % 8 == 0 and rep != 0:
            count_down(LONG_BREAK_MIN * 60)
            timer_label.config(text = 'Break...')
        else:
            count_down(WORK_MIN * 60)
            timer_label.config(text = 'Work!')


    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text = 'Break...')
        marker += '✓'
        check_mark_label.config(text = f'{marker}')
    rep += 1


def count_down(count):
    global timer

    minuts = math.floor(count / 60)
    seconds = count % 60
    if minuts < 10:
        minuts = f'0{minuts}'

    if seconds < 10:
        seconds = f'0{seconds}'

    canvas.itemconfig(canvas_text, text = f'{minuts}:{seconds}')

    if count > 0:
        timer = window.after(1000, count_down, count - 1)



window = t.Tk()
window.title("Pomodoro App")
window.config(background=RED)
window.config(padx=20, pady=20)


timer_label = t.Label(text = "Timer", font = (FONT_NAME, 30, 'bold'), fg= GREEN, bg= RED)
check_mark_label = t.Label(font= (FONT_NAME, 15, 'bold'), fg= GREEN, bg= RED)
timer_label.grid(column=1, row= 0)
check_mark_label.grid(column=1, row=3)


canvas = t.Canvas(width=200, height=224)
canvas.config(bg=RED, highlightthickness=0)
tomato_png = t.PhotoImage(file = 'tomato.png')
canvas.create_image(103, 112, image = tomato_png)
canvas_text = canvas.create_text(103, 125, text='00:00', fill=WINE, font = (FONT_NAME, 20, 'bold'))
canvas.grid(column=1, row=1)


start_button = t.Button(text='Start', width=10, bg=RED, fg=YELLOW, font= (FONT_NAME, 11, 'bold'), command = start_timer)
reset_button = t.Button(text="Reset", width=10, bg=RED, fg=YELLOW, font= (FONT_NAME, 11, 'bold'), command = reset)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)


window.mainloop()