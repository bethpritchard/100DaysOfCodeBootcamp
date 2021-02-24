from bs4 import BeautifulSoup
import requests

URL = "https://www.afi.com/afis-100-years-100-movies/"
response = requests.get(URL)
afi_webpage = response.text
soup = BeautifulSoup(afi_webpage, "html.parser")

movies = soup.find_all(name="h6", class_="q_title")

movie_titles = [movie.get_text() for movie in movies]

with open("movies.txt", "a") as file:
    for movie in movie_titles:
        file.write(movie + "\n")