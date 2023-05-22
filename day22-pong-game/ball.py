from turtle import Turtle
import random
RANGE1 = (-75, 75)
RANGE2 = (105, 255)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()
        self.ball_speed = 0.2

    def create_ball(self):
        self.penup()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.setheading(random.choice([random.randint(-75, 75), random.randint(105, 255)]))

    def move(self):
        self.speed(0.1)
        self.forward(self.ball_speed)

    def collision_with_up_down(self):
        self.setheading(360 - self.heading())

    def collision_with_paddle(self):
        self.setheading(540 - self.heading())

    def recenter(self):
        self.goto(0, 0)
        self.ball_speed = 0.2
        self.setheading(random.randint(0, 360))

    def speed_up(self):
        self.ball_speed *= 1.1
        self.move()
