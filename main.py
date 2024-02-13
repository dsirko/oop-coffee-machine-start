from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_machine_is_on = True

while coffee_machine_is_on:
    user_answer = input("What would you like? (espresso/latte/cappuccino/): ").lower()
    if user_answer == "report":
        ingridients_report = CoffeeMaker()
        ingridients_report.report()
        money_report = MoneyMachine()
        money_report.report()
    if user_answer == "off":
        print("Coffee machine is going shot down...")
        coffee_machine_is_on = False
