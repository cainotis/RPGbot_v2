"""help.py is the module which respond to the hello command.
This modulo was not made to run at its own, but it will have a function that will run when this is the main module to update the command list for futures helps
"""

import basic

commands = basic.loadJson('./Messages/commands.json')

def list(message):
	data = ' list\t'
	msg  = "The following commands are available: ```\n"
	for line in commands["common"]:
		msg += '\t{0}\n'.format(line)
	msg += "```"
	chat = [[message.channel,msg]]
	return data,chat

# if this is the main module
if __name__ == '__main__':
	#print the documentation
	print(__doc__)
	#fazer uma função para modificar as coisas do help
