#joker_card.py
from .cards import *

class Joker(Card):
    """The Joker card which can have many unique rules according to the game."""
    
    def __init__(self, col):
        """col is either red or"""
        self.suit = 4
        if col == "red":
            self.value = 16
            self.imagename = "red_joker.png"
        elif col == "black":
            self.value = 17
            self.imagename = "black_joker.png"
        

    def __repr__(self):
        """Returns a string format of the object"""
        if self.value == 16:
            self.color = "Red"
        else:
            self.color = "Black"

        return f"{self.color} Joker"