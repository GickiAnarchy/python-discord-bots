import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
import os
from private import botprivate
from data import bankfunctions, economyview


intents = nextcord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = "..", intents = intents)

toke = botprivate.TokenClass()

@client.command(aliases = ["loadadmin", "la"])
@commands.has_role("Cool Kid")
async def loaddataadmin(ctx):
  client.load_extension("data.dataadmin")
  await ctx.send("dataadmin has been loaded!")

@loaddataadmin.error
async def loaddataadmin_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("`You dont have permissions to run this command.`")
    else:
      await ctx.send(f"There has been an error loading dataadmin")
      print(str(error))

@client.event
async def on_ready():
    c = 1
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            print(f"{c} - {filename}")
            client.load_extension(f"cogs.{filename[:-3]}")
            c += 1
    print("Bot is ready")
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Game("*WIP* Economy Bot -  '..'"))

@client.command()
@commands.has_role("Cool Kid")
async def clr(ctx, amount = 0):
		await ctx.channel.purge(limit=amount)

@clr.error
async def clr_error(ctx, error):
		if isinstance(error, commands.CheckFailure):
			await ctx.send("`You dont have permissions to run this command.`")

@client.command()
@commands.has_role("Cool Kid")
async def testmenu(ctx):
    await economyview.colour(ctx)


#Run the f'n thing!
client.run(toke.getToken())
