from internet_class import InternetSpeedTwitterBot
import os

NAME=os.environ["NAME"]
PASSWORD=os.environ["PASSWORD"]
DOWNLOAD = 350
UPLOAD = 100

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
down = bot.down
up = bot.up

if up < UPLOAD or down < DOWNLOAD:
    tweet = f"Hey Internet provider, why is my internet speed {down}down/{up}up when i pay for {DOWNLOAD}down/{UPLOAD}up?"
    bot.tweet_at_provider(tweet, NAME, PASSWORD)