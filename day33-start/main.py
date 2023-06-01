import requests
from datetime import datetime
MY_LAT = 22.198746
MY_LNG = 113.543877
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # if response.status_code != 200:
# #     raise Exception("Bad response from ISS API")
# response.raise_for_status()
# data = response.json()
# # print(data)
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (float(longitude), float(latitude))
# print(iss_position)
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}
response = requests.get(url="https://api.sunrise-sunset.org/json?lat=22.198746&lng=113.543877", params=parameters)
response.raise_for_status()

data= response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
time_now = datetime.now()
print(sunset,"\n",time_now)