##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib

my_email = "quansunpythonlearning@gmail.com"
password = "xwbbuydfprsnmqlu"

# 1. Update the birthdays.csv
info = pd.read_csv("birthdays.csv")
today = dt.datetime.today()
birthday_star = info[(info.month == today.month) & (info.day == today.day)]
print(birthday_star.name)

# 2. Check if today matches a birthday in the birthdays.csv
if birthday_star.empty:
    print('DataFrame is empty!')
else:
    for i in range(len(birthday_star)):
        letter_order = random.randint(1, 3)
        name = birthday_star.name.iloc[i]
        with open(f"./letter_templates/letter_{letter_order}.txt", "r") as file:
            content = file.read()
            new_content = content.replace("[NAME]", name)
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=birthday_star.email.iloc[i],
                                msg=f"Subject:Happy Birthday\n\n{new_content}")
# 4. Send the letter generated in step 3 to that person's email address.
