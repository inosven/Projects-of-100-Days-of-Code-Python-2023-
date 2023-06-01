import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 22.210928  # Your latitude
MY_LONG = 113.552971  # Your longitude

my_email = "quansunpythonlearning@gmail.com"
to_address = "quansunpythonlearning@yahoo.com"
password = "xwbbuydfprsnmqlu"
def check_position():


    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
# Your position is within +5 or -5 degrees of the ISS position.
    if abs(MY_LAT - iss_latitude) <= 5 and abs(MY_LONG - iss_longitude) <= 5:
        return True
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.


# print(sunrise, sunset)
def is_dark():
    if time_now.hour <= sunrise or time_now.hour >= sunset:
        return True
    else:
        return False

while True:
    time.sleep(60)
    if check_position() and is_dark():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password),
            connection.sendmail(from_addr=my_email, to_addrs=to_address, msg="Subject:Look up!\n\nThe ISS is above you in the sky!")
