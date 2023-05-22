from turtle import Turtle
Y_POSITION = [-20, 0, 20]
class Paddle(Turtle):

    def __init__(self, xcor):
        super().__init__()
        self.paddle_body = []
        self.create_paddle(xcor)

    def create_paddle(self, xcor):
        for i in range(len(Y_POSITION)):
            t = Turtle(shape="square")
            t.penup()
            t.color("white")
            t.goto(xcor, Y_POSITION[i])
            self.paddle_body.append(t)

    def up(self):
        if self.paddle_body[2].ycor() < 280:
            for seg in self.paddle_body:
                seg.setheading(90)
                seg.forward(20)
    def down(self):
        if self.paddle_body[0].ycor() > -280:
            for seg in self.paddle_body:
                seg.setheading(270)
                seg.forward(20)
