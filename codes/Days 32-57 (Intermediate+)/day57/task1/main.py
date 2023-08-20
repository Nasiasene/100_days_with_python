from flask import Flask, render_template
import requests as r
AGE_ENDPOINT = "https://api.agify.io"
GEN_ENDPOINT = "https://api.genderize.io/"   

app = Flask(__name__)

@app.route('/')
def homepage():
    return "<h1>Try an name!</h1>"

@app.route('/<name>')
def get_gen_age(name):
    response = r.get(url=AGE_ENDPOINT, params={'name': name})
    age = response.json()['age']
    response = r.get(url=GEN_ENDPOINT, params={'name': name})
    gen = response.json()['gender']
    return f"<h1>Hey {name.title()}!</h1> <h2>I think you are {gen}.</h2> <h3>And maybe {age} years old.</h3>"

if __name__ == "__main__":
    app.run(debug=True)

#using render_template, after the name of the archive, i can sand many variables i want (**kwargs) and will be sended to the html file.
#using the {{}} in the html file, i can use code.