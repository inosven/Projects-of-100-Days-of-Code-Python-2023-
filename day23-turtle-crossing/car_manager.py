from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        if random.randint(1, 6) == 1:
            self.all_cars.append(Car())

    def move_cars(self):
        for car in self.all_cars:
            car.setx(car.xcor() - self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.setheading(180)
        self.penup()
        self.setx(300 - STARTING_MOVE_DISTANCE)
        self.sety(random.randint(-250, 250))
