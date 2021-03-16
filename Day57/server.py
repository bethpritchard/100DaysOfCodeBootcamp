import datetime
import random
import requests

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    random_number = random.randint(1, 100)
    year = datetime.date.today().year

    return render_template("index.html", num=random_number, year=year)


@app.route('/guess/<name>')
def guess(name):
    year = datetime.date.today().year

    params = {"name": name.title()}
    age_response = requests.get(url="https://api.agify.io/", params=params)
    age_dict = age_response.json()
    age = age_dict["age"]

    gender_response = requests.get(url="https://api.genderize.io/", params=params)
    gender_dict = gender_response.json()
    gender = gender_dict["gender"]

    return render_template("index.html", year=year, age=age, name=name, gender=gender)

if __name__ == '__main__':
    app.run(debug=True)
