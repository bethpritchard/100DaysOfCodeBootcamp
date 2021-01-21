from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"
with open("snake_high_score.txt", mode="r") as file:
    HIGH_SCORE = file.read()
    HIGH_SCORE = int(HIGH_SCORE)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.high_score = HIGH_SCORE
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}    High score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.display_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)
