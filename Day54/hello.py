from flask import Flask
app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_italic(f):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>PARAGRAPH!</p><h2>another line</h2>' \
           '<img src = https://media.tenor.com/images/eff22afc2220e9df92a7aa2f53948f9f/tenor.gif>' \




@app.route('/bye')
@make_bold
@make_italic
def say_bye():
    return "Bye!"


@app.route('/username/<name>/<int:number>')
def greet(name,number):
    return f"Hello there {name}. You are {number} years old."

if __name__ == '__main__':
    app.run(debug=True)