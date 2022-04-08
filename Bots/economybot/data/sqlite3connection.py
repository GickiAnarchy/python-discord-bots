import nextcord
from nextcord.ext import commands
import sqlite3


file_name = "data/eco.db"

class DB_Create(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Remove the below code after creating the table !
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

def setup(client):
    client.add_cog(DB_Create(client))