import turtle
from random import randint


speed_range_start = 5
speed_range_stop = 7
LEVEL_STEP = 3
car_number = 25

turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


class Car(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random_color())
        self.shapesize(1, 2)
        self.penup()
        self.goto(randint(-300, 300), randint(-250, 250))

    def move(self):
        self.bk(randint(speed_range_start, speed_range_stop))
        self.reset_car()

    def reset_car(self):
        if self.xcor() > 320 or self.xcor() < -320:
            self.setx(self.xcor() * -1)
            if -230 < self.ycor() < 230:
                self.sety(self.ycor() - randint(-20, 20))

    def next_level(self):
        global speed_range_start, speed_range_stop, car_number
        car_number += 5
        speed_range_stop += LEVEL_STEP
        self.move()




