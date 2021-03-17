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

    params = {"name": name}
    age_response = requests.get(url="https://api.agify.io/", params=params)
    age_dict = age_response.json()
    age = age_dict["age"]

    gender_response = requests.get(url="https://api.genderize.io/", params=params)
    gender_dict = gender_response.json()
    gender = gender_dict["gender"]

    return render_template("guess.html", year=year, age=age, name=name, gender=gender)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
