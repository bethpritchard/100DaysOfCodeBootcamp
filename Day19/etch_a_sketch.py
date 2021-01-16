from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

heading = 0

def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clock_wise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)



def anti_clock_wise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_drawing():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()




screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=anti_clock_wise)
screen.onkey(key="d", fun=clock_wise)
screen.onkey(key = "c", fun = clear_drawing)

screen.exitonclick()
