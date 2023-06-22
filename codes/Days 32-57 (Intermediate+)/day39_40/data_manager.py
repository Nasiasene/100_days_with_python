import requests as r

USER = "xxx"
PASSWORD = "xxx"
URL = "https://api.sheety.co/xxx/xxx/xxx"
BASIC = (USER, PASSWORD)


class DataManager:
    
    def __init__(self):
        self.sheet_data = []


    def get_data(self):
        response = r.get(url=URL, auth=BASIC)
        data = response.json()
        self.sheet_data = data["prices"]
        return self.sheet_data
    

    def update_sheet(self, data):
        self.sheet_data = data
        for i in data:
            params = {
                "price": {
                    "iataCode": i["iataCode"]
                }
            }
            response = r.put(url=f"{URL}/{i['id']}", auth=BASIC, json=params)