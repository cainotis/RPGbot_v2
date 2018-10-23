"""help.py is the module which respond to the hello command.
This modulo was not made to work at its own, but it will have a function that will run when this is the main module to update the command list for futures helps
"""

import json

with open('commands.json','r') as f:
	commands = json.load(f)

def list(message):
	data = 'list\t'
	msg  = "The following commands are available: ```\n"
	for key in commands:
		msg += '\t' + key + ": " + commands[key ] + '\n'
	msg += "```"
	chat = [[message.channel,msg]]
	return data,chat

# if this is the main module
if __name__ == '__main__':
	#print the documentation
	print(__doc__)
	#fazer uma função para modificar as coisas do help
