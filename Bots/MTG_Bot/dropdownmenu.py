import nextcord
from mtgsdk import Card, Set, Type, Subtype, Supertype
from nextcord.ext import commands


class Dropdown(nextcord.ui.Select):
    def __init__(self, sets):
        self.sets = sets
        options = []
        for s in self.sets:
            options.append(nextcord.SelectOption(label=f"{s.code}", description=f"{s.name}"))
            
        super().__init__(placeholder="Choose a card set...",  min_values=1, max_values=1, options = options)

    async def callback(self, interaction: nextcord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's 
        # selected options. We only want the first one.
        return f"{self.values[0]}"


class DropdownView(nextcord.ui.View):
    def __init__(self, sets):
        super().__init__()
        # Adds the dropdown to our view object.
        self.add_item(Dropdown(sets))

#####################################
"""
    @staticmethod
    def loadSet(set):
        n = Card.where(set = set).where(language = "English").all()
        self.setcards = n
        print(f"Cards list .... CHECK\n{len(nmt)} total cards.")
    


@bot.command()
async def colour(ctx):
    # Create the view containing our dropdown
    view = DropdownView()

    # Sending a message containing our view
    await ctx.send('Pick your favourite colour:', view=view)
"""

