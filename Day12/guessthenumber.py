import random as rand
import day12art
import time
EASY_LEVEL_TURNS = 5
HARD_LEVEL_TURNS = 10


def difficulty_select(difficulty):
    if difficulty == 'hard':
        return HARD_LEVEL_TURNS
    elif difficulty == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return False


def user_guess():
    return int(input("Input guess: "))


def compare(number, guess):
    if guess > number:
        return "Too high"
    else:
        return "Too low"

def play_round():
    number = rand.randint(0,100)
    print(f'''I'm thinking of a number between 0 and 100.''')
    guesses = False

    while not guesses:
        difficulty = input("Choose your difficulty. Type 'easy' or 'hard': ").lower()
        guesses = difficulty_select(difficulty)

    print(f"{difficulty.title()} level selected. You have {guesses} guesses!")

    while guesses > 0:
        current_guess = user_guess()
        if current_guess == number:
            print("Congratulations! You won!")
            print(day12art.win_art)
            guesses = 0
        else:
            guesses -= 1
            print(compare(number, current_guess))
            print(f"You have {guesses} guesses remaining!")

    if guesses == 0 and current_guess != number:
        print(f"You lose! The number was {number}")
        print(day12art.lose_art)
    time.sleep(3)





if __name__ == '__main__':
    print(day12art.logo)
    print(f"Welcome to the number guessing game!")
    while input("Do you want to play a round? type 'y' or 'n': ") == 'y':
        play_round()
