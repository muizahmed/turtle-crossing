from turtle import Turtle, Screen
from cars import Car, car_number
from user import User
from text import Text
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

text = Text()
user = User()
screen.onkey(fun=user.move, key="Up")

cars = []
for _ in range(car_number):
    car = Car()
    cars.append(car)


is_game_on = True
while is_game_on:
    text.next_level()
    screen.update()
    time.sleep(0.1)

    for car in cars:
        car.move()

        # Logic of Lose
        if user.distance(car) < 30:
            text.game_over()
            is_game_on = False

        # Logic of Win
        elif user.ycor() >= 320:
            text.clear()
            text.level += 1
            text.next_level()
            user.goto(0, -280)
            car.next_level()


screen.exitonclick()
