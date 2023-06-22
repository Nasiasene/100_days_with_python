import datetime as dt
import smtplib as smtp
import random as rd
MY_EMAIL = "davi.nasiamorim@gmail.com"
password = "your_password"

time = dt.datetime.now()
day = time.weekday()

if day == 1:
    with open("quotes.txt", 'r') as file:
        quotes = file.readlines()
        day_quote = rd.choice(quotes)

conection = smtp.SMTP("smtp.gmail.com")
conection.starttls()
conection.login(user=MY_EMAIL, password= password)
conection.sendmail(
    from_addr=MY_EMAIL, to_addrs="davi.ted@hotmail.com",
    msg=f"Subject:Day Quote!\n\n{day_quote}"
)
conection.close()