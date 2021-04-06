from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import os

class LoginForm(FlaskForm):
    email = StringField(label='Email')
    password = PasswordField(label='Password')
    submit = SubmitField(label="Log In")


app = Flask(__name__)

app.secret_key = os.environ.get("SECRETKEY")


@app.route('/submit', methods=('GET', 'POST'))
def submit():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('success.html', form=form)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=('GET', 'POST'))
def login():
    login_form = LoginForm()
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
