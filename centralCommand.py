

def hub(message):
	text = ' '.join(message.content[1:].lower().split())
	if text == 'help':
		pass

if __name__ == '__main__':

	class message:
		def __init__(self):
			self.content = "?HElP"

	aux = message()

	hub(aux)