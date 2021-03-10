from flask import Flask
from random import randint
app = Flask(__name__)

correct_url = "https://media.giphy.com/media/3d0PahT093UPe/giphy.gif"
higher_url = "https://media.giphy.com/media/xM3MSNqU6ffAA/giphy.gif"
lower_url = "https://media.giphy.com/media/2Vizs8uaBEb6g/giphy.gif"
home_url = "https://media.giphy.com/media/AYOEJe1rdWEes/giphy.gif"

target_num = randint(0, 9)
print(target_num)

@app.route('/')
def home():
    return f"<h1 style=color:#00FFFF>Guess a number between 0 and 9</h1> \n" \
      f"<img width=400px src={home_url}>"

@app.route('/<int:num>')
def guess_number(num):
    if num > target_num:
        return f"<h1  style=color:MediumSlateBlue>Too high!<h1>" \
               f"<img width=400px src={higher_url}>"
    elif num < target_num:
        return f"<h1  style=color:DeepPink>Too low!<h1>" \
               f"<img width=400px src={lower_url}>"
    else:
        return f"<h1  style=color:MediumSeaGreen>CORRECT!<h1>" \
               f"<img width=400px src={correct_url}>"

if __name__ == '__main__':
   app.run(debug=True)