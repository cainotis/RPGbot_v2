import discord
import BCF
import commands
import json

with open('tokenTest.txt','r') as f:
	TOKEN = f.read()

client = discord.Client()

@client.event
async def on_message(message):

	# we do not want the bor to reply to itself
	if message.author == client.user:
		return

	data = BCF.headline() + '\t' + str(message.author) + '\t'
	chat = []
	dat = msg = ''
	if message.content.startswith('?'):
		dat,msg = commands.hub(message)
	data += dat
	chat += msg
	for msg in chat:	
		await client.send_message(msg[0],msg[1].format(message))
	BCF.log(data)


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)