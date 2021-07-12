from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.player1 = 0
        self.player2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-70, 250)
        self.write(self.player1, False, align="center", font=("Arial", 30, "normal"))
        self.goto(70, 250)
        self.write(self.player2, False, align="center", font=("Arial", 30, "normal"))

    def score_player1(self):
        self.player1 += 1

    def score_player2(self):
        self.player2 += 1

