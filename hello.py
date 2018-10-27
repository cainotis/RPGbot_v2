"""hello.py is the module which responds to the hello command.
This module was not made to run at its own
"""

import basic

helloList = basic.loadJson('./Messages/hello.json')

def greeting(message):
	dat,msg = basic.choose(helloList)
	data = "{0}\t".format(dat)
	chat = [[message.channel,msg]]
	return data,chat

# if this is the main module
if __name__ == '__main__':
	#print the documentation
	print(__doc__)