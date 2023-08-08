from flask import Flask
import random as rd
app = Flask(__name__)
NUM = rd.randint(0, 9)

@app.route('/')
def open_page():
    return '<h1 style="font-weight: bold; font-size: 24px;">Guess a number between 0 and 9 !</h1><img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:num>')
def play(num):
    if num > NUM:
        return '<h1 style="font-weight: bold; font-size: 24px; color: red">Too high, try again!</h1><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    elif num < NUM:
        return '<h1 style="font-weight: bold; font-size: 24px; color: purple">Too low, try again!</h1><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return '<h1 style="font-weight: bold; font-size: 24px; color: blue">You found me!</h1><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'

if __name__ == "__main__":
    app.run(debug=True)