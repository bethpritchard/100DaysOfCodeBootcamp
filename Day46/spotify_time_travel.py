from datetime import datetime
import requests
from bs4 import BeautifulSoup
from pprint import pprint

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
# ------------- SET UP -----------
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private playlist-modify-public",
        redirect_uri="http://example.com",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]


#---------------- get date ---------

date_text = input("What date would you like to travel to? Input in format DD/MM/YYYY: ")
original_date = date_text
date_text = date_text.split('/')
date = ""
for elem in date_text[::-1]:
    date+= elem


year = date[:4]


# -------------------- get songs -----------------
url = f"https://www.officialcharts.com/charts/singles-chart/{date}/7501"

response = requests.get(url)
charts_site = response.text
soup=BeautifulSoup(charts_site,"html.parser")

songs = soup.find_all(name="div", class_="title")
song_names = [song.get_text().replace("\n", " ").strip().title() for song in songs]

# ----------------- get song uris ---------------------
song_uris = []

for song in song_names:
    result = sp.search(f"track: {song} year: {year}", type = "track")

    try:
        uri = result["tracks"]['items'][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Error: {song} does not exist on Spotify")


# # ---------------- create playlist ------------------------
playlist_name = f"Time Travel Back to {original_date}"
playlist_description = f"Time travel with Python!"
playlist = sp.user_playlist_create(user_id,
                                   playlist_name,
                                   public=True,
                                   description=playlist_description)

result = sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print("Playlist compiled!")