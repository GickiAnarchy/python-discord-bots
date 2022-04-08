#deck.py
from .cards import Card
from .joker_card import Joker
from random import shuffle


class Deck:
    """ Class of 52 Card() to create a full deck."""
    def __init__(self):
        self.cards = []
        self.images = []
        self.shuffled = False

    def createDeck(self):
        for i in range(2, 15):
            for j in range(4):
                crd = Card(j, i)
                self.cards.append(crd)
        self.Shuffle()
        
    def createDeckWithJokers(self):
        self.createDeck()
        redjr = Joker("red")
        blackjr = Joker("black")
        self.cards.append(redj)
        self.cards.append(blackj)
        self.Shuffle()
        
    def Shuffle(self):
        if len(self.cards) == 0:
            return
        shuffle(self.cards)
        self.shuffled = True
        print(f"Shuffling {str(len(self.cards))} cards..")

    def drawCard(self):
        if self.isEmpty:
            return
        pulled = self.cards.pop()
        print(f"Pulled card:\n{pulled}")
        return pulled

    @property
    def isEmpty(self):
        if len(self.cards) >= 1:
            return False
        else:
            return True 

    @property
    def left(self):
        return str(len(self.cards))