## Magic: The Gathering Discord Bot

>version: 0.4
>GickiAnarchy
>fatheranarchy@programmer.net

**Requirements** *nextcord, mtgsdk*

**Usage:** 
*use '..' before the commands i.e. '..clr 50' or '..choose'
		
**Commands:**
clr <int>
	clears <int> amount of messages in the channel

clrall
	clears all messages in the channel

listsets
	Lists all the codes of all Card Sets. The codes are used in ..choose 

choose
	Asks for the set code after pressing enter. Get the codes from ..listsets

randomCard
	displays a random card from the loaded set

getCard
	displays some text info about a card. This card is held until changed.

showCard
	shows an image the the held card. Shows back of a MTG card if no image is available

saveSet
	Saves a setcode.json locally where the bot is being ran from.

downloadSet
	Bot posts the loaded set in a message as a .json to download

schedSwitch
	Toggles the hourly MTG post
	
HourlyMessage
	Posts card information once an hour if schedSwitch is True.





