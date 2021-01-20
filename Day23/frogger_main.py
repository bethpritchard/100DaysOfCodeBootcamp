import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from frogger_scoreboard import Scoreboard
Y_FINISH_LINE = 280
HIT_DISTANCE = 25
CAR_FREQUENCY = 5 #increase to get fewer cars

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
    if loop_number % CAR_FREQUENCY == 0:
        new_car = CarManager()
        cars.append(new_car)

    # Move cars
    for car in cars:
        car.move()

    # Detect collision
    for car in cars:
        if car.distance(player) < HIT_DISTANCE:
            print("squish")
            scoreboard.game_over()
            game_is_on = False

    if player.ycor() > Y_FINISH_LINE:
        player.restart()
        time.sleep(0.5)
        scoreboard.increase_score()





screen.exitonclick()
