
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

if __name__ == '__main__':
	pass
	#fazer uma função para modificar as coisas do help
