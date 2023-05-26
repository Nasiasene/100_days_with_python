import requests
from datetime import datetime
import smtplib as smtp

MY_LAT = -7.127623
MY_LONG = -34.824417
EMAIL = 'davi.nasiamorim366@gmail.com'
PASSWORD = 'xxx'
night_time = False
proximity = False


response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

if -5 <= iss_latitude - MY_LAT <=5 and -5 <= iss_longitude - MY_LONG <= 5:
    proximity = True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
df = response.json()
sunrise_h = int(df['results']['sunrise'].split('T')[1].split(":")[0])
sunset_h = int(df['results']['sunset'].split('T')[1].split(":")[0])

time_now = int(datetime.now().hour)

if time_now < sunrise_h and time_now >= sunset_h:
    night_time = True


if night_time and proximity:
    connection = smtp.SMTP('smtp.gamil.com')
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=EMAIL, to_addrs=EMAIL,
        msg='Subject:ISS Location.\n\nRIGHT ABOVE YOU!!!!')
    connection.close()