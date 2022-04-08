from mtgsdk import Card, Set, Type

class MTGCard():
    def __init__(self, card: Card):
        self.card = card
        self.cardImage = card.image_url
        self.name = card.name
        self.set = card.set_name
        self.setcode = card.set
        self.text = card.text
        self.release_date = card.release_date
        self.power = card.power
        self.toughness = card.toughness
        self.colors = card.colors
        self.color_id = card.color_identity
        self.type = card.type
        self.rarity = card.rarity


    @property
    def name(self):
        return self.name
    
    @property
    def set(self):
        return self.set
    
    @property
    def type(self):
        return self.type
    
    @property
    def text(self):
        return self.text
    
    @property
    def colors(self):
        return self.colors