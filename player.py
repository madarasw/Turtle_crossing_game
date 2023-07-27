# Imports and constants
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 230


# Player class to define player's functionalities and attributes
class Player(Turtle):

    def __init__(self):
        super().__init__()
        """
        Create and position a player at STARTING_POSITION, facing upwards
        """
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def go_up(self):
        """
        Move upwards by MOVE_DISTANCE in each function call
        """
        self.forward(MOVE_DISTANCE)

    def finished(self):
        """
        Check if the player has crossed the finish line.
        Return True if it has
        Return false if it hasn't
        """
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False

    def reset(self):
        """
        Take player to the initial position
        """
        self.goto(STARTING_POSITION)

