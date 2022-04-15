#Class to store the Discord bot private token.
""" MUST BE KEPT SECURE """

class TokenClass():
    def __init__(self):
        #discord token 1st half
        self.dt1 = "OTE0MDU4NjYzNDI0MDU3MzQ0.YaHhdw.hJ"
        #discord token 2nd half
        self.dt2 = "_XdwaNFNG4HLRA3gpTKHC69mI"


    def getToken(self):
        retstr = str(self.dt1 + self.dt2)
        print(retstr)
        return retstr
