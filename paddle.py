from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, cor):
        super().__init__()
        self.penup()
        self.goto(cor)
        self.shape("square")
        self.resizemode(rmode="user")
        self.color("white")
        self.shapesize(stretch_wid=5 , stretch_len=1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

        