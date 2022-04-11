#Code by GickiAnarchy
# fatheranarchy@programmer.net

from mtgsdk import Card, Set, Type
import json
import io
import os

set_folder = os.path.abspath(os.path.join(os.path.dirname(__file__),".", "Sets"))

class MTGCard():
    def __init__(self, card):
        self.original = card
        self.cardImage = card.image_url
        self.cardname = card.name
        self.cardset = card.set_name
        self.setcode = card.set
        self.cardtext = card.text
        self.release_date = card.release_date
        self.power = card.power
        self.toughness = card.toughness
        self.cardcolors = card.colors
        self.color_id = card.color_identity
        self.cardtype = card.type
        self.rarity = card.rarity
        self.str_props = []
        self.checkProps()


    @property
    def getDict(self):
        d = vars(self.original)
        return d

    @property
    def original_card(self):
        return self.original

    @property
    def imgurl(self):
    	return self.cardImage

    @property
    def name(self):
        return self.cardname
    
    @property
    def code(self):
        return self.setcode
    
    @property
    def set(self):
        return self.cardset
    
    @property
    def type(self):
        return self.cardtype
    
    @property
    def text(self):
        return self.cardtext
    
    @property
    def colors(self):
        return self.cardcolors


    def checkProps(self):        
        orig_props = [self.cardname, self.cardset, self.setcode, self.power, self.toughness, self.color_id, self.cardcolors, self.cardtype, self.rarity, self.release_date, self.cardtext]
        for p in orig_props:
            try:
                s = "{}".format(p)
                self.str_props.append(s)
            except:
                print("Error in MTGCard Properties")
                self.str_props.append("ERROR")
        if self.cardImage == None:
        	self.cardImage = "https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/f/f8/Magic_card_back.jpg"
        
    
    def __repr__(self):
        """Return formatted string of this object"""
        cardStr = "Name:        {}\nSet:    {} -- {}\n#/#    {}/{}\nColor:    {} -- {}\nType:    {}\nRarity:    {}\nRelease Date:    {}\n\n{}".format(self.str_props[0], self.str_props[1], self.str_props[2], self.str_props[3], self.str_props[4], self.str_props[5], self.str_props[6], self.str_props[7], self.str_props[8], self.str_props[9], self.str_props[10])
        return cardStr


#######################################################
#######################################################
#######################################################
class MTGList:
    def __init__(self):
        if not os.path.isdir(set_folder):
            os.mkdir(set_folder)        
        self.mtg_dict = {}
        self.filename = ""
        self.setsfile = ""
       

    
    @property
    def getFile(self):
        if os.path.exists(f"{self.setsfile}"):
            return self.setsfile

    def defaultFile(self):
        return f"{set_folder}/UGL.json"


    def addCards(self, cards):
        self.filename = f"{cards[0].code}.json" 
        for c in cards:
            self.mtg_dict[f"{c.name}"] = c.getDict
    
    
    def saveCards(self):
        with open(f"{set_folder}/{self.filename}", "w") as f:
            json.dump(self.mtg_dict, f, indent = 4)
            f.close
        self.setsfile = f"{set_folder}/{self.filename}"


#######################################################
#######################################################
#######################################################
