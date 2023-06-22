import pandas as pd
import datetime as dt
import random as rd 
import smtplib as smtp
FILES = ("letter_1.txt", "letter_2.txt", "letter_3.txt")
EMAIL = 'davi.nasiamorim366@gmail.com'
PASSWORD = 'xxx'

today = dt.datetime.now()
atual_date = (today.day, today.month)

df = pd.read_csv("birthdays.csv")
lines = df.shape[0]

for i in range (lines):
    new_data = (df["day"][i], df['month'][i])

    if atual_date == new_data:
        name = df["name"][i]
        email = df["email"][i]

        file = rd.choice(FILES)
        with open(file) as email_body:
            text = email_body.read()
            text = text.replace("[NAME]", f"{name}")

        conection = smtp.SMTP("smtp.gmail.com")
        conection.starttls()
        conection.login(user=EMAIL, password= PASSWORD)
        conection.sendmail(
            from_addr=EMAIL, to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{text}"
        )
        conection.close()