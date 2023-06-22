from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

notification = NotificationManager()
sheet_api = DataManager()
sheet_data = sheet_api.get_data()

search_api = FlightSearch()

for i in sheet_data:
    iata = i["iataCode"]
    if iata == "":
        i["iataCode"] = search_api.find_iata(i["city"])

sheet_api.update_sheet(sheet_data)
sheet_data = sheet_api.get_data()


city_dicts = {}
for i in sheet_data:
    check_flights = search_api.search_flies(origin_code="LON", destination_code=i["iataCode"])
    city_dicts[i["city"]] = {
        "price": search_api.price,
        "origin_city": search_api.origin_city,
        "origin_airport": search_api.origin_airport,
        "destination_city": search_api.destination_city,
        "destination_airport": search_api.destination_airport,
        "out_date": search_api.out_date,
        "return_date": search_api.return_date
    }
    
    if city_dicts[i["city"]]["price"] < i["lowestPrice"]:

        notification.send_email(
            email_to="davi.ted@hotmail.com",
            message_sub="Low price ALERT!",
            message_body=f"Only {city_dicts[i['city']]['price']} to fly from {city_dicts[i['city']]['origin_city']}-{city_dicts[i['city']]['origin_airport']} to {city_dicts[i['city']]['destination_city']}-{city_dicts[i['city']]['destination_airport']}, from {city_dicts[i['city']]['out_date']} to {city_dicts[i['city']]['return_date']}"
        )