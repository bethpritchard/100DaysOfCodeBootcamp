from turtle import Turtle

MOVE_LEN = 70

class Paddle(Turtle):
    def __init__(self, x_coord):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x_coord, 0)

    def go_up(self):
        new_y = self.ycor() + MOVE_LEN
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_LEN
        self.goto(self.xcor(), new_y)
        
