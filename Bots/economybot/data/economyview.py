import nextcord
from nextcord.ext import commands

####################################################
class Confirm(nextcord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # 
    @nextcord.ui.button(label='Confirm', style=nextcord.ButtonStyle.green)
    async def confirm(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('Confirming', ephemeral=True)
        self.value = True
        self.stop()
    #
    @nextcord.ui.button(label='Cancel', style=nextcord.ButtonStyle.grey)
    async def cancel(self, button: nextcord.ui.Button, interaction: nextcord.Interaction):
        await interaction.response.send_message('Cancelling', ephemeral=True)
        self.value = False
        self.stop()
        
####################################################    
async def ask(ctx, question = "Confirm or Cancel"):
    """Sends the view to channel and returns True if confirmed or False if canceled or timed out"""
    view = Confirm()
    await ctx.send(question, view=view)
#Wait for the View to stop listening for input...
    await view.wait()
    if view.value is None:
        print('Timed out...')
        return False
    elif view.value:
        print('Confirmed...')
        return True
    else:
        print('Cancelled...')
        return False


####################################################
# Defines a custom Select containing colour options
# that the user can choose. The callback function
# of this class is called when the user changes their choice
class Dropdown(nextcord.ui.Select):
    def __init__(self):

        # Set the options that will be presented inside the dropdown
        options = [nextcord.SelectOption(label='Red', description='Your favourite colour is red', emoji='🟥'),nextcord.SelectOption(label='Green', description='Your favourite colour is green', emoji='🟩'), nextcord.SelectOption(label='Blue', description='Your favourite colour is blue', emoji='🟦')]

        # The placeholder is what will be shown when no option is chosen
        # The min and max values indicate we can only pick one of the three options
        # The options parameter defines the dropdown options. We defined this above
        super().__init__(placeholder='Choose your favourite colour...', min_values=1, max_values=1, options=options)

    async def callback(self, interaction: nextcord.Interaction):
        # Use the interaction object to send a response message containing
        # the user's favourite colour or choice. The self object refers to the
        # Select object, and the values attribute gets a list of the user's 
        # selected options. We only want the first one.
        await interaction.response.send_message(f'Your favourite colour is {self.values[0]}')



####################################################
class DropdownView(nextcord.ui.View):
    def __init__(self):
        super().__init__()

        # Adds the dropdown to our view object.
        self.add_item(Dropdown())

####################################################
async def colour(ctx):
    """Sends a message with our dropdown containing colours"""

    # Create the view containing our dropdown
    view = DropdownView()

    # Sending a message containing our view
    await ctx.send('Pick your favourite colour:', view=view)

####################################################
