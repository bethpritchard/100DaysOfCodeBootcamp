import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 54.326790
MY_LONG = -2.747580

my_email = "MY_EMAIL"
password = "MY_PASSWORD"

def is_close():
    global MY_LAT, MY_LONG
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if iss_latitude -5 <= MY_LAT <= iss_latitude + 5 and iss_longitude-5 <= MY_LONG <= iss_longitude + 5:
        return True
    return True



def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    #
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True
    return True




#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


if is_dark() and is_close():

    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="bethpritchard97@gmail.com", msg="Subject: LOOK OUTSIDE!\n\nISS is above you")
    connection.close()
