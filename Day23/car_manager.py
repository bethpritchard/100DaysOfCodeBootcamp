from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "turquoise"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
Y_COORDS = list(range(-230,250,10))
INITIAL_X = 280


class CarManager(Turtle):
    def __init__(self):
        super(CarManager, self).__init__()
        self.color(r.choice(COLORS))
        self.setheading(180)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2.5)
        initial_y = r.choice(Y_COORDS)
        self.goto(INITIAL_X, initial_y)
        self.move_dist = STARTING_MOVE_DISTANCE
        self.speed("fastest")

    def move(self):
        new_x = self.xcor() - self.move_dist
        self.goto(new_x, self.ycor())

    def increase_level(self):
        self.move_dist += MOVE_INCREMENT

