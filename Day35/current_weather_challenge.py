import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWD_URL = "https://api.openweathermap.org/data/2.5/onecall"
OWD_KEY = os.environ.get("OWD_KEY")
account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN')

OWD_PARAMS = {
    "lat": 54.326790,
    "lon": -2.747580,
    "appid": OWD_KEY,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWD_URL, params=OWD_PARAMS)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][8:18]

will_rain = False

for hour_data in weather_slice:
    weather_code = hour_data["weather"][0]["id"]
    if int(weather_code) > 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="TWILIO_NUM",
        to="MY_NUM"
    )

    print(message.status)
