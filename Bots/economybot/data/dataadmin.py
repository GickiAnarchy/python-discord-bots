import nextcord
from nextcord.ext import commands
import sqlite3


file_name = "data/eco.db"

class DB_Create(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command(name = "create_table", aliases = ["ct", "maketable", "mt"])
    async def create_table(self, ctx):
        self.db = sqlite3.connect(r"data/eco.db")
        self.cursor = self.db.cursor()
        self.cols = ["wallet", "bank"] # You can add as many as columns in this !!!
        self.cursor.execute("""CREATE TABLE economy(userID BIGINT)""")
        self.db.commit()
        for col in self.cols:
            self.cursor.execute(f"ALTER TABLE economy ADD COLUMN {col}")
        self.db.commit()
        self.cursor.close()
        self.db.close()
        await ctx.send("Table created successfully !")
    # Remove the above code after creating the table !


    @commands.command()
    async def drop_bank(self, ctx):
        self.db = sqlite3.connect(file_name)
        self.cursor = self.db.cursor()
        self.cursor.execute("""DELETE FROM economy""")
        self.db.commit()
        self.db.close()
        await ctx.send("Economy Data has been deleted!!")
        

    @commands.command(aliases = ["ct_roulette"])
    async def create_table_roulette(self, ctx):
        self.db = sqlite3.connect(file_name)
        self.cursor = self.db.cursor()
        self.cols = ["RollHistory"] # You can add as many as columns in this !!!
        self.cursor.execute("""CREATE TABLE roulette(userID BIGINT)""")
        self.db.commit()
        for col in self.cols:
            self.cursor.execute(f"ALTER TABLE roulette ADD COLUMN {col}")
        self.db.commit()
        self.cursor.close()
        self.db.close()
        await ctx.send("Table created successfully !")


    @commands.command()
    async def unloadcog(self, ctx):
        self.client.unload_extension("data.dataadmin")
        print("Unloaded DataAdmin Cog")


def setup(client):
    client.add_cog(DB_Create(client))