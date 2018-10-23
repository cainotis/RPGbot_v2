"""hello.py is the module which responds to the hello command.
This modulo was not made to work at its own
"""

import json
import random

with open('hello.json','r') as f:
	helloList = json.load(f)

def greeting(message):
	data = 'list\t'
	rand = random.randint(0,len(helloList)-1)
	msg  = helloList[rand]
	chat = [[message.channel,msg]]
	return data,chat

# if this is the main module
if __name__ == '__main__':
	#print the documentation
	print(__doc__)