import random as rand, art, time


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = cards[rand.randint(0, 12)]
    return random_card


def score_calc(hand):
    if len(hand) == 2 and sum(hand) == 21:
        return 0

    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)


def compare(user_score, computer_score):
    if computer_score == 0 or computer_score == 21:
        return "Computer got a blackjacK!"
    elif user_score == 0 or user_score == 21:
        return "You got a blackjack!!"
    elif user_score > 21:
        return "You went over 😒"
    elif computer_score > 21:
        return "Computer went over! You win 😁"
    elif user_score < computer_score:
        return f"You lose! 😭"
    elif user_score == computer_score:
        return f"It's a draw! 🤞"
    else:
        return f"You win! 💕😁🙌✨🎉"


def play_round():
    print(art.logo)
    is_game_over = False
    count = 0
    user_cards = []
    computer_cards = []

    while count < 2:
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
        count += 1

    while not is_game_over:
        user_score = score_calc(user_cards)
        computer_score = score_calc(computer_cards)
        print(f"""Your cards: {user_cards}, current score: {user_score}
            """)
        time.sleep(1)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True

        else:
            print(f"The computers first card is: {computer_cards[0]}")
            time.sleep(0.5)
            user_deal = input("Type 'y' to deal, type 'n' to pass: ")
            if user_deal == 'y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = score_calc(computer_cards)

    print(f'You final hand: {user_cards}')
    time.sleep(0.5)
    print(f'Your final score: {user_score}')
    time.sleep(0.5)
    print(f'Computer hand: {computer_cards}')
    time.sleep(0.5)
    print(f'Computer score: {computer_score}')
    time.sleep(0.5)
    print(compare(user_score, computer_score))


if __name__ == '__main__':
    while input("Do you want to play a round of Blackjack? Type 'y' or 'n': ")== 'y':
        play_round()
