from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 235)
        self.score = 0
        self.text = f"Score: {self.score}"
        self.write(self.text, False, align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.text = f"Score: {self.score}"
        self.clear()
        self.write(self.text, False, align="center", font=FONT)

    def reset_score(self):
        self.score = 0

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=FONT)
