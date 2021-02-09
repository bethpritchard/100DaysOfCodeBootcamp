import requests
from pprint import pprint

import os

api_key = os.environ.get("TEQUILA_KEY")
api_headers = {
    "apikey": api_key,
    "accept": "application/json"
}

api_endpoint = "https://tequila-api.kiwi.com/locations/query"


class FlightSearch:
    def get_destination_code(self, city):
        query = {
            "term": city,
            "location_types" : "city",
            "limit" : 1
        }

        response = requests.get(url=api_endpoint, headers=api_headers, params=query)
        search_result = response.json()["locations"]
        return search_result[0]["code"]
