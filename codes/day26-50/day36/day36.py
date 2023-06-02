import requests as r
import datetime as dt


API_KEY = 'xxx'
API_KEY2 = 'xxx'
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


params = {
    'function':'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK_NAME,
    'datatype':'json',
    'apikey': API_KEY
}


response = r.get(STOCK_ENDPOINT, params=params)
data = response.json()
data = data["Time Series (Daily)"]


datatime = f"{dt.datetime.now().year}-{(dt.datetime.now().month - 1):02d}-{dt.datetime.now().day:02d}"
yesterday_date = dt.datetime.now() - dt.timedelta(days=1)
yesterday_datetime = f"{yesterday_date.year}-{(yesterday_date.month):02d}-{(yesterday_date.day):02d}"


yesterday_data = data[yesterday_datetime]
yesterday_data_close = yesterday_data["4. close"]


daybefore_yesterday_date = yesterday_date - dt.timedelta(days=1)
daybefore_yesterday_datetime = f"{daybefore_yesterday_date.year}-{(daybefore_yesterday_date.month):02d}-{(daybefore_yesterday_date.day):02d}"

daybefore_yesterday_data = data[daybefore_yesterday_datetime]
daybefore_yesterday_data_close = daybefore_yesterday_data["4. close"]


diff = float(yesterday_data_close) - float(daybefore_yesterday_data_close)
if diff < 0:
    diff = -diff

percent_diff = (diff / float(yesterday_data_close)) * 100

if percent_diff >= 1:

    params2 = {
        'apiKey': API_KEY2,
        'qInTitle': COMPANY_NAME
    }

    response = r.get(NEWS_ENDPOINT, params=params2)
    news_data = response.json()['articles'][:3]
    
    article = [f"Title: {i['title']}.\n {i['description']} \n\n\n" for i in news_data]

print(article)
