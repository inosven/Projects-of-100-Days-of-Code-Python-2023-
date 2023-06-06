import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = "GK6NIW4EG1M1TFJT"
NEW_API_KEY = "7f92141cf23e4de8bfc8874ff42dbab2"
TWILIO_SID = "dasdasdasda"
TWILIO_AUTH_TOKEN = "asdas"
# account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
# auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
#
#
# stock_api

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_price_params = {
    "function" :"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "outputsize":"compact",
    "apikey":STOCK_API_KEY,
}
response = requests.get(url="https://www.alphavantage.co/query", params=stock_price_params)
response.raise_for_status()
stock_price_data = response.json()["Time Series (Daily)"]
# print(list(stock_price_data.items()))
yesterday_data = list(stock_price_data.items())[0]
before_yesterday_data = list(stock_price_data.items())[1]
# print(float(yesterday_data[1]["4. close"]))
rate = abs(float(yesterday_data[1]["4. close"])-float(before_yesterday_data[1]["4. close"])) / (float(before_yesterday_data[1]["4. close"]))
# print(rate)
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
news_params = {"q":COMPANY_NAME,
               "searchIn":"title",
               "apiKey":NEW_API_KEY,

}
if rate > 0.01:
    response = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    response.raise_for_status()
    news_data = response.json()
    three_articles = news_data["articles"][:3]
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
    formatted_articles = [f"Headline:{article['title']}. \nBrief:{article['description']}" for article in three_articles]

#Optional: Format the SMS message like this:
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for article in formatted_articles:
        message = client.messages.create(
        from_='+13613102508',
        body=article,
        to='+asdsadsdasd',
        )

    """
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

