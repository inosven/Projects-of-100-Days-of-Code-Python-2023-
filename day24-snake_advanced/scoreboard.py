from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        with open("highscore.txt", "r") as file:
            self.high_score = int(file.read())
        self.score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("Game Over ! 😢", move=False, align=ALIGNMENT, font=FONT)
