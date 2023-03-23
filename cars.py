import random
from turtle import Turtle
COLOR = ["orange","red","blue","green","yellow","pink","purple","violet"]


class Cars(Turtle):

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = 5

    def create_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=0.75,stretch_len=2.7)
            new_car.penup()
            # new_car.hideturtle()
            new_car.color(random.choice(COLOR))
            random_y = random.randint(-240,240)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def car_move(self):
        for i in self.all_cars:
            i.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += 10

