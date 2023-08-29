import time
from turtle import Screen

import car_manager
import scoreboard
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Road Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
player1 = Player()
level = Scoreboard()
level.level()
car_count = 10
cars = []
for car_no in range(car_count):
    car = CarManager()
    car.start_position()
    cars.append(car)

screen.listen()
screen.onkey(fun=player1.move_up, key='Up')
game_is_on = True
loop_count = 0
while game_is_on:
    time.sleep(0.1)
    if loop_count - 6 == 0:
        loop_count -= 6
        new_car = CarManager()
        new_car.new_car_position()
        cars.append(new_car)
    for car_select in cars:
        if car_select.distance(player1) < 20 and car_select.xcor() < 50:
            level.game_over()
            game_is_on = False
        car_select.move_car()
    if player1.ycor() > 250:
        player1.start_position()
        car_manager.STARTING_MOVE_DISTANCE += car_manager.MOVE_INCREMENT
        scoreboard.LEVEL += 1
        level.level()
    loop_count += 1
    screen.update()
print("Game Over")
screen.exitonclick()