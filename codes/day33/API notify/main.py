import requests, json

response = requests.get('http://api.open-notify.org/iss-now.json')
print(requests)

df = response.json()
lat = df['iss_position']['latitude']
long = df['iss_position']['longitude']

print(f"Latitude: {lat}\nLongitude: {long}")