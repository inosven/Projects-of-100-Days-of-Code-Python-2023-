import smtplib
import datetime as dt
import random
my_email = "quansunpythonlearning@gmail.com"
to_address = "quansunpythonlearning@yahoo.com"
password = "xwbbuydfprsnmqlu"
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=to_address,
#                         msg="Subject:Hello!\n\nThis is a test email."
#                         )

now = dt.datetime.now()
# print(now.month)

# date_of_birth = dt.datetime(year=1991, month=10, day=25)
# print(date_of_birth)

if now.weekday() == 1:
    with open("quotes.txt","r") as file:
        quotes = file.readlines()
        quote = random.choice(quotes)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=f"Subject:Monday Motivation\n\n{quote}")