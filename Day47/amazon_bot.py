import requests
from bs4 import BeautifulSoup

url ="https://www.amazon.co.uk/Tefal-Actifry-Traditional-Portions-Capacity/dp/B078QT1288/ref=sr_1_3?crid=17AN6E7PIQ503&dchild=1&keywords=tefal+air+fryer&qid=1614535742&sprefix=tefal%2Caps%2C267&sr=8-3"

headers = {
    "Accept-Language" : "en-GB,en;q=0.5",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}

response = requests.get(url=url, headers=headers)
amazon_site = response.text

soup = BeautifulSoup(amazon_site, "lxml")
price_soup = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").text
price = price_soup.split("£")[1]
print(soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").text)