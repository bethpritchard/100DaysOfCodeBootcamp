import requests
from pprint import pprint
from flight_data import FlightData

import os

api_key = os.environ.get("TEQUILA_KEY")


tequila_endpoint = "https://tequila-api.kiwi.com"



class FlightSearch:

    def get_destination_code(self, city_name):
        endpoint = f"{tequila_endpoint}/locations/query"
        headers = {
            "apikey": api_key,
            "accept": "application/json"
        }
        query = {
            "term": city_name,
            "location_types" : "city",
            "limit" : 1
        }
        response = requests.get(url=endpoint, headers=headers, params=query)
        search_result = response.json()["locations"]
        return search_result[0]["code"]

    def find_flight(self, origin_city_code, destination_city_code, from_date, to_date):
        endpoint = f"{tequila_endpoint}/v2/search"
        headers = {
            "apikey": api_key,
        }
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
            "sort" : "price",
            "max_stopovers" : 0
        }

        response = requests.get(url=endpoint, headers=headers, params=query)

        try:
            data = response.json()['data'][0]
            #print(data)
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        #print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data