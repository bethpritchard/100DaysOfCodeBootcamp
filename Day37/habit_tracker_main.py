import requests
from datetime import datetime, timedelta

USERNAME = "bethpritchard97"
TOKEN = "!0NkLs5zG*ga#5Dz"

pixela_endpoint = "https://pixe.la/v1/users"

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_id = "graph1"

headers = {
    "X-USER-TOKEN" : TOKEN
}

user_params = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

graph_params = {
    "id":graph_id,
    "name":"Water Tracker",
    "unit":"bottles",
    "type":"int",
    "color": "sora"
}


today = datetime.now()

yesterday = today - timedelta(days=1)
yesterday = yesterday.strftime("%Y%m%d")

update_params = {
    "date":today.strftime("%Y%m%d"),
    "quantity":"1000"
}


## ----------- Create account and graph
# reponse = requests.post(pixela_endpoint, json=user_params)
#
#
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)
#

today = today.strftime("%Y%m%d")

update_graph_url = f"{graph_endpoint}/{graph_id}"
delete_url = f"{update_graph_url}/{today}"


# response = requests.post(url=update_graph_url,headers=headers, json=update_params)
# print(response.text)
delete_response = requests.delete(url=delete_url, headers = headers)
print(delete_response.text)
response = requests.post(url=update_graph_url,headers=headers, json=update_params)
print(response.text)
print(update_graph_url)





