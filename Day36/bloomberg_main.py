import requests
import os
from stock_data_json import STOCK_DATA
from twilio.rest import Client

import time

tic = time.perf_counter()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = os.environ.get('STOCK_API_KEY')
NEWS_KEY = os.environ.get('NEWS_API_KEY')

TWILL_SID = os.environ.get('TWILL_ACCOUNT')
TWILL_KEY = os.environ.get('TWILL_AUTH')

print(TWILL_SID)
print(TWILL_KEY)

VIRTUAL_NUMBER = os.environ.get('TWILL_NUMBER')
MY_NUMBER = os.environ.get('MY_NUMBER')




is_higher = False
is_lower = False
get_news = False

## API CALL = removed as takes too long
# stock_dict = {}
# STOCK_PARAMS = {
#     "function":"TIME_SERIES_DAILY",
#     "symbol":STOCK,
#     "outputsize" : "compact",
#     "apikey" : STOCK_KEY
# }
#
# stock_response = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
# stock_data = stock_response.json()["Time Series (Daily)"]


stock_data = STOCK_DATA  # comment this out if using API
data_list = [value for key, value in STOCK_DATA.items()]

yesterday_price = float(data_list[0]["4. close"])
day_before_price = float(data_list[1]["4. close"])

diff = abs(yesterday_price - day_before_price)
limit = yesterday_price * 0.05

if diff > limit:
    get_news = True
    if yesterday_price > day_before_price:
        is_higher = True
    else:
        is_lower = True



## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
# HINT 1: Think about using the Python Slice Operator


NEWS_PARAMS ={
    "q": COMPANY_NAME,
    "apiKey": NEWS_KEY
}

news_response = requests.get(url=NEWS_ENDPOINT,params=NEWS_PARAMS)
news_articles = news_response.json()["articles"][:3]



                      #\nHeadline:{article["title"]} \nBrief{article["description"]}" for article in news_articles)


# ----------------------- SEND MESSAGES ---------------------

## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
# HINT 1: Consider using a List Comprehension.
triangle = "🔺"
if is_higher:
    triangle = "🔺"
else:
    triangle = "🔻"

formatted_articles = [f"{STOCK}:{triangle}{round(diff)}%" \
                      f"\nHeadline:{article['title']}" \
                      f"\nBrief: {article['description']}"""  for article in news_articles]

get_news = True
if get_news:
    for article in formatted_articles:
        client = Client(TWILL_SID, TWILL_KEY)



        message = client.messages.create(
            body=article,
            from_=VIRTUAL_NUMBER,
            to=MY_NUMBER
        )

        print(message.status)






# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
