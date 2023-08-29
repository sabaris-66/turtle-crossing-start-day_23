from turtle import Turtle
FONT = ("Courier", 24, "normal")
LEVEL = 1

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()

    def level(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"Level: {LEVEL}", align='center', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over", align='center', font=FONT)


