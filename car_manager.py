from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


# def increase_speed(MOVE_DISTANCE= STARTING_MOVE_DISTANCE):
#     MOVE_DISTANCE += MOVE_INCREMENT


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.color(random.choice(COLORS))
        self.penup()
        self.y = random.randint(-250, 250)
        self.x = random.randint(0, 300)

    def start_position(self):
        self.goto(x=self.x, y=self.y)

    def new_car_position(self):
        self.goto(310, self.y)

    def move_car(self):
        x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(x=x, y=self.y)
