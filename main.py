import smtplib
import datetime as dt
import pandas as pd
from random import *
import os
PLACEHOLDER = "[NAME]"
# Change your email and password accordingly
EMAIL = "use_you_email@whatever.com"
PASSWORD = "put_your_password_here"

pandas = pd.read_csv("birthdays.csv")
txt_files = "letter_templates"
files = os.listdir(txt_files)
random_file = choice(files)
path = os.path.join(txt_files, random_file)

with open(path) as letter:
    random_letter = letter.read()

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    new_letter = random_letter.replace(PLACEHOLDER, birthday_person["name"])
    with smtplib.SMTP("INTRODUCE CORRECT DATA") as connection:
    # SMTP value will change according to your email address provider. Some examples:
    # smtp.gmail.com (Google), smtp.live.com (Outlook), smtp.mail.yahoo.com (Yahoo).
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{new_letter}"
        )
    print("Email sent successfully!")
else:
    print("Its nobody's birthday today")
