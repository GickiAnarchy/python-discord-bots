#cards.py
import os
import random


thisfolder = os.path.abspath(os.path.dirname(__file__))
class CardImages():
    def __init__(self):
        self.imageLinks = {}
        self.links = []
        self.titles = []
        with open(f"{thisfolder}/imageLinks.txt") as f:
            for x in f.readline():
                if "http" in x:
                    self.links.append(x)
                else:
                    self.titles.append(x)
        if len(self.links) == len(self.titles):
            leg = len(self.titles)
            while leg >= 0:
                self.imageLinks[self.titles.pop()] = {f"{self.links.pop()}"}

    @property
    def imgDict(self):
        return self.imageLinks
            
cimages = CardImages()


class Card():
    """Single playing card class"""

    back = r"https://images2.imgbox.com/b4/9f/gZwyMGpy_o.png"
    
    suits = ["spades", "hearts", "diamonds", "clubs"]

    values = [None, None,"2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]

    def __init__(self, s, v, hidden = True):
        """suit + value are ints"""
        self.value = v
        self.suit = s
        self.name = f"{self.suits[self.suit]}_{self.values[self.value]}"
        self.hidden = hidden
        self.image = None


    def __lt__(self, c2):
        """Handles the 'less than' operator (<)"""
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
        else:
            return False
        return False

    def __gt__(self, c2):
        """Handles the 'greater than' operator (>)"""
        if self.value > c2.value:
            return True
        if self.value == c2.value:
         if self.suit > c2.suit:
            return True
        else:
            return False
        return False

    def __repr__(self):
        """Returns a string format of the object"""
        v = self.values[self.value] +\
        " of " + \
        self.suits[self.suit]
        return v

    def getImage(self):
        listFile = open(f"{thisfolder}/imageLinks.txt", "r")
        listlist = listFile.readlines()
        iii = 0
        for cx in listlist:
            print(str(iii))
            if self.name in cx:
                self.image = listlist.pop(iii + 1)
            if not cx:
                print("NOOOOOOOOOOOOOOO")
                self.image = self.back
                return
            iii += 1
        print(self.image)
            
            
        
    def Image(self):
        self.getImage()
        return f"{self.image}"
    
    @property
    def backUrl(self):
        return self.back
