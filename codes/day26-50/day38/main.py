import datetime as dt
import requests as r


#NutritionIX API
ID = "xxx"
KEY = "xxx"
ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

text = input("Tell me wich exercise you did: ")

header = {
    "x-app-id":ID,
    "x-app-key":KEY
}

params = {
 "query": text,
 "gender":"male",
 "weight_kg": 78.3,
 "height_cm":177.64,
 "age":20
}

response = r.post(url=ENDPOINT, headers=header, json=params)
data = response.json()
data = data["exercises"]


#Sheety API
date = dt.datetime.now()
date = date.strftime("%d/%m/%Y")

time = dt.datetime.now()
time = time.strftime("%X")

for i in data:
    params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": i["name"],
            "duration": int(i["duration_min"]),
            "calories": i["nf_calories"]
    }
}

url = "https://api.sheety.co/username/projectName/sheetName"

user = "xxx"
password = "xxx"
basic = (user, password)

response = r.post(url=url, json=params, auth=basic)