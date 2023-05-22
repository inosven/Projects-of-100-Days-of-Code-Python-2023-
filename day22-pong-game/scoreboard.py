from turtle import Turtle

Y_POSITION = 240
ALIGNMENT = "center"
FONT = ("Arial", 36, "normal")


class Scoreboard(Turtle):

    def __init__(self, xcor):
        super().__init__()
        self.score = 0
        self.create_scoreboard(xcor)
        self.update()

    def create_scoreboard(self, xcor):
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(xcor, Y_POSITION)

    def update(self):
        self.clear()
        self.write(f"{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def create_middle(self):
        t = Turtle()
        t.penup()
        t.hideturtle()
        t.color("white")
        t.setheading(270)
        t.pensize(5)
        for i in range(300, -300, -60):
            t.penup()
            t.goto(0, i)
            t.pendown()
            t.forward(30)
