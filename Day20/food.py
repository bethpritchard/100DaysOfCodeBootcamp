from turtle import Turtle
import random
SHAPE = "circle"
COLOUR = "turquoise"

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color(COLOUR)
        self.speed("fastest")
        self.move_food()


    def move_food(self):
        random_x = random.randint(-275,275)
        random_y = random.randint(-275, 275)
        self.goto(random_x, random_y)




