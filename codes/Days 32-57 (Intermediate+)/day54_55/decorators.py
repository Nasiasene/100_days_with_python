from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!\n'

def bold(func):
    def wrapper():
        str = func()
        return f"<b>{str}</b>"
    return wrapper
def emphasis(func):
    def wrapper():
        str = func()
        return f"<em>{str}</em>"
    return wrapper
def underline(func):
        def wrapper():
            str = func()
            return f"<ul>{str}</ul>"
        return wrapper

@app.route('/bye')
@underline
@emphasis
@bold
def name_():
    return 'bye!'


if __name__ == "__main__":
    app.run(debug=True)   



''''
class User:
    def __init__(self, name):
        self.name = name
        self.logged = False

def is_logged(func):
    def wrapper(*args):
        if args[0].logged == True:
            func()
    return wrapper       

@is_logged
def create_blog(user):   #user or any variable/key will be on args* or kwarg**
    return user.name
'''