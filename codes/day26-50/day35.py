import requests
import smtplib as smtp

EMAIL = 'davi.nasiamorim366@gmail.com'
PASSWORD = 'xxx'
key ='xxx'
endpoint = 'https://api.openweathermap.org/data/2.5/forecast?'
parameters = {
    'lat':  -7.11532,
    'lon':   -34.861,
    'appid': key
}

response = requests.get(url=endpoint, params=parameters)
data = response.json()['list'][:12]


for i in range (len(data)):
    data_id = data[i]['weather'][0]['id']
    if data_id < 700:
        conection = smtp.SMTP("smtp.gmail.com")
        conection.starttls()
        conection.login(user=EMAIL, password= PASSWORD)
        conection.sendmail(
            from_addr=EMAIL, to_addrs='davi.ted@hotmail.com',
            msg=f"Subject:It's gonna rain!\n\nBring your umbrella."
        )
        conection.close()
