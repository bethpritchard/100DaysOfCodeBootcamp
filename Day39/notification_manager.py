import os
from twilio.rest import Client
import smtplib


TWILL_SID = os.environ.get('TWILL_ACCOUNT')
TWILL_KEY = os.environ.get('TWILL_AUTH')

VIRTUAL_NUMBER = os.environ.get('TWILL_NUMBER')
MY_NUMBER = os.environ.get('MY_NUMBER')

EMAIL = os.environ.get("EMAIL")
EMAIL_PASS = os.environ.get("PASSWORD")


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILL_SID,TWILL_KEY)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=VIRTUAL_NUMBER,
            to=MY_NUMBER,
        )
        print(message.sid)

    def send_email(self, message, user_email, flight_url):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=EMAIL, password=EMAIL_PASS)
            for user in user_email:
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=user,
                    msg=f"Subject:Beth's Flight Club Alert\n\n{message}\n{flight_url}"
                )
