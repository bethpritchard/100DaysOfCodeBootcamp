import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWD_KEY = "MY_KEY"
OWD_URL = "https://api.openweathermap.org/data/2.5/onecall?"


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
    if int(weather_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

    account_sid = "MY_ACCOUNT"
    auth_token = "MY_KEY"

    client = Client(account_sid, auth_token, http_client=proxy_client)


    message = client.messages \
        .create(
        body="Join Earth's mightiest heroes. Like Kevin Bacon.",
        from_="VIRTUAL_NUMBER",
        to="MY_NUMBER"
    )

    print(message.status)
