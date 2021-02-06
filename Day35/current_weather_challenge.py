import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

OWD_URL = "https://api.openweathermap.org/data/2.5/onecall"
OWD_KEY = "06b95e007082c4a6a8271b60ce917fd6"
account_sid = 'ACbaa3c082fa755d4ad5f3dbc44d01a643'
auth_token = '27aab67bdfab27b20f14a04c02af26d6'

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
    #proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})
    client = Client(account_sid, auth_token)


    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+19014727436",
        to="+447464994849"
    )

    print(message.status)
