from turtle import Turtle


class Paddle(Turtle):

    # making the paddle
    def __init__(self, start):
        super().__init__()
        self.speed("fastest")
        self.goto(start, 0)
        self.penup()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(1, 5)


    # moving the paddle
    def up(self):
        self.speed("fastest")
        self.forward(30)

    def down(self):
        self.speed("fastest")
        self.backward(30)