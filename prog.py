import discord
import BCF

with open('tokenTest','r') as f:
	TOKEN = f.read()

client = discord.Client()

@client.event
async def on_message(message):

	# we do not want the bor to reply to itself
	if message.author == client.user:
		return

	data = BCF.headline() + '\t' + str(message.author) + '\t'

	if message.content.startswith('?'):
		

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)