from .cards import *
from .deck import *
from .player import Player

import time

class Highcard():
    """    """
    def __init__(self):
        self.deck = Deck()
        self.opponent = Player(dealer = True)
        self.player = Player()

    def deal(self):
        self.deck.createDeck()
        self.opCard = self.deck.drawCard()
        self.plCard = self.deck.drawCard()
        self.opponent.hand.add_card(self.opCard)
        self.player.hand.add_card(self.plCard)
        print("Cards dealt")

    def show(self):
        self.opCard.hidden = False
        print(f"{repr(self.opCard)}")
        self.plCard.hidden = False
        print(f"{repr(self.plCard)}")

    def isWinner(self):
        if self.plCard > self.opCard:
            print("Player wins")
            return True
        else:
            print("Opponent wins")
            return False


###########
hc = Highcard()

hc.deal()
time.sleep(2)
hc.show()
time.sleep(2)
hc.isWinner()
time.sleep(5)