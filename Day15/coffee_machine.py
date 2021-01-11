from coffee_data import MENU, resources, money


def user_input():
    return input("What would you like? (espresso/latte/cappuccino):").lower()


# TODO: display after user input




# TODO: take money in
def money_in():
    pass


# TODO: process coins

def count_money():
    pass


# TODO: print report
def print_report():
    report = f'''
Water: {resources['water']}
Oat milk: {resources['oat milk']}
Coffee: {resources['coffee']}
Money: ${money}'''
    return report


# TODO: check resources
def check_resources(coffee):
    for resource, value in coffee.items():
        if value > resources[resource]:
            return f"Sorry, we are out of {resource}"
        else:
            return f"resources ok"


# TODO: check transaction


# TODO: make coffee
def make_coffee():
    pass
    # TODO: select coffee from data
    # TODO: check resources
    # if not enough resources then refund


def invalid_choice():
    return f"Sorry, I do not understand that. Please try again."


def coffee_machine():
    """
    Main function for coffee machine
    """

    machine_on = True
    initial = True

    # User input and mode selection
    while machine_on:
        while initial:
            user_selection = user_input()
            # print(f"User selection is: {user_selection}")
            if user_selection == 'report':
                print(print_report())
                break
            elif user_selection in MENU.keys():
                chosen_coffee = MENU[user_selection]
                print(f"chosen_coffee = {chosen_coffee}")
                # TODO: fix this part
                #
                print(check_resources(chosen_coffee['ingredients']))
                break
            elif user_selection == 'off':
                print(f"Turning off.")
                machine_on = False
                break
            else:
                print(invalid_choice())






if __name__ == '__main__':
    coffee_machine()
