import json

charList = {}
objList = {}

def upload_changes():
	global charList
	global objList
	tempCharList = open('charList.json', 'w')
	tempCharList.write(json.dumps(charList))
	tempCharList.close()
	tempObjList = open('objList.json', 'w')
	tempObjList.write(json.dumps(objList))
	tempObjList.close()

def reset_list(typeof):
	global charList
	global objList
	if typeof == "character":
		tempCharList = open('charList.json', 'w')
		reset = {}
		tempCharList.write(json.dumps(reset))
		tempCharList.close()
		reload_list(typeof)
	elif typeof == "object":
		tempObjList = open('objList.json', 'w')
		reset = {}
		reset['weapon'] = {}
		reset['armor'] = {}
		tempObjList.write(json.dumps(reset))
		tempObjList.close()
		reload_list(typeof)
	elif typeof in objList:
		reload_list(typeof)
		tempObjList = open('objList.json', 'w')
		objList[typeof] = {}
		tempObjList.write(json.dumps(objList))
		tempObjList.close()
		reload_list(typeof)
	else:
		print("Invalid list type - reset\n")

def reload_list(typeof):
	global charList
	global objList
	if typeof == 'character':
		with open('charList.json', 'r') as file:
			charList = json.load(file)
	elif typeof in objList or typeof == 'object':
		with open('objList.json', 'r') as file:
			objList = json.load(file)
	else:
		print("Invalid list type - reload")

def print_list(typeof, length):
	global charList
	global objList
	reload_list(typeof)
	if typeof == 'character':
		print("Character count: ", len(charList))
		cont = 1
		if length.lower() == "long":
			for character in charList:
				print("Character", cont, ":", character)
				print("Vit: {0[vit]}\nStr: {0[str]}\nDex: {0[dex]}\nInt: {0[int]}\nAgi: {0[agi]}\nPer: {0[per]}\nWpMast {0[wpmast]}\nMagMast {0[magmast]}\nEleMast {0[elemast]}".format(charList[character]))
				cont += 1
		elif length.lower() == "short":
			for character in charList:
				print("Character", cont, ":", character)
				cont += 1
		else:
			print("Invalid print length - print")

	elif typeof == 'object':
		for obj_type in objList:
			print(obj_type, "count: ", len(objList[obj_type]))
			if length.lower() == "long":
				for obj in objList[obj_type]:
					print(obj)
					if obj_type == 'weapon':
						print("\tBase attack: {0[base]}\n\tRange: {0[range]}".format(objList['weapon'][obj]))
					elif obj_type == 'armor':
						print("\tBase defense: {0[base]}\n\tCrit reduction: {0[critred]}\n\tSkills:".format(objList['armor'][obj]))
					print("\tSkills:")
					if "passive" in objList[obj_type][obj]['skills']:
						print("\t\tPassives:")
						for passive in objList[obj_type][obj]['skills']['passive']:
							print("\t\t\t", passive, end="")
							print(":", objList[obj_type][obj]['skills']['passive'][passive])
					else:
						print("\t\tPassives: None")
					if "active" in objList[obj_type][obj]['skills']:
						print("\t\tActives:")
						for active in objList[obj_type][obj]['skills']['active']:
							print("\t\t\t", active, end="")
							print(":", objList[obj_type][obj]['skills']['active'][active])
					else:
						print("\t\tActives: None\n")
					if "description" in objList[obj_type][obj]:
						print("\tDescription:", objList[obj_type][obj]['description'])
					else:
						print("\tDescription: None")

			elif length.lower() == "short":
				for obj in objList[obj_type]:
					print(obj_type, end=", ")
			else:
				print("Invalid print length - print")

	elif typeof in objList:
		print(typeof, "count: ", len(objList[typeof]))
		if length.lower() == "long":
			for obj in objList[typeof]:
				print(obj)
				if typeof == 'weapon':
					print("\tBase attack: {0[base]}\n\tRange: {0[range]}\n".format(objList['weapon'][obj]))
				elif typeof == 'armor':
					print("\tBase defense: {0[base]}\n\tCrit reduction: {0[critred]}\n\tSkills:".format(objList['armor'][obj]))
				print("\tSkills:")
				if "passive" in objList[typeof][obj]['skills']:
					print("\t\tPassives:")
					for passive in objList[typeof][obj]['skills']['passive']:
						print("\t\t\t", passive, end="")
						print(":", objList[typeof][obj]['skills']['passive'][passive])
				else:
					print("\t\tPassives: None")
				if "active" in objList[typeof][obj]['skills']:
					print("\t\tActives:")
					for active in objList[typeof][obj]['skills']['active']:
						print("\t\t\t", active, end="")
						print(":", objList[typeof][obj]['skills']['active'][active])
				else:
					print("\t\tActives: None\n")
				if "description" in objList[typeof][obj]:
					print("\tDescription:", objList[typeof][obj]['description'])
				else:
					print("\tDescription: None")

		elif length.lower() == "short":
			for obj in objList[typeof]:
				print(typeof, end=", ")
		else:
			print("Invalid print length - print")
	else:
		print("Invalid list type - print")
	print()

