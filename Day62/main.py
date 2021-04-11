from flask import Flask, render_template, redirect,url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateTimeField
from wtforms.validators import DataRequired, URL
import os
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRETKEY")

Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe location', validators=[DataRequired(), URL()])
    opening_time = StringField('Opening Time', validators=[DataRequired()])
    closing_time = StringField('Closing Time', validators=[DataRequired()])
    coffee_rating = SelectField("Coffee rating", validators=[DataRequired()],
                                choices=[i * "☕" for i in range(1, 5)])
    wifi_rating = SelectField("Wifi strength rating", validators=[DataRequired()],
                              choices=[i * "📡" for i in range(1, 5)])
    socket_rating = SelectField("Power socket availbility", validators=[DataRequired()],
                                choices=[i * "🔌" for i in range(1, 5)])
    submit = SubmitField('Submit')


# ---------------------------------------------------------------------------

# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        new_cafe = f"\n{form.cafe.data}, " \
                   f"{form.location.data}," \
                   f"{form.opening_time.data}," \
                   f"{form.closing_time.data}," \
                   f"{form.coffee_rating.data}," \
                   f"{form.wifi_rating.data}," \
                   f"{form.socket_rating.data}"
        with open('cafe-data.csv', 'a',encoding="utf8") as csv_file:
            csv_file.write(new_cafe)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding="utf8") as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
