import smtplib
import random
import datetime as dt

my_email = "EMAIL"
password = "PASSWORD"

# ------------ Get random quote -------

with open("quotes.txt", "r") as file:
    quotes = file.readlines()

random_quote = random.choice(quotes)


# -------------- Send email -------------

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 1:
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="b.pritchard@newcastle.ac.uk", msg=random_quote)
    connection.close()

