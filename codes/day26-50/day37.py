import requests as r
import datetime as dt

'''
#Creating my user

ENDPOINT = 'https://pixe.la/v1/users'

params = {
    "token": 'xxx',
    "username": 'nasiasene',
    "agreeTermsOfService": 'yes',
    "notMinor": 'yes'
}

response = r.post(url=ENDPOINT, json=params)
print(response.text)
'''


'''
#Creating the graph

user = 'nasiasene'
token = 'xxx'
ENDPOIONT = f'https://pixe.la/v1/users/{user}/graphs'

params = {
    "id" : 'grraphic',
    "name" : 'test graphic',
    "unit" : 'commit',
    "type" : 'int',
    "color" : 'ajisai'
}

headers = {
    "X-USER-TOKEN" : token,
}

response = r.post(url=ENDPOIONT, json=params, headers=headers)
print(response.text)
'''


'''
#Add pixel's

today = dt.datetime.now()
user = 'nasiasene'
token = 'vilhennaa1'
GRAPHID = 'grraphic'
ENDPOIONT = f'https://pixe.la/v1/users/{user}/graphs/{GRAPHID}'

params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": '20'
}

headers = {
    "X-USER-TOKEN" : token,
}

response = r.post(url=ENDPOIONT, json=params, headers=headers)
print(response.text)
'''



'''
#Update Pixel's
today = dt.datetime.now()
user = 'nasiasene'
token = 'xxx'
GRAPHID = 'grraphic'
ENDPOIONT = f'https://pixe.la/v1/users/{user}/graphs/{GRAPHID}/{today.strftime("%Y%m%d")}'

params = {
    "quantity": '26'
}

headers = {
    "X-USER-TOKEN" : token,
}

response = r.put(url=ENDPOIONT, json=params, headers=headers)
print(response.text)
'''


'''
#Delete Pixel's
today = dt.datetime.now()
user = 'nasiasene'
token = 'xxx'
GRAPHID = 'grraphic'
ENDPOIONT = f'https://pixe.la/v1/users/{user}/graphs/{GRAPHID}/20230503'

headers = {
    "X-USER-TOKEN" : token,
}

response = r.delete(url=ENDPOIONT, headers=headers)
print(response.text)
'''