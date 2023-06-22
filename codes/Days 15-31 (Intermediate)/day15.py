MENU = {"espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,},
        "cost": 1.5,},
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,},
        "cost": 2.5,},
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,},
        "cost": 3.0,}}

resources = {"water": 300, "milk": 200, "coffee": 100,}
profit = 0

def resource_amount(cafe):
    cafe_ingredients = cafe['ingredients']
    for i in resources:
        if resources[i] < cafe_ingredients[i]:
            print(f"Sorry there is not enough {i}.")
            return 0
        else:
            return 1

def money(cafe):
    print(f"price to be paid: {cafe['cost']}")
    print("Please insert coins.")
    money = 0
    money += int(input("0.25 cents: ")) * 0.25
    money += int(input("0.1 cents: ")) * 0.1
    money += int(input("0.05 cents: ")) * 0.05
    money += int(input("0.01 cents: ")) * 0.01
    return money

def money_true(money, cafe, profit):
    if cafe['cost'] > money:
        print("Sorry that's not enough money. Money refunded.")
        return 0
    else:
        tip = money - cafe['cost']
        profit += cafe['cost']
        print(f"Here is ${tip} in change.")
        return 1
    
def makecoffe(cafe):
    cafe_ingredients = cafe['ingredients']
    for i in resources:
        if i not in cafe_ingredients:
            continue
        else:
            resources[i] -= cafe_ingredients[i]
    print("Here is your ☕️. Enjoy!")


on_off = True
while on_off:
    select = input("What would you like? (espresso/latte/cappuccino): ")
    if select == 'off':
        print("Goodbye")
        on_off = False
    elif select == 'report':
        print("Here is the resources: ")
        for i in resources:
            print(f"{i}: {resources[i]}")
        print(f"profit: R${profit}.")
    else:
        if select != 'espresso' and select!= "latte" and select != "capuccino":
            print("input a valid option")
            continue
        else: 
            cafe = MENU[select]
            if resource_amount(cafe) == 1:
                money = money(cafe)
                if money_true(money, cafe, profit) == 1:
                    makecoffe(cafe)
                else:
                    continue
            else:
                continue