from datetime import datetime
import requests
from bs4 import BeautifulSoup

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]





# date_text = input("What year would you like to travel to? Input in format DD/MM/YYYY: ").split("/")
#
# date = ""
# for elem in date_text[::-1]:
#     date+= elem
# date = int(date)
date = 19970901

url = f"https://www.officialcharts.com/charts/singles-chart/{date}/7501"

response = requests.get(url)
charts_site = response.text
soup=BeautifulSoup(charts_site,"html.parser")

songs = soup.find_all(name="div", class_="title")
song_names = [song.get_text().replace("\n", " ").strip() for song in songs]



