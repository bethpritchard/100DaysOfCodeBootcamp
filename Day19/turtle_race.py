from turtle import Turtle, Screen
import random


def run_game():
    score = 0
    is_race_on = True
    screen.clear()
    user_bet = screen.textinput(title="Make your bet!",
                                prompt="Which turtle will win the race? Enter a colour: ").lower()
    colours = ["red", "orange", "yellow", "green", "blue", "purple"]
    if user_bet not in colours:
        screen.textinput(title="Make your bet!", prompt="Please choose a colour!!").lower()

    all_turtles = []

    for i in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.penup()
        new_turtle.color(colours[i])
        new_turtle.goto(x = -240, y =- 100 + (i * 50))
        all_turtles.append(new_turtle)

    if user_bet:
        is_race_on = True

    while is_race_on:
        for turtle in all_turtles:
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
            if turtle.xcor() > 230:
                is_race_on = False
                winning_colour = turtle.pencolor()
                if winning_colour == user_bet:
                    score += 1
                    print(f"You win! The {winning_colour} turtle won. \n Your score is {score}")
                else:
                    print(f"You lose! The {winning_colour} turtle won! \n Your score is {score}")
                    is_race_on = False





screen = Screen()
screen.setup(width = 500, height = 400)

game_running = True
while game_running:
    start_game = screen.textinput(title= "Start game?", prompt="Yes or no:").lower()
    if start_game == "yes":
        run_game()
    else:
        game_running = False
        screen.bye()





