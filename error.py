"""error.py is the module which controls all the errors messages of the bot
This module was not made to run at its own
"""

import json
import random

with open("errorMessagens.json", 'r') as f:
	errorMessagens = json.load(f)

def commandNotFound(message):
	rand = random.randint(0,len(errorMessagens["command not found"])-1)
	msg  = errorMessagens["command not found"][rand]
	data = "{0}\t".format(rand)
	chat = [[message.channel,msg]]
	return data,chat

# if this is the main module
if __name__ == '__main__':
	#print the documentation
	print(__doc__)