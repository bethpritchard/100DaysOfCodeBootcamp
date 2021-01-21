from turtle import Screen
import time
from snake import Snake
from food import Food
from snake_scoreboard import Scoreboard


WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 17:
        food.move_food()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if abs(snake.head.xcor()) > (WIDTH / 2) - 10 or abs(snake.head.ycor()) > (HEIGHT / 2) - 10:
        snake.reset_segments()
        scoreboard.reset_score()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 0:
            snake.reset_segments()
            scoreboard.reset_score()



screen.exitonclick()
