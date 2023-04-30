from turtle import Turtle

FONT = ("Arial", 15, "bold")
END_FONT = ("Arial", 30, "bold")
ALIGNMENT = "center"
TITLE = -10, 275

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.total_points = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(TITLE)
        self.write(f"Score: {self.total_points}", align=ALIGNMENT, font=FONT)
        
    def point(self):
        self.total_points += 1
        self.clear()
        self.write(f"Score: {self.total_points}", align=ALIGNMENT, font=FONT)
        
    def end(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=END_FONT)