from mtgsdk import Card, Set, Type, Subtype, Supertype
import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import os
import botprivate
import asyncio
import time
import random
import json


intents = nextcord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = "..", intents = intents)

token = botprivate.TokenClass()

thisfolder = os.path.abspath(os.path.dirname(__file__))
setspath = f"{thisfolder}/sets/"
sets = Set.all()
print("sets....CHECK")
nmt = []
cards = []
setcodes = []
setn = ""


@client.event
async def on_ready():
#     c = 1
#     for filename in os.listdir("./cogs"):
#         if filename.endswith(".py"):
#             print(f"{c} - {filename}")
#             client.load_extension(f"cogs.{filename[:-3]}")
#             c += 1
     print("Bot is ready")
     await client.change_presence(status=nextcord.Status.online, activity=nextcord.Game("Magic: The Gathering Card Bot"))


@client.command()
async def randomCard(ctx):
        if len(cards) <= 0:
            await ctx.send("Choose a card set first... \"..choose\"")
        nm = random.choice(cards)
        em = nextcord.Embed(title = nm.name)
        em.set_footer(text = nm.id)
        if nm.image_url == None:
            print(f"{nm.image_url}")
            nm.image_url = "https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/f/f8/Magic_card_back.jpg"
        em.set_image(url = nm.image_url)
        await ctx.send(embed = em)


@client.command()
async def choose(ctx):
    refc = None
    for s in sets:
        setcodes.append(f"{s.code}")
    def is_correct(m):
            if m not in setcodes:
                print("Not a set code")
                #return False
            return m.author == ctx.author
    try:
        msg = await client.wait_for('message', check=is_correct, timeout=30.0)
    except asyncio.TimeoutError:
        return await ctx.send("Sorry, I can't wait forever.")
    await ctx.send("gathering cards....")
    setn = f"{msg.content}"
    cd =Card.where(set = msg.content).where(language = "English").all()
    for c in cd:
        cards.append(c)
    refc = random.choice(cards)
    print(f"{type(cards)} -- {len(cards)}")
    await ctx.send(f"{refc.set_name} set cards loaded..  Use ..randomCard")
    setn = refc.set_name


@client.command()
async def listsets(ctx):
    await ctx.send("This will take a second....")
    emb = nextcord.Embed(title = "Sets")
    st = ""
    x = 1
    for s in sets:
        a = st
        co = f"{s.code}"
       # na = f"{s.name}"
        b = "{}".format(co)
        st = "  --  ".join([a, b])
        x += 1
        if len(sets) < 40:
            x = len(sets) - 40
        elif x == 40:
            x = 1
            emb.add_field(name = "MTG", value = f"{st}")
            st = ""
    await ctx.send(embed = emb)
    

@client.command()
async def saveset(ctx):
    with open(f"{cards[0].set}.json", "w") as f:
        for c in cards:
            f.write(c)
        f.close()

"""
@client.command(aliases = ["addcards", "newset"])
async def newcards(ctx):
    loadCards()
    await ctx.send("More cards added to the MTG card pool")

def loadCards():
    n = Card.where(setName = sets.pop().name).where(language = "English").all()
    for c in n:
        nmt.append(c)
    print(f"Cards list .... CHECK\n{len(nmt)} total cards.")

@client.command()
async def randomCard(ctx):
    nm = random.choice(nmt)
    em = nextcord.Embed(title = nm.name)
    em.set_footer(text = nm.id)
    if nm.image_url == None:
        nm.image_url = "https://static.wikia.nocookie.net/mtgsalvation_gamepedia/images/f/f8/Magic_card_back.jpg"
    em.set_image(url = nm.image_url)
    await ctx.send(embed = em)
"""    

#Run the f'n thing!
client.run(token.getToken())