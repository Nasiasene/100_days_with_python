import requests as r
URL_IATA = "https://tequila-api.kiwi.com/locations/query"
URL_FLY = "https://tequila-api.kiwi.com/v2/search"
API_KEY = "xxx"
import datetime as dt
HEADER = {"apikey": API_KEY}


class FlightSearch:


    def find_iata(self, data):
        query = {
            "term": data,
            "location_types": "city"
        }
        response  = r.get(url=URL_IATA, headers=HEADER, params=query)
        find_code = response.json()
        find_code = find_code["locations"][0]["code"]
        return find_code


    def search_flies(self, origin_code, destination_code):

        date_from = dt.datetime.now() + dt.timedelta(days=1)
        date_from =  date_from.strftime("%d/%m/%Y")
        date_to = dt.datetime.now() + dt.timedelta(days=180)
        date_to = date_to.strftime("%d/%m/%Y")

        query = {
            "fly_from": origin_code,
            "fly_to": destination_code,
            "date_from": date_from,
            "date_to": date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }
        
        response = r.get(url=URL_FLY, headers=HEADER, params=query)
        data = response.json()["data"][0]

        self.price = data["price"]
        self.origin_city=data["route"][0]["cityFrom"],
        self.origin_airport=data["route"][0]["flyFrom"],
        self.destination_city=data["route"][0]["cityTo"],
        self.destination_airport=data["route"][0]["flyTo"],
        self.out_date=data["route"][0]["local_departure"].split("T")[0],
        self.return_date=data["route"][1]["local_departure"].split("T")[0]