import nextcord
from nextcord.ext import commands
import os
import random
from data import bankfunctions


class BasicInteraction(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases=["rob", "lick"])
    @commands.guild_only()
    async def steal(self, ctx, victim: nextcord.User):
        self.user = ctx.author
        # memberconverter = commands.MemberConverter()
        # try:
        #     member = await memberconverter.convert(ctx, victim)
        # except commands.MemberNotFound:
        #     pass
        # else:
        self.victim = victim
        victim_account = await bankfunctions.get_bank_data(self.victim)
        target_wallet = victim_account[1]
        user_account = await bankfunctions.get_bank_data(self.user)
        user_wallet = user_account[1]
            
            #print(type(victim_account))
            # await ctx.send(f"Wallet: ${victim_account[1]} --- Bank: ${victim_account[2]}")
            # print("Tested steal command")
            
        schance = random.randint(1, 100)
		
        half_of_total = target_wallet/2
        quarter_of_total = target_wallet/4
        user_loss_amount = floor((13/user_wallet) * 100)
        
        print(f"user_loss_amount: {str(user_loss_amount)}")
        
        low_level = random.randint(1, half_of_total)
        high_level = random.randint((half_of_total + quarter_of_total), target_wallet)            

        # User ends up losing money
        if schance < 20:
            print("<20")
            await bankfunctions.update_bank(self.user, -user_loss_amount)
            await ctx.send(f"{self.user.name} tried to rob {self.victim.name} and lost ${str(user_loss_total)} in the process!")
        # User is not successful in the robbery attempt
        elif schance < 68:
            print("<68")
            await ctx.send(f"{self.user.name} tried to rob {self.victim.name} and failed!!")
        # User was successful at the robbery
        elif schance < 95:
            print("<95")
            await bankfunctions.update_bank(self.victim, -low_level)
            await bankfunctions.update_bank(self.user, low_level)
            await ctx.send(f"{self.user.name} stole ${str(low_level)} from {self.victim.mention}")
        # User robs the victim for ALOT
        elif schance <= 100:
            print("<=100")
            await bankfunctions.update_bank(self.victim, -high_level)
            await bankfunctions.update_bank(self.user, high_level)
            await ctx.send(f"{self.user.name} stole ${str(high_level)} from {self.victim.mention}")
        else:
            print(str(schance))

    @steal.error
    async def steal_error(self, ctx, error: commands.CommandError):
        # if the conversion above fails for any reason, it will raise `commands.BadArgument`
        # so we handle this in this error handler:
        if isinstance(error, commands.BadArgument):
            return await ctx.send('Couldn\'t find that user.')


    @commands.command(aliases=["donate", "charity"])
    @commands.guild_only()
    async def givecash(self, ctx, target: nextcord.User, amount = 0):
        self.user = ctx.author
        self.user_account = await bankfunctions.get_bank_data(self.user)
        self.user_wallet = self.user_account[1]
        self.target= target
        if self.target == None:
            self.target = ctx.author
        else:
            self.target_account = await bankfunctions.get_bank_data(self.target)
            self.target_wallet = self.target_account[1]

        if self.user == self.target:
            await ctx.send("Uhhh, wtf are you tryimg to do?/nAnyways....")
        if self.user_wallet < int(amount):
            await ctx.send("You do not have that much money to give away!")
            return
        if int(amount) < 0:
            await ctx.send("Invalid amount. Can't give a negative amoint!")
            return

        await bankfunctions.update_bank(self.user, -1 * int(amount))
        await bankfunctions.update_bank(self.target, int(amount))
        await ctx.send(f"{self.target.mention} just recieved ${str(amount)} from {self.user.name}.")


def setup(client):
    client.add_cog(BasicInteraction(client))
