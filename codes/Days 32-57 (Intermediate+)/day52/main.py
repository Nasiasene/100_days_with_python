from InstaFollower import InstaFollower
import os

TARGET_ACCOUNT = 'cinephile.club'
EMAIL=os.environ["EMAIL"]
PASSWORD=os.environ["PASSWORD"]

bot = InstaFollower()
bot.login(EMAIL, PASSWORD)
bot.find_followers(TARGET_ACCOUNT)
bot.follow()