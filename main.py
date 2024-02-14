from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_items = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
drinks = menu_items.get_items()
coffee_machine_is_on = True

while coffee_machine_is_on:
    user_answer = input(f"What would you like? {drinks}: ").lower()
    if user_answer == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_answer == "off":
        print("Coffee machine is going shot down...")
        coffee_machine_is_on = False
    else:
        drink = menu_items.find_drink(user_answer)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

