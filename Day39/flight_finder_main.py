# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
import os
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# TODO SWITCH TO GOOGLE API

# TODO Step 4 of Day39
"https://github.com/leba0495/100-Days-Of-Python-Journey/blob/main/Day39:40-flight-deal-finder/data_manager.py"


tequila_key = os.environ.get("TEQUILA_KEY")
print(tequila_key)

tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"

tequila_header = {
    "apikey" : tequila_key
}


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])


    print(f"Sheet Data: {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()