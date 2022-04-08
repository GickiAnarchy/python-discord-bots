import nextcord
import random
from nextcord.ext import commands
from data import bankfunctions

class BasicGames(commands.Cog):
    def __init__(self, client):
        self.client = client
        

    @commands.command(aliases = ["flip", "cf"], description = "Coin <amount to bet> <'Heads' or 'Tails'>")
    @commands.guild_only()
    async def coin(self, ctx, bet = 0, coincall = "heads"):
        """ Flips a coin.
            Coin <amount to bet> <'Heads' or 'Tails'>
        Args:
            ctx (_type_): Context of the command usage
            bet (int, optional): _description_. Defaults to 0.
            coincall (str, optional): _description_. Defaults to "heads".
        """
        # Lists of valid inputs
        headsList = ["heads", "h", "head"]
        tailsList = ["tails", "t", "tail"]
        
        # Initialize variables
        self.user = ctx.author
        pick = coincall.lower()
        
        # Check if user can cover the bet
        ca = await bankfunctions.canAfford(self.user, bet)
        if ca == False:
            await ctx.send(f"You can't afford ${str(bet)}!")
            return
        
        # Check user heads/tails input
        if pick in headsList:
            pick = "heads"
        elif pick in tailsList:
            pick = "tails"
        else:
            print(f"{str(pick)} isn't recognized. Please choose 'heads' or 'tails'.")
            return        
        
        # Flip the coin -- 'Randomly choose heads or tails'.
        seq = ["heads", "tails"]
        ran = random.choice(seq)
        print(f"{str(ran)}")
        
        # Check against users guess and payout
        if str(ran) == pick:
            await bankfunctions.update_bank(self.user, bet)
            print(f"{self.user.name} won.")
        else:
            await bankfunctions.update_bank(self.user, bet)
            print(f"{self.user.name} lost.")



def setup(client):
    client.add_cog(BasicGames(client))