import json

charList = {}
objList = {}
actList = {}

def upload_changes():
	global charList
	global objList
	global actList
	tempCharList = open('charList.json', 'w')
	tempCharList.write(json.dumps(charList))
	tempCharList.close()
	tempObjList = open('objList.json', 'w')
	tempObjList.write(json.dumps(objList))
	tempObjList.close()
	tempActList = open('actList.json', 'w')
	tempActList.write(json.dumps(actList))
	tempActList.close()

def reset_list(typeof):
	global charList
	global objList
	global actList
	reload_list(typeof)
	if typeof == "character":
		charList = {}
	elif typeof == "object":
		objList['weapon'] = {}
		objList['armor'] = {}
		objList['item'] = {}
	elif typeof in objList:
		objList[typeof] = {}
	elif typeof == "action":
		actList = {}
	else:
		print("Invalid list type - reset\n")
	upload_changes()
	reload_list(typeof)

def reload_list(typeof):
	global charList
	global objList
	global actList
	if typeof == 'character':
		with open('charList.json', 'r') as file:
			charList = json.load(file)
	elif typeof in objList or typeof == 'object':
		with open('objList.json', 'r') as file:
			objList = json.load(file)
	elif typeof == 'action':
		with open('actList.json', 'r') as file:
			actList = json.load(file)
	else:
		print("Invalid list type - reload")

