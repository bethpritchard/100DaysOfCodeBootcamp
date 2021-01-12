from coffee_data import MENU, resources, money


def user_input():
    return input("What would you like? (espresso/latte/cappuccino):").lower()



def money_in():
    dollars = int(input(f"Dollars: "))
    quarters = int(input(f"Quarters: "))*0.25
    cents = int(input(f"Cents: "))*0.01
    money_paid = dollars + quarters + cents
    return money_paid


def count_money(money_paid, price):
    global money
    if money_paid > price:
        money +=  price
        print(f"Here is your ${round(money_paid - price, 2)} change.")
        return True
    else:
        return False



def print_report():
    report = f'''
Water: {resources['water']}
Oat milk: {resources['oat milk']}
Coffee: {resources['coffee']}
Money: ${money}'''
    return report



def check_resources(coffee):
    for resource, value in coffee.items():
        if value > resources[resource]:
            print(f"Sorry, we are out of {resource}.")
            return False
        else:
            return True


def make_coffee(coffee):
    for key in coffee:
        resources[key] = resources[key] - coffee[key]





def invalid_choice():
    return f"Sorry, I do not understand that. Please try again."


def coffee_machine():
    """
    Main function for coffee machine
    """

    global chosen_coffee
    machine_on = True
    initial = True
    enough_resources = True

    # User input and mode selection
    while machine_on:
        while initial:
            user_selection = user_input()
            # print(f"User selection is: {user_selection}")
            if user_selection == 'report':
                print(print_report())
                break
            elif user_selection in MENU.keys():
            # Main coffee function
                chosen_coffee = MENU[user_selection]
                enough_resources = check_resources(chosen_coffee['ingredients'])

            elif user_selection == 'off':
                print(f"Turning off.")
                machine_on = False
                break
            else:
                print(invalid_choice())


            while enough_resources:
                print(f"Please insert at least ${chosen_coffee['cost']}")
                money_paid = money_in()
                if count_money(money_paid, chosen_coffee['cost']):
                    make_coffee(chosen_coffee['ingredients'])
                    print(f"Here is your {user_selection}. ☕ Enjoy!")
                    break
                else:
                    print(f"Sorry, that is not enough money. Money refunded.")
                    break





if __name__ == '__main__':
    coffee_machine()
