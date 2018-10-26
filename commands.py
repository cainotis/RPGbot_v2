"""commands.py is the module which control the commands that the bot do. It chose which module respond to every command it receives
"""

import error
import hello
import help
import user

def hub(message):
	text = ' '.join(message.content[1:].lower().split())
	data = ''
	chat = []
	dat = msg = ''
	if text == 'hello':
		data += 'hello\t'
		dat,msg = hello.greeting(message)
	elif text == 'help':
		data += 'help \t'
		dat,msg = help.list(message)
	elif text == 'start':
		data += 'start\t'
		dat,msg = user.start(message)
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

	print(hub(message()))
	#do examples for each command