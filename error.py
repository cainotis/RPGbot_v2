"""error.py is the module which controls all the errors messages of the bot
This module was not made to run at its own

	commandNotFound(message): print the error message when the command was not found

"""

import basic

errorMessagens = basic.loadJson("./Messages/error.json")

def commandNotFound(message):
	dat,msg  = basic.choose(errorMessagens["command not found"])
	data = "{0}\t".format(dat)
	chat = [[message.channel,msg]]
	return data,chat

# if this is the main module
if __name__ == '__main__':
	#print the documentation
	print(__doc__)