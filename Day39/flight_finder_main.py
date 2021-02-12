import os
from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "LON"

# TODO Step 4 of Day39
"https://github.com/leba0495/100-Days-Of-Python-Journey/blob/main/Day39:40-flight-deal-finder/data_manager.py"


tequila_key = os.environ.get("TEQUILA_KEY")


tequila_endpoint = "https://tequila-api.kiwi.com/v2/search"

tequila_header = {
    "apikey" : tequila_key
}


data_manager = DataManager()
notification_manager = NotificationManager()
flight_search = FlightSearch()
sheet_data = data_manager.get_destination_data()


if sheet_data[0]["IATA Code"] == "":

    for row in sheet_data:
        row["IATA Code"] = flight_search.get_destination_code(row["City"])


    #print(f"Sheet Data: {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()


tomorrow = datetime.now() + timedelta(days=1)

six_months = tomorrow + timedelta(days=(6 * 30))



for destination in sheet_data:
    flight = flight_search.find_flight(
        ORIGIN_CITY_IATA,
        destination["IATA Code"],
        from_date=tomorrow,
        to_date=six_months
    )
    if flight is None:
        continue

    if flight.price < destination["Lowest Price"]:
        message = f"\nLow price alert! {flight.price} to fly from {flight.origin_city}" \
                  f"- {flight.origin_airport} " \
                  f"to {flight.destination_city} -{flight.destination_airport}" \
                  f" from {flight.out_date} to {flight.return_date} "

        notification_manager.send_text(message)
