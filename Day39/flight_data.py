import requests
from pprint import pprint

import os

api_key = os.environ.get("TEQUILA_KEY")
api_headers = {
    "apikey": api_key,
    # "accept": "application/json"
}

api_endpoint = "https://tequila-api.kiwi.com/v2/search"
date_format = "01/04/2021"


class FlightData():
    def __init__(self):
        self.price = ""
        self.departure_code = "LON"
        self.destination_code = ""
        self.date_from = "01/03/2021"
        self.date_to = "01/09/2021"
        self.return_from = ""
        self.return_to = ""
        self.flight_type = ""
        self.curr = "GBP"

    def find_flight(self,city_code):
        query = {
            "fly_from": "LON",
            "fly_to": city_code,
            "date_from": self.date_from,
            "date_to": self.date_to,
            "flight_type": "return",
            "curr": self.curr,
            "sort" : "price"
        }

        response = requests.get(url=api_endpoint, headers=api_headers, params=query)
        data = response.json()
        return data["data"][0]



