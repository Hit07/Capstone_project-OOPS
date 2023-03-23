from turtle import Screen
from player import Player
import time as t
from cars import Cars
from score import Score


screen = Screen()
screen.setup(width=600,height=600)
screen.title("Crossing Game")
screen.tracer(0)


player = Player()
cars = Cars()
score = Score()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    screen.update()
    t.sleep(0.1)
    cars.create_car()
    cars.car_move()

    for car in cars.all_cars:
        if car.distance(player) <= 25:
            game_is_on = False
            score.crash()

    if player.ycor() > 280:
        player.reset_position()
        cars.increase_speed()
        score.point()
screen.exitonclick()

