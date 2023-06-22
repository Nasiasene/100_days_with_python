from menu import Menu
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker

menu = Menu()
machine = CoffeeMaker()
money_machine = MoneyMachine()


on_off = True
while on_off:
    order_coffee = input(f"\nWhat would you like?{menu.get_items()}: ")
    if order_coffee == 'off':
        on_off = False
        break
    elif order_coffee == 'report':
        machine.report()
        money_machine.report()
        continue
    elif order_coffee == 'refil':
        machine.refil() #MY_FUNCTION.
    else:
        if menu.find_drink(order_coffee):
            order_coffee = menu.find_drink(order_coffee)
        else:
            continue
        if machine.is_resource_sufficient(order_coffee):
            cost_coffee = order_coffee.cost
            if money_machine.make_payment(cost_coffee):
                machine.make_coffee(order_coffee)