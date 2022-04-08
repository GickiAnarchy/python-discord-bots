from mtgsdk import Card, Set, Type, Subtype, Supertype
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import os
import asyncio
import time
import random
from mtgcard import MTGCard, MTGList



thisfolder = os.path.abspath(os.path.dirname(__file__))
setspath = f"{thisfolder}/sets/"


class MTGCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.sets = []
        self.codes = []
        self.cards = []
        self.cardsWrap = []
        self.isLoaded = False
        self.isCards = False
        self.myCard = None
        self.saveList = MTGList()
        



    @commands.command()
    async def listsets(self, ctx):
        print("listsets")
        await ctx.send("This will take a second....")
        self.sets = Set.all()
        emb = nextcord.Embed(title = "Sets")
        st = ""
        x = 1
        for s in self.sets:
            a = st
            co = f"{s.code}"
            b = "{}".format(co)
            st = "  --  ".join([a, b])
            x += 1
            if len(self.sets) < 50:
                x = len(self.sets) - 50
            elif x == 50:
                x = 1
                emb.add_field(name = "MTG", value = f"{st}")
                st = ""
        await ctx.send(embed = emb)

                
    @commands.command()
    async def choose(self, ctx):
        print("choose")
        for s in self.sets:
            self.codes.append(f"{s.code}")
        await ctx.send("Type in a Set Code:")
        def is_correct(m):
                if str(m.content) not in self.codes:
                    print("Not a set code")
                    return False
                return m.author == ctx.author
        try:
            msg = await self.client.wait_for('message', check=is_correct, timeout=30.0)
        except asyncio.TimeoutError:
            return await ctx.send("Sorry, I can't wait forever.")
        await ctx.send("gathering cards....")
        self.cards = Card.where(set = msg.content).where(language = "English").all()        
        for c in self.cards:
            wrapped = MTGCard(c)
            self.cardsWrap.append(wrapped)
        self.isLoaded = True
        self.saveList.addCards(self.cardsWrap)
        await ctx.send(f"{self.cards[0].set} cards loaded..  Use ..randomCard")


    @commands.command(aliases = ["showrandom", "rancard", "random"])
    async def randomCard(self, ctx):
        print("randomCard")
        if self.isLoaded:
            rancard = random.choice(cards)
            em = nextcord.Embed(title = rancard.name)
            em.set_footer(text = rancard.id)            
            if rancard.image_url == None:
                print(f"{rancard.image_url}")
                rancard.image_url = "https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/f/f8/Magic_card_back.jpg"                
            em.set_image(url = rancard.image_url)
        else:
            await ctx.send("No cards are loaded")
        await ctx.send(embed = em)


    @commands.command()
    async def getCard(self, ctx, isDict = False):
        print("getCard")
        if self.isLoaded:
            self.myCard = random.choice(self.cardsWrap)
            if isDict == False:
                await ctx.send(str(self.myCard))
            else:
                await ctx.send(f"{self.myCard.getDict}")


    @commands.command()
    async def showCard(self, ctx):
        print("showCard")
        if self.myCard == None:
            await ctx.send("You have no card yet")
            return
        em = nextcord.Embed(title = f"{self.myCard.name}")
        em.set_image(url = f"{self.myCard.imgurl}")
        await ctx.send(embed = em)


    @commands.command()
    async def saveSet(self, ctx):
        print("saveSet")
        if self.isLoaded:
            self.saveList.saveCards()
            await  ctx.send(f"Set file saved")

##################################################################
##################################################################

def setup(client):
    client.add_cog(MTGCog(client))


