from datetime import datetime
import requests
import os

GENDER = "female"
WEIGHT_KG = YOUR WEIGHT
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE


APP_ID = os.environ.get("NUTRITIONIX_ID")
API_KEY = os.environ.get("NUTRITIONIX_KEY")

AUTH_KEY = os.environ.get("SHEETY_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ.get("SHEETY_URL")

exercises_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

sheet_headers = {
    "Authorization": f"Bearer {AUTH_KEY}"
}

# -------- Get new exercise from user -----------

user_input = input("Enter exercise: ")

exercise_params = {
    "query": user_input
}

exercise_response = requests.post(
    url=exercise_endpoint,
    headers=exercises_headers,
    json=exercise_params)

new_entry = exercise_response.json()

# ----------- Create params for Sheety ------------
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in new_entry["exercises"]:
    new_exercise = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }

    }

    add_exercise = requests.post(sheet_endpoint,
                                 json=new_exercise,
                                 headers=sheet_headers)
