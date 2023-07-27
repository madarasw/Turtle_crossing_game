# Imports and constants
from random import randint
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUM_CARS = 100


# CarManager Class to define car functionalities and attributes
class CarManager:
    def __init__(self):
        """
        Create cars: an array of cars which will be filled later with car objects
        Create finish line: define and draw the line for the turtle to finish and win the game. cars move below the line
        Create start line: define and draw the line for the turtle to start the game. cars move above this line
        """
        self.cars = []
        self.moving_speed = STARTING_MOVE_DISTANCE

        finish_line = Turtle()
        finish_line.color("black")
        finish_line.shape("square")
        finish_line.penup()
        finish_line.shapesize(stretch_wid=0.1, stretch_len=50)
        finish_line.goto(0, 220)

        start_line = Turtle()
        start_line.color("black")
        start_line.shape("square")
        start_line.penup()
        start_line.shapesize(stretch_wid=0.1, stretch_len=50)
        start_line.goto(0, -220)

    def get_new_car(self):
        """
        Create a new car and add it to the list of cars
        This function does not return a car
        """
        car = Turtle()
        car.color(COLORS[randint(0, 5)])    # or use random.choice(COLORS)
        car.shape("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.goto(300, randint(-200, 200))
        car.setheading(180)
        self.cars.append(car)

    def move(self):
        """
        Move cvar forward everytime this function calls
        This function does not return anything
        """
        for car in self.cars:
            car.forward(self.moving_speed)

    def increase_speed(self):
        """
        Increases the speed of moving every time this function calls
        This function does not return anything
        """
        self.moving_speed += MOVE_INCREMENT

    def check_distance(self, player):
        """
        Check if the turtle stands within the distance of 20 pixels
        This function return True if the car is too close to turtle
        This function return False if the car is not too close to turtle
        """
        for car in self.cars:
            if car.distance(player) < 20:
                return True
        return False




