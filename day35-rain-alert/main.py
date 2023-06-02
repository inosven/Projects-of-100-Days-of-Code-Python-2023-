import os

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

api_key = os.environ.get("OWM_API_KEY")

parameters = {"lat": 22.163998,
              "lon": 113.557783,
              "exclude": "currently,daily,minutely",
              "appid": api_key,

              }
response = requests.get(url="https://api.openweathermap.org/data/3.0/onecall", params=parameters)
response.raise_for_status()
data = response.json()
will_rain = False
for hour in data["hourly"][:12]:
    if int(hour["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https":os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an 🌂",
        from_='+13613102508',
        to='+85368587654'
    )

print(message.status)

