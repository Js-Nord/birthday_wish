import smtplib
import datetime as dt
import pandas as pd
from random import *
import os
PLACEHOLDER = "[NAME]"
my_email = "jessesnnt@gmail.com"
password = "nbbmnkjstrsgrjdt"

pandas = pd.read_csv("birthdays.csv")
txt_files = "letter_templates"
files = os.listdir(txt_files)
random_file = choice(files)
path = os.path.join(txt_files, random_file)

with open(path) as letter:
    random_letter = letter.read()

now = dt.datetime.now()
today = now.day
bd_day = pandas.day
bd_name = pandas.name

if (bd_day == today).any():
    target_row = pandas[pandas["day"] == today]
    target_name = target_row["name"].values[0]
    target_email = target_row["email"].values[0]

    new_letter = random_letter.replace(PLACEHOLDER, target_name)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
                            from_addr=my_email,
                            to_addrs=target_email,
                            msg=f"Subject:Happy Birthday!\n\n{new_letter}"
                            )


