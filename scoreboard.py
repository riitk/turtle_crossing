from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 255)
        self.write(f'Level: {self.level}', align="left", font=FONT)

    def write_score(self):
        self.clear()
        self.write(f'Level: {self.level}', align="left", font=FONT)

    def game_over(self):
        a = Turtle()
        a.color("red")
        a.hideturtle()
        a.penup()
        a.goto(-110, 0)
        a.write("GAME OVER !!! ", font=("Courier", 24, "normal"))
