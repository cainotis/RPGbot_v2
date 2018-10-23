
"""Basic Control Functions(BFC) is the module which have the functions that help the control and the maintenance of the bots made with this system
	
	headline() : make the date format for the log
	log() : save the data to the datalog.txt

Examples:
"""

import time

def headline():
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
	with open('datalog','a') as f:
		f.write(data + '\n')
	return 

# if this is the main module
if __name__ == '__main__':
	# print the documentation
	print(__doc__)
	# and the examples 
	print('\theadline() :', headline())