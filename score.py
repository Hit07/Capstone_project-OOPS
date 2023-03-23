from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-250, 250)
        self.write(f"Level:{self.level}",align="left",font=("Courier", 24, "normal"))

    def crash(self):
        self.goto(0,0)
        self.write(f"Game over!!!😰", align="center", font=("Courier", 24, "normal"))

    def point(self):
        self.level += 1
        self.update()