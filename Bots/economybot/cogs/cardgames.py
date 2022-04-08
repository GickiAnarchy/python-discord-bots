import nextcord
import random
from nextcord.ext import commands
from data import bankfunctions
from data.playingcards import Card,Deck
import asyncio


class CardGames(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def backcard(self, ctx):
        self.c = Card(2,5)
        em = nextcord.Embed(title = "CARD BACK")
        em.set_image(url= f"{self.c.back}")
        await ctx.send(embed = em)

    @commands.command()
    @commands.guild_only()
    async def highcard(self, ctx):
        self.player = ctx.author
        await bankfunctions.open_bank(self.player)
        users = await bankfunctions.get_bank_data(self.player)
        self.wallet_amt = users[1]
        await ctx.send(f"How much do you want to wager?  Max:${self.wallet_amt}")

        def is_correct(m):
            return m.author == ctx.author and m.content.isdigit()

        try:
            msg = await self.client.wait_for('message', check=is_correct, timeout=10.0)
        except asyncio.TimeoutError:
            return await ctx.send("Sorry, I can't wait forever.")
            
        self.deck = Deck()
        self.deck.createDeck()
        self.wager = int(msg.content)    
        self.com = self.deck.drawCard()
        self.card = self.deck.drawCard()
        winningpot = self.wager * 1.5
        self.strresult = ""

        if self.wager > self.wallet_amt:
            await ctx.send(f"You can't afford ${str(self.wager)}")
            return

        if self.card > self.com:
            print(f"{self.player} won")
            await bankfunctions.update_bank(self.player, winningpot)
            self.strresult =f"{self.player} won"
        else:
            print(f"{self.player} lost")
            await bankfunctions.update_bank(self.player, -int(self.wager))
            self.strresult =f"{self.player} lost"

        em = nextcord.Embed(title = "High Card Results")
        userImg = self.card.Image()
        print(f"{userImg}")
        em2 = nextcord.Embed(title = "Your Card")
        em2.set_image(url = f"{userImg}")
        em.add_field(name = "Card to beat", value = f"{repr(self.com)}", inline = True)
        em.add_field(name = "Your card", value = f"{repr(self.card)}", inline = True)
        em.set_footer(text = f"{self.strresult}")
        
        await ctx.send(embed = em)
        await ctx.send(embed = em2)





def setup(client):
    client.add_cog(CardGames(client))
