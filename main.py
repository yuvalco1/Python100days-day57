import random
import time
import requests

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    data = response.json()
    return render_template("index.html",posts=data)


@app.route('/old')
def homeold():
    random_number = random.randint(1, 100)
    year = time.strftime("%Y")
    return render_template('indexold.html', random_number=random_number, cyear=year)

@app.route('/guess/<string:name>')
def guess(name):
    name = name.title()
    response = requests.get(f'https://api.genderize.io/?name={name}&country_id=IL')
    data = response.json()
    gender = data['gender']
    response2 = requests.get(f'https://api.agify.io?name={name}&country_id=IL')
    data2 = response2.json()
    age = data2['age']
    return render_template('guess.html', name=name,age=age,gender=gender)

@app.route('/blog')
def blog():
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    data = response.json()
    return render_template('blog.html', posts=data)

@app.route('/post/<int:num>')
def post(num):
    response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
    data = response.json()
    return render_template('post.html', posts=data, num=num)

if __name__ == "__main__":
    app.run(debug=True)


