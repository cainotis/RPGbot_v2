"""help.py is the module which respond to the hello command.
This modulo was not made to run at its own

	list(message) : it return the list of commands
"""

import basic
import user

commands = basic.loadJson('./Messages/commands.json')

posts = basic.loadJson('./Messages/help.json')

def list(message):
	data = 'list \t'
	dat,msg  = basic.choose(posts['list']['common'])
	data += '{0}\t'.format(dat)
	msg += "```\n"
	for line in commands["common"]:
		msg += '\t{0}\n'.format(line)
	msg += "```\n"
	if user.exist(message.author):
		data += "user \t"
		if message.server:
			data += 'server\t'
			dat,aux = basic.choose(posts['list']['server'])
			msg += aux
			data += '{0}\t'.format(dat)
		else :
			data += 'private\t'
			dat,aux = basic.choose(posts['list']['private'])
			msg += aux
			data += '{0}\t'.format(dat)
			msg += " ```\n"
			for line in commands["private"]:
				msg += '\t{0}\n'.format(line)
			msg += " ```\n"
			if user.gm(message.author):
				data += 'GM\t'
				dat,aux = basic.choose(posts['list']['GM'])
				msg += aux
				data += '{0}\t'.format(dat)
				msg += " ```\n"
				for line in commands["GM"]:
					msg += '\t{0}\n'.format(line)
				msg += " ```\n"
	else :
		data += 'Nuser\t'

	chat = [[message.channel,msg]]
	return data,chat

def exist(command):
	if command in commands["command"]:
		return True
	return False

# if this is the main module
if __name__ == '__main__':
	#print the documentation
	print(__doc__)
