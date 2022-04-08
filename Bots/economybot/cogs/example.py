import nextcord
from nextcord.ext import commands

class ExampleCog(commands.Cog):
    def __init__(self, client):
        self.client = client


def setup(client):
    client.add_cog(ExampleCog(client))