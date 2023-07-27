"""
UDEMY - 100 Days of Code: The Complete Python Pro Bootcamp for 2023 by Dr. Angela Yu
Day - 23

I, Madara Wimalarathna wrote this program as a practice session for the above Udemy course.
It is a paid course. Therefore, please do not misuse :)

The idea behind the program, the scenario and the program structure was given in the course.
"""


# Imports and constants import time
import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
score_board = Scoreboard()

# Create player and a set of cars
player = Player()
cars = CarManager()

# Set player movements
screen.listen()
screen.onkey(player.go_up, "Up")

# Game activation
game_is_on = True

while game_is_on:
    # create new cars and move all the cars forward
    # If for loop run 100N times, 20N cars will be created
    if randint(0, 5) == 1:
        cars.get_new_car()
    cars.move()
    # Check for the finishing criteria
    # If the player is touching a car, the game is over
    if cars.check_distance(player):
        score_board.game_over()
        game_is_on = False
    # Once the player has crossed the finish live and complete the current level below reset actions will be taken
    # Take the player to initial position
    # Speedup the cars for the next round
    # Show the Update scoreboard level by one, so the user know this is a new level (Next round)
    if player.finished():
        player.reset()
        cars.increase_speed()
        score_board.level_increase()

    # slow down the for loop
    time.sleep(0.1)
    # reflect changes on screen
    screen.update()

screen.exitonclick()
