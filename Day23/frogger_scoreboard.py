from turtle import  Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.score = 1
        self.penup()
        self.goto(-200,260)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"LEVEL: {self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score += 1
        self.write(f"LEVEL: {self.score}", align=ALIGNMENT, font=FONT)
        self.display_score()


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)