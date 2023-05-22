
# import heroes
# tim.shape("turtle")
# tim.color("red")
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
# print(heroes.gen())
# steps = 100
# for i in range(0, steps+1, 10):
#     if i % 20 == 0:
#         tim.penup()
#     else:
#         tim.pendown()
#     tim.forward(10)
from turtle import Turtle, Screen
import random
screen = Screen()
screen.colormode(255)

tim = Turtle()
# for i in range(3, 11):
#     tim.pencolor((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
#     angle = int(360/i)
#     for j in range(int(360/angle)):
#         tim.right(angle)
#         tim.forward(100)

tim.pensize(1)
tim.speed(0)


def random_direction():
    directions = [0, 90, 180, 270]
    angle = random.choice(directions)
    return angle


def random_color():
    rand_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return rand_color


def random_walk(steps):
    for i in range(steps):
        tim.setheading(random_direction())
        tim.pencolor(random_color())
        tim.forward(30)


def spirograph(radius, circle_number):
    angle = 360/circle_number
    for i in range(circle_number):
        tim.setheading(angle * i)
        tim.pencolor(random_color())
        tim.circle(radius)


spirograph(100,100)












screen.exitonclick()
