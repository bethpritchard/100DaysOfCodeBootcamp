from bs4 import BeautifulSoup
# import lxml

import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

articles = soup.find_all(name="a", class_="storylink")
article_texts = [tag.getText() for tag in articles]
articles_links = [tag.get("href") for tag in articles]


article_upvotes = [int(score.get_text().split()[0]) for score in soup.find_all(name="span", class_= "score")]



largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_index)
