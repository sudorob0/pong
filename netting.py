from turtle import Turtle


class Netting(Turtle):

    # this creates the netting for the screen
    def __init__(self, line):
        super().__init__()
        self.speed("fastest")
        self.penup()
        net = line * 30 - 300
        self.setpos(0, net)
        self.shape("square")
        self.color("white")
        self.shapesize(.8, .2)

