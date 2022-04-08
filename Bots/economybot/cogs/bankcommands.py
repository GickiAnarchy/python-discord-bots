import nextcord
import datetime
from nextcord.ext import commands
from data import bankfunctions, economyview


class BankCommands(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["bal", "check", "chkbal"])
    @commands.guild_only()
    async def balance(self, ctx):
        self.user = ctx.author
        await bankfunctions.open_bank(self.user)
        users = await bankfunctions.get_bank_data(self.user)
        self.wallet_amt = users[1]
        self.bank_amt = users[2]
        self.net_amt = int(self.wallet_amt + self.bank_amt)
        em = nextcord.Embed(
            title=f"{self.user.name}'s Balance",
            description=f"Wallet: {self.wallet_amt}\nBank: {self.bank_amt}",
            color=nextcord.Color(0x00FF00),
        )
        await ctx.send(embed=em)

    @commands.command(aliases=["update$", "addmoney", "winmoney", "losemoney"])
    @commands.guild_only()
    async def updatemoney(self, ctx, amount=0, mode="wallet"):
        await bankfunctions.update_bank(ctx.author, amount, mode)
        await ctx.send(f"${amount} has been updated")

    @commands.command(aliases=["with"])
    @commands.guild_only()
    async def withdraw(self, ctx, amount=None):
        user = ctx.author
        await bankfunctions.open_bank(user)
        users = await bankfunctions.get_bank_data(user)
        bank_amt = users[2]
        if amount.isdigit():
            amount = int(amount)
        else:
            if amount.lower() == "all" or amount.lower() == "max":
                await bankfunctions.update_bank(user, +1 * bank_amt)
                await bankfunctions.update_bank(user, -1 * bank_amt, "bank")
                await ctx.send(f"{user.mention} you withdrew {bank_amt} in your wallet")
                return
        if amount > bank_amt:
            await ctx.send(f"{user.mention} You don't have that enough money!")
            return
        if amount < 0:
            await ctx.send(f"{user.mention} enter a valid amount !")
            return
        await bankfunctions.update_bank(user, +1 * amount)
        await bankfunctions.update_bank(user, -1 * amount, "bank")
        await ctx.send(f"{user.mention} you withdrew **{amount}** from your **Bank!**")

    @commands.command(aliases=["dep"])
    @commands.guild_only()
    async def deposit(self, ctx, amount=None):
        self.user = ctx.author
        await bankfunctions.open_bank(self.user)
        self.users = await bankfunctions.get_bank_data(self.user)
        self.wallet_amt = self.users[1]
        if amount.isdigit():
            self.amount = int(amount)
        else:
            if amount.lower() == "all" or amount.lower() == "max":
                await bankfunctions.update_bank(self.user, -1 * self.wallet_amt)
                await bankfunctions.update_bank(self.user, +1 * self.wallet_amt, "bank")
                await ctx.send(f"{self.user.mention} deposits ${self.wallet_amt} in the bank")
                return
        if self.amount > self.wallet_amt:
            await ctx.send(f"{self.user.mention} You don't have that enough money!")
            return
        if self.amount < 0:
            await ctx.send(f"{self.user.mention} enter a valid amount !")
            return
        await bankfunctions.update_bank(self.user, -1 * self.amount)
        await bankfunctions.update_bank(self.user, +1 * self.amount, "bank")
        await ctx.send(f"{self.user.mention} deposited ${self.amount} to the bank.")

    @commands.command()
    @commands.has_role("Cool Kid")
    async def freemoney(self, ctx, amount=100):
        self.user = ctx.author
        self.amount = int(amount)
        self.resp = await economyview.ask(ctx)
        if self.resp == True:
            await bankfunctions.update_bank(self.user, self.amount)
            await ctx.send(f"{self.user.mention} just found ${self.amount}")
    
    
def setup(client):
    client.add_cog(BankCommands(client))


"""
	@commands.command()
    @commands.has_role("Cool Kid")
    async def freemoney(self, ctx, amount=100):
		self.user = ctx.author
        self.amount = int(amount)
        self.resp = await economyview.ask(ctx)
        if self.resp == True:
			await bankfunctions.update_bank(self.user, self.amount)
	    	await ctx.send(f"{self.user.mention} just found ${self.amount}")


    @commands.command(aliases=["leader", "lb"])
    @commands.guild_only()
    async def leaderboard(self, ctx):
        self.users = await bankfunctions.get_lb()
        self.data = []
        self.index = 1
        for member in self.users:
            if self.index > 10:
                break
            self.member_name = self.client.get_user(member[0])
            self.member_amt = member[1]
            if self.index == 1:
                self.msg1 = f"**🥇 `{self.member_name}` -- {self.member_amt}**"
                self.data.append(self.msg1)
            if self.index == 2:
                self.msg2 = f"**🥈 `{self.member_name}` -- {self.member_amt}**"
                self.data.append(self.msg2)
            if self.index == 3:
                self.msg3 = f"**🥉 `{self.member_name}` -- {self.member_amt}**\n"
                self.data.append(self.msg3)
            if self.index >= 4:
				self.members = f"**{self.index} `{self.member_name}` -- {self.member_amt}**"
				self.data.append(self.members)
            self.index += 1
        msg = "\n".join(self.data)
    	em = nextcord.Embed(
    		title=f"Top {self.index - 1} Richest Users - Leaderboard",
    		description=f"It's Based on Net Worth (wallet + bank) of Global Users\n\n{msg}",
    		color=nextcord.Color(0x00FF00),
    		timestamp=datetime.datetime.utcnow()
    	)
    	em.set_footer(text=f"GLOBAL - {ctx.guild.name}")
        await ctx.send(embed=em)
"""
