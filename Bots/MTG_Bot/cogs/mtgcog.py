from mtgsdk import Card, Set, Type, Subtype, Supertype
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import os
import asyncio
import random
import time
from mtgcard import MTGCard, MTGList
import datetime

thisfolder = os.path.abspath(os.path.dirname(__file__))
setspath = f"{thisfolder}/sets/"
urlpath = f"{thisfolder}/urls/"

class MTGCog(commands.Cog):
    def __init__(self, client):
        self.urlfile = "urls.txt"
        self.client = client
        self.sets = None
        self.codes = []
        self.cards = []
        self.cardsWrap = []
        self.isLoaded = False
        self.isCards = False
        self.myCard = None
        self.saveList = MTGList()
        self.codenames = []
        self.nameindex = 0
        self.schedOn = False
        self.urls = []
        self.setupVars()
        #self.setupURLs()


    def setupURLs(self):
        if os.path.exists(f"urls/{self.urlfile}"):
            with open(f"urls/{self.urlfile}", "r") as f:
                if not self.urls[0] == None:
                    cpyList = self.urls
                    self.urls = f.readlines()
                    for u in self.urls:
                        if u in cpyList:
                            continue
                        else:
                            self.urls.append(u)
                else:
                    self.urls = f.readliness()
                f.close()


    def saveURLs(self, fname):
        self.urls = []
        for c in self.cardsWrap:
          u = c.imgurl
          if u == None or "":
            continue
          #if u in self.urls:
          #  continue
          self.urls.append(f"{u.strip()}")
        with open(f"{urlpath}{fname}", "w+") as f:
          i = 0
          for u in self.urls:
            f.write(u)
            i += 1
            print(str(i))
          f.close()


    def setupVars(self):
      # Makes url folder if not there
        if not os.path.isdir(urlpath):
          os.mkdir(urlpath)
      # Makes sets folder if not there
        if self.sets == None:
          self.sets = Set.all()
        else:
          print("Sets list is not None")
      # Sets schedSwitch to True
      # Sets self.chan as the General channel in discord server
        self.chan = self.client.get_channel(911721005658038355)
        self.schedOn = True
        


    @commands.command()
    @commands.has_role("Cool Kid")
    async def saveallurls(self, ctx):
      for set in self.sets:
        await ctx.send("One set at a time..", delete_after=20)
        fname = f"{set.code}_URL.fa"
        if os.path.exists(f"{urlpath}{fname}"):
          print(f"{fname} already exists")
          continue
        cur_set = set
        self.allcards = Card.where(language="English").where(set = cur_set.code).all()
        await ctx.send("almost done..", delete_after=2)
        self.cardsWrap = []
        for c in self.allcards:
            wrapped = MTGCard(c)
            self.cardsWrap.append(wrapped)
        self.saveURLs(fname)
        await ctx.send(f"{cur_set.name} has been saved")


    @commands.command()
    async def listsets(self, ctx):
        print("listsets")
        await ctx.send("This will take a second....")
        emb = nextcord.Embed(title="Sets")
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
                emb.add_field(name="MTG", value=f"{st}")
                st = ""
        await ctx.send(embed=emb)


    @commands.command()
    async def choose(self, ctx):
        print("choose")
        for s in self.sets:
            self.codes.append(f"{s.code}")
            self.codenames.append(f"{s.name}")
        await ctx.send("Type in a Set Code:")

        def is_correct(m):
            mesg = str(m.content).upper()
            if mesg not in self.codes:
                print("Not a set code")
                return False
            else:
                self.nameindex = self.codes.index(m.content)
                return m.author == ctx.author

        try:
            msg = await self.client.wait_for('message',check =  is_correct,timeout=30.0)
        except asyncio.TimeoutError:
            return await ctx.send("Sorry, I can't wait forever.")
        await ctx.send("gathering cards....")
        self.cards = Card.where(set=msg.content).where(
            language="English").all()
        for c in self.cards:
            wrapped = MTGCard(c)
            self.cardsWrap.append(wrapped)
        self.isLoaded = True
        self.saveList.addCards(self.cardsWrap)
        await ctx.send(
            f"{self.codenames[self.nameindex]} cards loaded..  Use ..randomCard")


    @commands.command(aliases=["showrandom", "rancard", "random"])
    async def randomCard(self, ctx):
        print("randomCard")
        if self.isLoaded:
            rancard = random.choice(self.cards)
            em = nextcord.Embed(title=rancard.name)
            em.set_footer(text=rancard.id)
            if rancard.image_url == None:
                print(f"{rancard.image_url}")
                rancard.image_url = "https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/f/f8/Magic_card_back.jpg"
            em.set_image(url=rancard.image_url)
        else:
            await ctx.send("No cards are loaded")
        await ctx.send(embed=em)


    @commands.command()
    async def getCard(self, ctx, isDict=False, sched=False):
        print("getCard")
        if self.isLoaded:
            self.myCard = random.choice(self.cardsWrap)
            if sched:
                return
            if isDict == False:
                await ctx.send(str(self.myCard))
            else:
                await ctx.send(f"{self.myCard.getDict}")
                await self.showCard(ctx)


    @commands.command()
    async def showCard(self, ctx):
        print("showCard")
        if self.myCard == None:
            await ctx.send("You have no card yet")
            return
        em = nextcord.Embed(title=f"{self.myCard.name}")
        em.set_image(url=f"{self.myCard.imgurl}")
        await ctx.send(embed=em)


    @commands.command()
    async def saveSet(self, ctx):
        print("saveSet")
        if self.isLoaded:
            self.saveList.saveCards()
            await ctx.send(f"Set file saved")


    @commands.command()
    @commands.has_role("Cool Kid")
    async def loadURLS(self, doWrite = False):
      self.all_urls = []
      for sfile in os.listdir(f"{urlpath}"):
        xx = True
        with open(f"{urlpath}{sfile}", "r") as f:
          while xx:
              line = f.readline()
              if not line:
                  xx = False
              else:
                  self.all_urls.append(line)
          f.close()
        print(str(len(self.all_urls)))
      if doWrite:
        with open("ALL_URLS.FA", "a") as allurls:
          for u in self.all_urls:
            allurls.write(u)
            allurls.write("\n")
          allurls.close()


    @commands.command(aliases=["dlset", "downloadfile", "dlfile"])
    async def downloadset(self, ctx):
        if not self.isLoaded:
            file = self.saveList.defaultFile()
        else:
            file = self.saveList.getFile
        nxfile = nextcord.File(file)
        await ctx.send(file=nxfile)


    @commands.command()
    @commands.has_role("Cool Kid")
    async def schedSwitch(self, ctx):
        if self.schedOn == False:
            self.schedOn = True
            print("Scheduled Message is set to TRUE")
        elif self.schedOn == True:
            self.schedOn = False
            print("Scheduled Message is set to FALSE")


    @commands.command()
    async def HourlyMessage(self, ctx):
        if not self.schedOn:
            await ctx.send("ERROR: schedOn is False. Please set to on.")
        while self.schedOn:
            now = datetime.datetime.now()
            then = now + datetime.timedelta(hours=1)
            wait_time = (then - now).total_seconds()
            await self.schedChoose(ctx)
            await asyncio.sleep(wait_time)


    @commands.command(hidden=True)
    @commands.has_role("Cool Kid")
    async def schedChoose(self, ctx):
        self.cardsWrap = []
        ranset = random.choice(self.sets)
        self.cards = Card.where(set=ranset.code).where(
            language="English").all()
        for c in self.cards:
            wrapped = MTGCard(c)
            self.cardsWrap.append(wrapped)
        self.isLoaded = True
        self.saveList.addCards(self.cardsWrap)
        print(f"{ranset.name} cards loaded.")
        await self.getCard(ctx, sched=True)
        await self.showCard(ctx)


##################################################################
##################################################################


def setup(client):
    pass
    #client.add_cog(MTGCog(client))
