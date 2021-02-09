import requests
import os

sheet_endpoint = os.environ.get("SHEET_ENDPOINT")
sheet_key = os.environ.get("SHEET_KEY")

sheet_headers = {
    "Authorization": f"Bearer {sheet_key}"
}


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheet_endpoint, headers=sheet_headers)
        sheet_data = response.json()
        self.destination_data = sheet_data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_code = {
                "price": {
                    "iataCode" : city['iataCode']
                }
            }
            response = requests.put(url=f"{sheet_endpoint}/{city['id']}",
                                    headers=sheet_headers,
                                    json=new_code)

