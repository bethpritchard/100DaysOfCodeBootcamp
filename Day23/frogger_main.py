import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from frogger_scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

cars = []
car_count = 0

screen.listen()
screen.onkey(player.move_turtle, "space")
loop_number = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    loop_number += 1
    # Create new car
    if loop_number % 6 == 0:
        new_car = CarManager()
        cars.append(new_car)

    # Move cars
    for car in cars:
        car.move()

    # Detect collision
    for car in cars:
        if car.distance(player) < 30:
            print("squish")
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > 280:
        player.restart()
        time.sleep(1)
        scoreboard.increase_score()





screen.exitonclick()
