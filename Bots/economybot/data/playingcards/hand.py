#hand.py
import random
from .cards import Card

class Hand():
    """A players hand of playing cards"""
    def __init__(self):
        self.cards = []


    def add_card(self, card: Card):
        self.cards.append(card)
    
    def drawFromHand(self):
        if self.cards <= 0:
            return
        return self.cards.pop()