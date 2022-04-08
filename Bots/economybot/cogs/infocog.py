import nextcord
from nextcord.ext import commands
import os
import random
from data import bankfunctions
from private import botprivate
from nextcord import Interaction, SlashOption

gID = botprivate.AMLATL_ID

class InfoCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    
    @nextcord.slash_command(guild_ids=[gID], description="AMLATL Basic Information")
    async def information(self, interaction: nextcord.Interaction):
        await interaction.response.send_message("This is a slash command in a cog!")
    


def setup(bot):
    bot.add_cog(InfoCog(bot))