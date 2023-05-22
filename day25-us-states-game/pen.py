from turtle import Turtle

FONT = ["Arial", 8, "normal"]
ALIGNMENT = "center"


class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.create()

    def create(self):
        self.penup()
        self.hideturtle()

    def draw_at_location(self, to_write, x, y):
        self.goto(x, y)
        self.write(to_write, align="center", font=FONT)

