import discord
import basic
import hub
import json

with open('tokenTest.txt','r') as f:
	TOKEN = f.read()

client = discord.Client()

@client.event
async def on_message(message):

	# we do not want the bor to reply to itself
	if message.author == client.user:
		return

	data = basic.headline(message)
	chat = []
	dat = msg = ''
	if message.content.startswith('?'):
		dat,msg = hub.commands(message)
	data += dat
	chat += msg
	for msg in chat:	
		await client.send_message(msg[0],msg[1].format(message))
	basic.log(data)


@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')

client.run(TOKEN)