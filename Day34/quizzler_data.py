import requests
import html


parameters = {
    "amount":10,
    "type": "boolean"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
data = response.json()
question_data = data["results"]
#
# for question_number in question_data:
#     question_number["question"]= html.unescape(question_number["question"])
#
# print(question_data)