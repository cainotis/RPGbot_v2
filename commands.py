
import help

def hub(message):
	text = ' '.join(message.content[1:].lower().split())
	data = ''
	chat = []
	dat = msg = ''
	if text == 'help':
		data += 'help\t'
		dat,msg = help.list(message)
	data += dat
	chat += msg
	return data,chat

if __name__ == '__main__':

	print(__doc__)

	class message:
		def __init__(self):
			self.content = '?HElP'
			self.channel = 'channel'
			self.author  = 'author'
			self.server  = 'server'

	print(hub(message()))