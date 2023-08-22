from flask import Flask, render_template
import requests as r
URL= "https://api.npoint.io/c790b4d5cab58020d391"

app = Flask(__name__)
response = r.get(url=URL)
data = response.json()

@app.route('/')
def home():
    return render_template("index.html", data=data, len_data=len(data))

@app.route('/post/<int:index>')
def post(index):
    return render_template("post.html", data=data[index-1])

if __name__ == "__main__":
    app.run(debug=True)