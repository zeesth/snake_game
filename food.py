from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.respawn()

    def respawn(self):
        x = randint(-270, 270)
        y = randint(-270, 270)
        self.goto(x, y)