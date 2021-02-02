"""
Edit CSV with emails to send
"""



import smtplib
import random
import datetime as dt
import pandas
import random

PLACEHOLDER = "[NAME]"

my_email = "EMAIL"
password = "EMAIL"

# ------------------ get birthday dict ------------------
df = pandas.read_csv("birthdays.csv")

birthday_dict = {(row.day, row.month): {"name": row.person_name, "email": row.email} for (index, row) in df.iterrows()}

# ------------------  get today's date and compare ------------------

today = dt.datetime.now()
current_month = today.month
current_day = today.day

today_date = (current_day, current_month)

# ------------------  get random letter and replace ------------------

random_number = random.randint(1, 3)
with open(f"letter_templates/letter_{random_number}.txt", "r") as file:
    letter = file.read()

if today_date in birthday_dict.keys():
    birthday = birthday_dict[today_date]

    name = birthday["name"]
    email = birthday["email"]

    letter = letter.replace(PLACEHOLDER, name)
    letter = letter.replace("Angela", "Beth")

# -------------------------  send email ---------------------------------

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email, msg=letter)
    connection.close()
