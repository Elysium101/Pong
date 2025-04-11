from turtle import Turtle

FONT = ("Courier", 60, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)    
        self.write(arg=f"{self.l_score}", align="center", font=FONT)
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", align="center", font=FONT)


    def increase_l_score(self):
        self.clear()
        self.l_score += 1
        self.goto(-100, 200)
        self.write(arg=f"{self.l_score}", font=FONT)


    def increase_r_score(self):
        self.clear()
        self.r_score += 1
        self.goto(100, 200)
        self.write(arg=f"{self.r_score}", font=FONT)