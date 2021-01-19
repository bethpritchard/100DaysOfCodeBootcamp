from turtle import Turtle
FONT = ("Arial", 36, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.hideturtle()
        self.total_score = 0

    def display_score(self):
        self.clear()
        self.goto(-100,240)
        self.write_score(self.left_score)
        self.goto(100, 240)
        self.write_score(self.right_score)

    def increase_left_score(self):
        self.left_score += 1
        self.total_score += 1
        self.display_score()

    def increase_right_score(self):
        self.right_score += 1
        self.total_score += 1
        self.display_score()

    def write_score(self, score):
        self.write(f" {score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER!\n\nFinal score:\n{self.left_score} : {self.right_score}", align=ALIGNMENT, font=FONT)
        self.goto(0, -300)
        if self.left_score > self.right_score:
            self.write(f"Left wins!")
        elif self.left_score < self.right_score:
            self.write(f"Right wins!")
        else:
            self.write(f"It's a draw!")

        self.left_score = 0
        self.right_score = 0

