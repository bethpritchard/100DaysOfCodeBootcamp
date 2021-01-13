from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coffee_machine():
    """
    Main function for coffee machine
    """
    coffeemaker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()


    machine_on = True
    initial = True

    while machine_on:
        while initial:
            options = menu.get_items()
            user_selection = input(f"What would you like? ({options}): ").lower()
            if user_selection == 'report':
                coffeemaker.report()
                money_machine.report()
                break

            elif user_selection == 'off':
                print(f"Turning off.")
                machine_on = False
                break
            else:
                drink = menu.find_drink((user_selection))
                print(drink)
                sufficient_resources = coffeemaker.is_resource_sufficient(drink)
                if sufficient_resources:
                    sufficient_money = money_machine.make_payment(drink.cost)
                    if sufficient_money:
                        coffeemaker.make_coffee(drink)




if __name__ == '__main__':
    coffee_machine()