from turtle import Turtle
from time import sleep

DISTANCE = 20
NORTH = 90 
SOUTH = 270
WEST = 180
EAST = 0


class Snake:
    def __init__(self, size):
        self.past = []
        self.body = []
        for i in range(size):
            self.past.append([])
            snake_piece = Turtle()
            snake_piece.penup()
            snake_piece.shape("square")
            snake_piece.color("white")
            snake_piece.setposition(0 - (20 * i), 0)
            self.body.append(snake_piece)
        self.head = self.body[0]

    def move(self):    
        self.past[0] = self.head.position()
        self.head.forward(DISTANCE)
        for i in range(1, len(self.body)):
            self.past[i] = self.body[i].position()
            self.body[i].setposition(self.past[i-1])

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def eat(self):
        self.past.append([])
        snake_piece = Turtle()
        snake_piece.penup()
        snake_piece.shape("square")
        snake_piece.color("white")
        snake_piece.setposition(self.past[len(self.body)-1])
        self.body.append(snake_piece)