from scraping import get_lists
from selenium_response import Sheet

all_lists = get_lists()

for i in range(len(all_lists[0])):
    bot = Sheet()
    for count in range(3):
        bot.send(all_lists[count][i])
    bot.confirm()