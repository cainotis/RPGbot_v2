"""user.py is the module responsible for controlling the users connects to the bot
This module was not made to run at its own

	exist(name): return if the user exists
	gm(name): return if the user is a GM
	start(message): sign up to the bot
"""

import basic
import error

newUser = basic.loadJson("./Data/newUser.json")

users  =  basic.loadJson("./Data/users.json")

posts  =  basic.loadJson("./Messages/user.json")

def exist(name):
	name = str(name)
	if users.get(name) == None:
		return False
	return True

def gm(name):
	name = str(name)
	if users[name]['GM']:
		return True
	return False

def start(message):
	name = str(message.author)
	msg = ''
	dat = ''
	data = ''
	chat = []
	if exist(name):
		data = "old  \t" 
		dat,msg = basic.choose(posts["start"]["old"])
		a = "{0.author.mention}"
		msg = msg.format(a,users[name])
	else :
		data = "new  \t"
		dat,msg = basic.choose(posts["start"]["new"])
		user = newUser
		user["id"] = len(users)
		user["initDate"] = basic.date()
		users.update({name : user})
		users["map"].append(name)
		basic.saveJson("./Data/users.json",users)
	data = "{0}\t".format(dat)
	chat = [[message.channel,msg]]
	return data,chat

def list(message):
	data = '' 
	dat  = ''
	msg  = ''
	data = 'allow\t'
	dat,msg = basic.choose(posts["list"])
	lista = sorted(users)
	lista.remove('map')
	msg += '\n\t'.join(lista)
	data += '{0}\t'.format(dat)
	chat = [[message.channel,msg]]
	return data,chat


# if this is the main module
if __name__ == '__main__':
	#print the documentation
	print(__doc__)