#Character specific

def new_character(name, VIT, STR, DEX, INT, AGI, PER, WpMast, MagMast, EleMast):
	global charList
	print("Making character", name, "...")
	if name in charList:
		print("Character already exists\n")
		print_list()
	else:
		charListTemp = open('charList.json', 'w')
		stats = {
			'vit' : VIT,
			'str' : STR,
			'dex' : DEX,
			'int' : INT,
			'agi' : AGI,
			'per' : PER,
			'wpmast' : WpMast,
			'magmast' : MagMast,
			'elemast' : EleMast
		}
		charList[name] = stats
		charListTemp.write(json.dumps(charList))
		charListTemp.close()
		print("Character %s created with success!\n" % name)

def print_character(name):
	global charList
	if name in charList:
		print("Name:", name)
		print("Vit: {0[vit]}\nStr: {0[str]}\nDex: {0[dex]}\nInt: {0[int]}\nAgi: {0[agi]}\nPer: {0[per]}\nWpMast {0[wpmast]}\nMagMast {0[magmast]}\nEleMast {0[elemast]}".format(charList[name]))
	else:
		print("Character not found")
	print()

def change_stats(name):
	global charList
	if name in charList:
		print("Changing", name, end="")
		statChange = input(". Input stat to change and amount:\n").split()
		for i in range(0, len(statChange), 2):
			statChange[i] = statChange[i].lower()
			tempStat = int(charList[name][statChange[i]]) + int(statChange[i+1])
			charList[name][statChange[i]] = tempStat
			upload_changes()
		print("Done")
	else:
		print("Character not found")
	print()

def delete_character(name):
	global charList
	if name in charList:
		print("Deleting character", name, "...\n")
		charList.pop(name)
		upload_changes()
		print("Character", name, "deleted\n")
	else:
		print("Character not found")

#Object specific

def new_object(typeof):
	global objList
	newObj = {}
	name = input("Input object name: ")
	if typeof.lower() in objList:
		if typeof.lower() == 'weapon':
			newObj = input("Type in weapon base attack and range:\n").lower().split()
			objList['weapon'][name] = {}
			objList['weapon'][name]['base'] = newObj[0]
			objList['weapon'][name]['range'] = newObj[1]
		elif typeof.lower() == 'armor':
			newObj = input("Type in armor base defense and crit reduction:\n").lower().split()
			objList['armor'][name] = {}
			objList['armor'][name]['base'] = newObj[0]
			objList['armor'][name]['critred'] = newObj[1]
		objList[typeof][name]['skills'] = {}
		while(True):
			user_in = input("Add skill?\n")
			if user_in.lower() == "yes":
				user_in = input("Passive or active?\n").lower()
				tempSkill = input("Type in skill name:\n")
				if user_in == "passive" or user_in == "active":
					if user_in not in objList[typeof][name]['skills']:
						objList[typeof][name]['skills'][user_in] = {}
					skillDescription = input("Type in skill description:\n")
					objList[typeof][name]['skills'][user_in][tempSkill] = skillDescription
			else:
				break
		user_in = input("Add description?\n")
		if user_in.lower() == "yes":
			description = input("Type in description:\n")
			objList[typeof][name]['description'] = description
		print(typeof, name, "created with success!\n")

	else:
		print("Invalid object type\n")
	print(objList)
	upload_changes()
