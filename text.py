from turtle import Turtle
import random
FONT = ("Courier", 20, "bold")


class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1

    def next_level(self):
        self.goto(-250, 250)
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
