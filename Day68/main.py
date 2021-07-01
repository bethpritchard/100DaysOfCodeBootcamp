import werkzeug.security
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'password1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods = ["GET", "POST"])
def register():
    if request.method == 'POST':

        password_hashed = generate_password_hash(
            request.form.get("password"),
            method="pbkdf2:sha256",
            salt_length=8)

        new_user = User(
            name=request.form.get("name"),
            email=request.form.get('email'),
            password = password_hashed
        )
        db.session.add(new_user)

        # Log in an authenticate user

        db.session.commit()

        login_user(new_user)

        print("New user added")

        return redirect(url_for("secrets"))

    return render_template("register.html")


@app.route('/login',methods = ["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        #Check stored password hash against entered password hashed.
        if check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('secrets'))

    return render_template("login.html")


@login_required
@app.route('/secrets')
def secrets():
    return render_template("secrets.html")



@app.route('/logout')
def logout():
    pass


@app.route('/download')
def download():
    return send_from_directory('static',filename="files/cheat_sheet.pdf")

if __name__ == "__main__":
    app.run(debug=True)
