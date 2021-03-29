from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

post_objs = []
response = requests.get("https://api.npoint.io/0ad676fe3ff093ac9c24")
all_posts = response.json()
#
# for post in all_posts:
#     new_post = Post(post_id=post["id"],
#                     title=post["title"],
#                     subtitle=post["subtitle"],
#                     content=post["body"])
#     post_objs.append(new_post)

@app.route("/")
def home():
    return render_template("index.html",posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)

