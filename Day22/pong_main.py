from turtle import Screen
from paddle import Paddle
from ball import Ball
from pong_scoreboard import Scoreboard
import time


WIDTH = 800
HEIGHT = 600

RIGHT_X = 350
LEFT_X = -350

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(RIGHT_X)
l_paddle = Paddle(LEFT_X)
ball = Ball()
scoreboard = Scoreboard()


def choose_rounds():
    number_rounds = screen.textinput(title="Round Select", prompt="Choose number of rounds")
    try:
        number_rounds = int(number_rounds)
    except ValueError:
        number_rounds = screen.textinput(title="Round Select", prompt="Enter an integer")
    return number_rounds


number_rounds = choose_rounds()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    scoreboard.clear()
    scoreboard.display_score()
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collision with wall
    if abs(ball.ycor()) > 280:
        ball.bounce_y()



    # Detect collision with paddles
    if  ball.distance(r_paddle) < 45 and ball.xcor() > 320 or ball.distance(l_paddle) < 45 and ball.xcor() < -320:
        ball.bounce_x()


    # Detect collision with other walls
    if ball.xcor() > 360:
        scoreboard.increase_left_score()
        ball.start_over()

    if ball.xcor() < -360:
        scoreboard.increase_right_score()
        ball.start_over()

    if scoreboard.total_score == number_rounds:
        game_is_on = False
        scoreboard.game_over()
        time.sleep(5)
        screen.bye()




