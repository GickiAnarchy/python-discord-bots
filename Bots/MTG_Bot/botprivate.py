#Class to store the Discord bot private token.
""" MUST BE KEPT SECURE """

class TokenClass():
    def __init__(self):
        #discord token 1st half
        self.token = "ENTER_TOKEN_HERE"
        
    def getToken(self):
        return self.token
