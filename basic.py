
"""basic.py is the module which was the basics control functions which are functions that help the control and the maintenance the bots made with this system
	
	date() : make the date format for the log
	log() : save the data to the datalog.txt
	loadJson(file) : load and return an json file
	saveJson(file,data) : load to a json file the data

Examples:
"""

import json
import time
import random

def date():
	t = time.localtime()
	data = str(t[0])+'/'+str(t[1])+'/'+str(t[2])+' '
	if t[3]<10:
		data += '0'
	data += str(t[3])+':'
	if t[4]<10:
		data += '0'
	data += str(t[4])+':'
	if t[5]<10:
		data +='0'
	data += str(t[5])+'\t'
	return data

def log(data):
	with open('./Data/datalog','a') as f:
		f.write(data + '\n')
	return

def loadJson(file):
	with open(file,'r') as f:
		return json.load(f)

def saveJson(file,data):
	with open(file,'w') as f:
		f.write(json.dumps(data))
	return

def chooseText(array):
	rand = random.randint(0,len(array)-1)
	return rand,array[rand]

# if this is the main module
if __name__ == '__main__':
	# print the documentation
	print(__doc__)
	# and the examples 
	print('\tdate() :', date())