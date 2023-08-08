from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!\nTEST'

#TERMINAL: Comand Prompt.
#>set FLASK_APP=hello.py
#>flask run

@app.route('/<test>/<int:num>') #<> create an variable.
def test(test, num):
    return f'<h1 style="text-align: center">{test} - {num}</h1><p>test paragraph</p><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRHp72GOIwOBB31vdr2pYMkyxlUhYPTAHQX6LEd7ur_zg&s" width=250>' #flask can return html code

if __name__ == "__main__":
    app.run(debug=True)

#will run the code with out using the prompt.
#when running the main file directly, the value of the __name__ variable is set to "__main__".