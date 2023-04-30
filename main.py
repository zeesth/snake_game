from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.listen()

simas = Snake(3)
food = Food()
score = Score()

screen.onkey(simas.up, "Up")
screen.onkey(simas.down, "Down")
screen.onkey(simas.left, "Left")
screen.onkey(simas.right, "Right")

screen.update()
game = True

while game:
    screen.update()
    sleep(0.1)
    simas.move()
    
    if simas.head.distance(food) < 15:
        food.respawn()
        simas.eat()
        score.point()

    if abs(simas.head.xcor()) > 280 or abs(simas.head.ycor()) > 280:
        game = False
        score.end()
    
    for piece in simas.body[1:]:
        if simas.head.distance(piece) < 15:
            game = False
            score.end()

screen.exitonclick()