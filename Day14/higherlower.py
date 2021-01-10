from day14art import vs, logo
from game_data import data
import random
import time


def get_choice():
    return random.choice(data)

def compare_choice(a_followers, b_followers):
    if a_followers > b_followers:
        return "A"
    elif a_followers < b_followers:
        return "B"

def choice_description(choice):
    return f"{choice['name']}, a {choice['description'].lower()} from {choice['country']}"

def player_guess():
    return input("Who has more followers? Type 'A' or 'B': ").upper()


def change_choice(answer, choice_a, choice_b):
    if answer == 'B':
        changed_choice = choice_b
    else:
        changed_choice = choice_a
    return changed_choice



def play_round():
    continue_game = True
    score = 0
    round_number = 1
    #add in a while loop to break when lose
    choice_a = get_choice()
    choice_b = get_choice()


    while continue_game:

        print(f'''
        
        ROUND {round_number}

''')
        print(f"Compare A: {choice_description(choice_a)} ")
        print(vs)
        print(f"Compare B: {choice_description(choice_b)}")
        print()

        guess = player_guess().upper()
        answer = compare_choice(choice_a['follower_count'], choice_b['follower_count'])
        if guess not in ['A','B']:
            print("Invalid input. Try again.")
            guess = player_guess().upper()

        elif answer == guess:
            choice_a = change_choice(answer,choice_a,choice_b)
            choice_b = get_choice()
            score  += 1
            round_number += 1
            print(f"Correct! Current score: {score}")


        else:
            continue_game = False
            print("Incorrect!")

    print(f"Final score: {score}")





if __name__ == '__main__':
    print(logo)
    play_round()