from turtle import Screen

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(WIDTH, HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)




screen.listen()
# screen.onkey(pong.move_up, "Up")
# screen.onkey(pong.move_down, "Down")


screen.exitonclick()