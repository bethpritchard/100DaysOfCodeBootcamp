import requests
from bs4 import BeautifulSoup
import smtplib
import os

my_email = os.environ.get("EMAIL_ACCOUNT")
password = os.environ.get("EMAIL_PASSWORD")
email_to = os.environ.get("EMAIL_TO")

url = "https://www.amazon.co.uk/Tefal-Actifry-Traditional-Portions-Capacity/dp/B078QT1288/ref=sr_1_3?crid=17AN6E7PIQ503&dchild=1&keywords=tefal+air+fryer&qid=1614535742&sprefix=tefal%2Caps%2C267&sr=8-3"
target_price = 180
headers = {
    "Accept-Language": "en-GB,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}

response = requests.get(url=url, headers=headers)
amazon_site = response.text

soup = BeautifulSoup(amazon_site, "lxml")
price_soup = soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").text
current_price = float(price_soup.split("£")[1])
item_name = soup.find(name="span", class_="a-size-large product-title-word-break").text.strip()

def send_email(message):
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=email_to, msg=message)
    connection.close()
    print("Email sent.")


if current_price <= target_price:
    message = f"Subject: Amazon Price Alert. \n\n{item_name} down to {current_price}. Buy now!"
    send_email(message)
