#test comment
# Imports and constants
from turtle import Turtle

FONT = ("Courier", 24, "normal")


# Scoreboard class to define Scoreboard functionalities and attributes
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        """
        Initiate a level 1 scoreboard
        """
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the level by one  when the function is called
        """
        self.clear()
        self.goto(-210, 250)
        on_board = f"Level: {self.level}"
        self.write(on_board, align="center", font=FONT)

    def game_over(self):
        """
        Prints the GAME OVER message once the function is called
        """
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

    def level_increase(self):
        """
        maintain  the level attribute by increasing it by one on each call.
        Call the update_scoreboard to update the score on scoreboard on each call
        """
        self.level += 1
        self.update_scoreboard()