def print_list(typeof, length):
	global charList
	global objList
	global actList
	reload_list(typeof)
	if typeof == 'character':
		print("Character count: ", len(charList))
		cont = 1
		if length.lower() == "long":
			for character in charList:
				print_character(character)
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
						print("\t\tActives: None")
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
					print("\tBase attack: {0[base]}\n\tRange: {0[range]}".format(objList['weapon'][obj]))
				elif typeof == 'armor':
					print("\tBase defense: {0[base]}\n\tCrit reduction: {0[critred]}\n\tSkills:".format(objList['armor'][obj]))
				elif typeof == 'item':
					print("\tItem class: {0[class]}".format(objList['item'][obj]))
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
					print("\t\tActives: None")
				if "description" in objList[typeof][obj]:
					print("\tDescription:", objList[typeof][obj]['description'])
				else:
					print("\tDescription: None")

		elif length.lower() == "short":
			for obj in objList[typeof]:
				print(typeof, end=", ")
		else:
			print("Invalid print length - print")

	elif typeof == 'action':
		print("Action count: ", len(actList))
		for act in actList:
			print(act)
			if length.lower() == "long":
				for actParam in actList[act]:
					if type(actList[act][actParam]) == str:
						print("\t", actParam, ": ", actList[act][actParam])
					else:
						print("\t", actParam)
						for paramSpec in actList[act][actParam]:
							if type(actList[act][actParam][paramSpec]) == str:
								print("\t\t", actParam, ":", actList[act][actParam][paramSpec])
							else:
								print("\t\t", paramSpec, ":", actList[act][actParam][paramSpec])
		if length.lower() != "short" and length.lower() != "long":
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
		totalHP = str(int(VIT)*10) + "/" + str(int(VIT)*10)
		stats = {
			'HP' : totalHP,
			'inventory' : {},
			'skill' : {},
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
		print("HP: {0[HP]}".format(charList[name]))
		print("Items:")
		for item in charList[name]['inventory']:
			print("\t", end="")
			if charList[name]['inventory'][item] == 'equipped':
				print("Equipped: ", end="")
			print(item)
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
			newObj = input("Type in weapon base attack and range: ").lower().split()
			objList['weapon'][name] = {}
			objList['weapon'][name]['base'] = newObj[0]
			objList['weapon'][name]['range'] = newObj[1]
		elif typeof.lower() == 'armor':
			newObj = input("Type in armor base defense and crit reduction: ").lower().split()
			objList['armor'][name] = {}
			objList['armor'][name]['base'] = newObj[0]
			objList['armor'][name]['critred'] = newObj[1]
		elif typeof.lower() == 'item':
			newObj = input("Type in object class: ").lower()
			objList['item'][name] = {}
			objList['item'][name]['class'] = newObj
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
	upload_changes()

def print_object(name):
	global objList
	for obj_type in objList:
		if name in objList[obj_type]:
			print(obj_type, ": ", name)
			if obj_type == 'weapon':
				print("\tBase attack: {0[base]}\n\tRange: {0[range]}".format(objList['weapon'][name]))
			elif obj_type == 'armor':
				print("\tBase defense: {0[base]}\n\tCrit reduction: {0[critred]}\n\tSkills:".format(objList['armor'][name]))
			elif obj_type == 'item':
				print("\tItem class: {0[class]}".format(objList['item'][name]))
			print("\tSkills:")
			if "passive" in objList[obj_type][name]['skills']:
				print("\t\tPassives:")
				for passive in objList[obj_type][name]['skills']['passive']:
					print("\t\t\t", passive, end="")
					print(":", objList[obj_type][name]['skills']['passive'][passive])
			else:
				print("\t\tPassives: None")
			if "active" in objList[obj_type][name]['skills']:
				print("\t\tActives:")
				for active in objList[obj_type][name]['skills']['active']:
					print("\t\t\t", active, end="")
					print(":", objList[obj_type][name]['skills']['active'][active])
			else:
				print("\t\tActives: None")
			if "description" in objList[obj_type][name]:
				print("\tDescription:", objList[obj_type][name]['description'])
			else:
				print("\tDescription: None")
			return
	print("Object not found\n")

def assign_object(obj, player):
	global charList
	global objList
	if player in charList:
		for obj_type in objList:
			if obj in objList[obj_type]:
				charList[player]['inventory'][obj] = 'not equipped'
				upload_changes()
				print(obj_type, obj, "assigned to", player, "with success!\n")
				user_in = input("Equip object? ").lower()
				if user_in == 'yes':
					equip_object(obj, player)
				return
		print("Object not found")
	else:
		print("Player not found")

def equip_object(obj, player):
	global charList
	global objList
	if player in charList:
		for obj_type in objList:
			if obj in objList[obj_type]:
				if charList[player]['inventory'][obj] == 'not equipped':
					charList[player]['inventory'][obj] = 'equipped'
					upload_changes()
					print(obj_type, obj, "equipped to", player, "with success!\n")
				else:
					charList[player]['inventory'][obj] = 'not equipped'
					upload_changes()
					print(obj_type, obj, "unequipped from", player, "with success!\n")
				return
		print("Object not found")
	else:
		print("Player not found")

def delete_object(name):
	global objList
	for obj_type in objList:
		if name in objList[obj_type]:
			print("Deleting object", name, "...\n")
			objList[obj_type].pop(name)
			upload_changes()
			print(obj_type, name, "deleted\n")
			return
	print("Object not found\n")

#Action specific

def new_action():
	global actList
	actName = input("Input name: ")
	actList[actName] = {}
	while(True):
		user_in1 = input("Add in new action parameter? ")
		if user_in1.lower() == 'yes':
			parameterName = input("Type in parameter name: ")
			if parameterName not in actList[actName]:
				actList[actName][parameterName] = {}
			user_in2 = input("Add multiple specifications? ").lower()
			if user_in2 == 'yes':
				while(True):
					user_in3 = input("Add in new specification? ").lower()
					if user_in3 == 'yes':
						parameterSpec = input("Type in specification name: ")
						specValue = input("Type in specification value: ")
						actList[actName][parameterName][parameterSpec] = specValue
					elif user_in3 == 'no':
						break
					else:
						continue
			else:
				parameterSpec = input("Type in parameter value: ")
				actList[actName][parameterName] = parameterSpec
		elif user_in1.lower() == 'no':
			print()
			break
		else:
			continue
	upload_changes()




