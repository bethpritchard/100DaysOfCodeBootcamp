from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired
import os
import requests

API_URL = "https://api.themoviedb.org/3/search/movie?"
API_KEY = os.environ.get("API_KEY")
IMG_URL = "https://image.tmdb.org/t/p/w500"
print(API_KEY)

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")
Bootstrap(app)

# CREATE DATABASE

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///top-movies.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, unique=False, nullable=False)
    description = db.Column(db.String(500), unique=False, nullable=False)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), unique=False, nullable=False)

db.create_all()

# CREATE FORM

class EditRatingForm(FlaskForm):
    rating = StringField(label="Rating", validators=[DataRequired()])
    review = StringField(label="Your Review")
    submit = SubmitField("Done")


class AddMovieForm(FlaskForm):
    title = StringField(label="Movie title", validators=[DataRequired()])
    submit = SubmitField("Add movie")


#
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
#
#
# db.session.add(new_movie)
# db.session.commit()

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = EditRatingForm()
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    print(movie)
    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", movie=movie, form=form)


@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()
    if form.validate_on_submit():
        movie_title = form.title.data
        print(movie_title)
        params = {
            "api_key": API_KEY,
            "query": movie_title
        }
        response = requests.get(API_URL, params=params)
        data = response.json()["results"]
        print(data)
        if len(data) == 0:
            return render_template("add.html", form=form, valid=False)
        else:
            return render_template("select.html", all_movies=data)

    return render_template("add.html", form=form, valid=True)


@app.route("/find", methods=["GET", "POST"])
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        params = {
            "api_key": API_KEY,
        }
        response = requests.get(movie_url, params=params)
        data = response.json()

        new_movie = Movie(title=data["title"],
                          year=data["release_date"][:4],
                          description=data["overview"],
                          img_url=IMG_URL + data["poster_path"])
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for('rate_movie', id=new_movie.id))




if __name__ == '__main__':
    app.run(debug=True)
