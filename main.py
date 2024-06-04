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

now = dt.datetime.now()
today = now.day
this_month = now.month
target_row = pandas[pandas["day"] == today]
target_name = target_row["name"].values[0]
target_email = target_row["email"].values[0]
target_day = target_row["day"].values[0]
target_month = target_row["month"].values[0]

if (target_day == today).any() and (target_month == this_month).any():
    new_letter = random_letter.replace(PLACEHOLDER, target_name)
    print("Email sent successfully!")
    # SMTP value will change according to your email address provider. Some examples:
    # smtp.gmail.com (Google), smtp.live.com (Outlook), smtp.mail.yahoo.com (Yahoo).
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                            from_addr=my_email,
                            to_addrs=target_email,
                            msg=f"Subject:Happy Birthday!\n\n{new_letter}"
                            )
else:
    print("Its nobody's birthday today")
