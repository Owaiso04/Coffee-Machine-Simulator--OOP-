from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

MENU = Menu()
Coins = MoneyMachine.COIN_VALUES
Resources = MenuItem(name="Resources", water=300, milk=200, coffee=100, cost=0)
Coffee_Maker = CoffeeMaker()
Money_Machine = MoneyMachine()

is_on = True

while is_on:
    options = MENU.get_items()
    choice = input(f"What would you like? {(options)}: ")
    if choice == "off":
        is_on == False
    if choice == "report":
        Coffee_Maker.report()
        Money_Machine.report()
    else:
        drink = MENU.find_drink(choice)
        if Coffee_Maker.is_resource_sufficient(drink) and Money_Machine.make_payment(
            drink.cost
        ):
            Coffee_Maker.make_coffee(drink)
