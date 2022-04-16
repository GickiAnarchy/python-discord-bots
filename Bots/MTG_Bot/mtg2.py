import nextcord
from nextcord.ext import commands
#from nextcord import Interaction, SlashOption
import os
import botprivate
from webserver import keep_alive

intents = nextcord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="..", intents=intents)
token = botprivate.TokenClass()
cog_folder = os.path.abspath(os.path.join(os.path.dirname(__file__)))


@client.event
async def on_ready():
    c = 1
    for filename in os.listdir(f"{cog_folder}/cogs"):
        if filename.endswith("cog.py"):
            print(f"{c} - {filename}")
            client.load_extension(f"cogs.{filename[:-3]}")
            c += 1
    print("Bot is ready")
    await client.change_presence(status=nextcord.Status.online, activity=nextcord.Game("Magic: The Gathering Card Bot"))
    chan = client.get_channel(911721005658038355)
    await chan.send("I'm back online ", delete_after=120)


@client.command()
async def clrall(ctx):
    await ctx.channel.purge()


@client.command()
async def clr(ctx, amount=0):
    await ctx.channel.purge(limit=amount)


keep_alive()
client.run(token.getToken())
