from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed()
        self.penup()
        self.x_move = 12
        self.y_move = 12

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def direction(self, angle):
        self.setheading(angle)
        return angle

    def bounce(self):
        self.y_move *= -1

    def hit(self):
        self.x_move *= -1




