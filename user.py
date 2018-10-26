"""user.py is the module responsible for controlling the users connects to the bot
This module was not made to run at its own
"""

import basic

newUser = basic.loadJson("./Data/newUser.json")

users  =  basic.loadJson("./Data/users.json")

init  =  basic.loadJson("./Messages/start.json")

def start(message):
	name = str(message.author)
	msg = ''
	dat = ''
	data = ''
	chat = []
	if users.get(name) == None:
		data = "new  \t"
		dat,msg = basic.chooseText(init["new"])
		user = newUser
		user["id"] = len(users)
		user["initDate"] = basic.date()
		users.update({name : user})
		users["map"].append(name)
		basic.saveJson("./Data/users.json",users)
	else :
		data = "old  \t" 
		dat,msg = basic.chooseText(init["old"])
		a = "{0.author.mention}"
		msg = msg.format(a,users[name])
	data = "{0}\t".format(dat)
	chat = [[message.channel,msg]]
	return data,chat

# if this is the main module
if __name__ == '__main__':
	#print the documentation
	print(__doc__)

	print(init)
	print(users)