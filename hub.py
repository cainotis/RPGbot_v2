"""commands.py is the module which control the commands that the bot do. It chose which module respond to every command it receives
"""

import error
import hello
import command
import user

def commands(message):
	text = ' '.join(message.content[1:].lower().split())
	data = ''
	chat = []
	dat = msg = ''
	if text == 'hello':
		data += 'hello\t'
		dat,msg = hello.greeting(message)
	elif text == 'help':
		data += 'help \t'
		dat,msg = command.list(message)
	elif text == 'start':
		data += 'start\t'
		dat,msg = user.start(message)
	#### if the message is not on server and the user exist
	elif (not message.server) and user.exist(message.author):
		if user.gm(message.author):
			if text == 'list users':
				data += 'list \t'
				dat,msg = user.list(message)
			else :
				data += 'NfoundGM\t'
				dat,msg = error.commandNotFound(message)
		else :
			if command.exist(text):
				data += 'denied\t'
			else :
				data += 'not found\t'
			dat,msg = error.commandNotFound(message)
	else :
		if command.exist(text):
			data += 'denied\t'
		else :
			data += 'not found\t'
		dat,msg = error.commandNotFound(message)
	data += dat
	chat += msg
	return data,chat

if __name__ == '__main__':

	print(__doc__)

	class message:
		def __init__(self):
			self.content = '?start'
			self.channel = 'channel'
			self.author  = 'author'
			self.server  = 'server'

	#print(hub(message()))
	#do examples for each command