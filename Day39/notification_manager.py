import os
from twilio.rest import Client


TWILL_SID = os.environ.get('TWILL_ACCOUNT')
TWILL_KEY = os.environ.get('TWILL_AUTH')

VIRTUAL_NUMBER = os.environ.get('TWILL_NUMBER')
MY_NUMBER = os.environ.get('MY_NUMBER')



class NotificationManager:
    def __init__(self):
        self.client = Client(TWILL_SID,TWILL_KEY)

    def send_text(self,message):
        message = self.client.messages.create(
            body=message,
            from_="+19014727436",
            to="+447464994849",
        )
        print(message.sid)
