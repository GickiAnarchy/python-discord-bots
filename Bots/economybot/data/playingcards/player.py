from .hand import Hand 

class Player():
    """    """
    def __init__(self, dealer = False):
        self.dealer = dealer
        self.phand = Hand()


    @property
    def hand(self):
        return self.phand