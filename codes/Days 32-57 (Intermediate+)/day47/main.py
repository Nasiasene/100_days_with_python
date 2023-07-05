import requests as r
from bs4 import BeautifulSoup
import lxml
import pandas as pd
import smtplib as smtp
import sys
import os

EMAIL1 = "davi.nasiamorim366@gmail.com"
EMAIL2 = "davi.ted@hotmail.com"
PASSWORD = os.environ["PASSWORD"]

#Modify or Check your wishlist.
choose = int(input("Do you want to modify an item in your wish list or just check? (0-Modify 1-Check): "))

if choose == 0:
    choose = int(input("You want to remove or append an item? (0-Append 1-Remove): "))
    if choose == 0:
        item_name = input("Insert the name of the product: ").title()
        url = input("Insert the amazon webpage: ")
        price = int(input("Insert the price you wan't check: R$"))
        item = {
            "item_name": str(item_name),
            "url": str(url),
            "price": price,
        }

        df = pd.DataFrame([item])

        try:
            old_df = pd.read_csv("codes\Days 32-57 (Intermediate+)\day47\items.csv")
            new_df = pd.concat([old_df, df], ignore_index=True)
        except FileNotFoundError:
            new_df = df

        new_df.to_csv("codes\Days 32-57 (Intermediate+)\day47\items.csv", index=False)

    else:
        try:
            df = pd.read_csv("codes\Days 32-57 (Intermediate+)\day47\items.csv")
        except FileNotFoundError:
            print("Have a wishlist so you can check it!")
            sys.exit()
        name = input("Insert the name of the product: ").title()
        df = df.drop(df[df["item_name"] == name].index)
        df.to_csv("codes\Days 32-57 (Intermediate+)\day47\items.csv", index=False)


else:
    try:
        df = pd.read_csv("codes\Days 32-57 (Intermediate+)\day47\items.csv")
    except FileNotFoundError:
        print("Have a wishlist so you can check it!")
        sys.exit()
    




#Check the price with webscrapping.
    items = []

    for index, row in df.iterrows():
        url = row["url"]
        check_price = row["price"]

        params = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
                    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
                }

        response = r.get(url, headers=params)
        html = response.content

        soup = BeautifulSoup(html, "lxml")
        price = soup.find(class_="a-price-whole").get_text()
        price = price.split(",")[0]
        price = int(price.replace(".", ""))

        if price <= check_price:
            items.append(row["item_name"])
            send_email = True



#Send Email

    if send_email:
        str = ''
        count = 0
        for i in items:
            count+=1
            if count == len(items):
                str += f"{i}."
            else:
                str += f"{i}, "

        conection = smtp.SMTP("smtp.gmail.com")
        conection.starttls()
        conection.login(user=EMAIL1, password= PASSWORD)
        conection.sendmail(
            from_addr=EMAIL1, to_addrs=EMAIL2,
            msg=f"Items from your Wishlist !\n\nItems on your wishlist are priced below normal!\nThe items are: {str}"
        )
        conection.close()

    else:
        print("Sorry, but none of the items are priced below the stipulated.")