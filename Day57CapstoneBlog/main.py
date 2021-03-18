from flask import Flask, render_template
import requests
from post import Post

blog_url = "https://api.npoint.io/5abcca6f4e39b4955965"

app = Flask(__name__)

post_objs = []
response = requests.get(blog_url)
all_posts = response.json()
for post in all_posts:
    new_post = Post(post_id=post["id"],
                    title=post["title"],
                    subtitle=post["subtitle"],
                    content=post["body"])
    post_objs.append(new_post)


@app.route("/")
def home():
    return render_template("index.html", posts=post_objs)

@app.route("/post/<int:num>")
def get_blog(num):
    return render_template("post.html", post=post_objs[num-1])

if __name__ == "__main__":
    app.run(debug=True)
