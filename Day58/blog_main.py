from flask import Flask, render_template,request
import requests
import smtplib
import os

EMAIL_SENDER = os.environ.get("EMAIL_ACCOUNT")
PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_RECIPIENT = os.environ.get("EMAIL_TO")

app = Flask(__name__)

post_objs = []
response = requests.get("https://api.npoint.io/0067e63917ca7a5034d9")
all_posts = response.json()


@app.route("/")
def home():
    return render_template("index.html",posts=all_posts)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/post/<int:index>")
def display_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post["id"] == index:
            requested_post= blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email address"], data["phone number"], data["message"])
        return render_template("contact.html",msg_sent = True)

    return render_template("contact.html", msg_sent=False)



def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_SENDER, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL_SENDER, to_addrs=EMAIL_RECIPIENT, msg=email_message)

    print("Success: email sent")

if __name__ == "__main__":
    app.run(debug=True)

