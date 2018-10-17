import discord

with open('tokenTest','r') as f:
	TOKEN = f.read()

client = discord.Client()

@client.event
async def on_message(message):

	# we do not want the bor to reply to itself
	if message.author == client.user:
		return