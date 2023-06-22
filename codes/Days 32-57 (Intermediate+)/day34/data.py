import requests, json

endpoint = 'https://opentdb.com/api.php'
parameters = {
    'amount':10,
    'type': 'boolean'
}

response = requests.get(f'{endpoint}', params=parameters)
df = response.json()
question_data = df['results']