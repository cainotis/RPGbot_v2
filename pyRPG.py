import json

charList = {}

def profile_description():
	"""
	Character Profile
	VIT (HP, tenacity)
	STR (damage, creating)
	DEX (damage, creating)
	INT (damage, creating)
	AGI (actions, hitRate, dodgeRate)
	PER (critRate, hitRate, dodgeRate)
	WeaponMastery (Specific - 100%, Namespace - 90%, Archetype - 75%, Type - 50%, Range - 25%)
		Namespace: Short Sword, Long Sword, Long Bow, ...
		Archetype: Sword, Bow, Mace, ...
		Type: Bashing, Slashing, Piercing, ...
		Range: Melee, Ranged
	MagicalMastery (Conjuration, Transmutation, Apportation)
	ElementalMastery (Specific - 100%, Attribute - 80%, Physical Type - 40%, )
		Attribute: Fire, Water, Lightning, Dark, Light, ...
		Physical Type: Ethereal (Dark, Light, Arcane, ...)
					   Volatile (Fire, Mist, Air, Lightning, ...)
					   Viscous (Water, Lava, Mercury, ...)
					   Solid (Ground, Metal, Rock, ...)
	"""

def main():
	reload_characters()
	menu_start()

def menu_start():
	menu = "exit\nreset list\nreload characters\nprint list\nnew character\ndelete character\nchange stats\nprint character\n"
	print("/help for command list, /exit to quit\n")
	while(True):
		INPUT = input()

		if INPUT == "/help":
			print(menu)

		elif INPUT == "reset list":
			print("Character list reset")
			reset_charList()
			print_list("short")

		elif INPUT == "reload characters":
			reload_characters()
			print("Character list loaded\n")

		elif INPUT == "print list":
			len_in = input("Short or long?\n")
			print_list(len_in)

		elif INPUT == "new character":
			newChar = input("Input name, VIT, STR, DEX, INT, AGI, PER, WpMast, MagMast, EleMast\n").split()
			newCharName = newChar[0]+" "+newChar[1]
			if len(newChar) != 11:
				print("Invalid number of information\n")
				continue
			else:
				make_character(newCharName, newChar[2], newChar[3], newChar[4], newChar[5], newChar[6], newChar[7], newChar[8], newChar[9], newChar[10])

		elif INPUT == "delete character":
			charName = input("Input name\n")
			delete_character(charName)

		elif INPUT == "change stats":
			charName = input("Input name\n")
			change_stats(charName)

		elif INPUT == "print character":
			charName = input("Input name\n")
			print_character(charName)

		elif INPUT == "exit":
			print("exiting\n")
			exit()
			
		else:
			print("Invalid command\n")
			continue

def reset_charList():
	charList = open('charList.json', 'w')
	abc = {}
	charList.write(json.dumps(abc))
	charList.close()
	reload_characters()

def reload_characters():
	global charList
	with open('charList.json', 'r') as file:
		charList = json.load(file)

def print_list(length):
	global charList
	reload_characters()
	print("Character count: ", len(charList))
	cont = 1
	if length.lower() == "long":
		for character in charList:
			print("Character", cont, ":", character)
			print("Vit: {0[vit]}\nStr: {0[str]}\nDex: {0[dex]}\nInt: {0[int]}\nAgi: {0[agi]}\nPer: {0[per]}\nWpMast {0[wpmast]}\nMagMast {0[magmast]}\nEleMast {0[elemast]}".format(charList[character]))
			cont += 1
			'''
			print("Vit:", charList['charList'][character]['vit'])
			print("Str:", charList['charList'][character]['str'])
			print("Dex:", charList['charList'][character]['dex'])
			print("Int:", charList['charList'][character]['int'])
			print("Agi:", charList['charList'][character]['agi'])
			print("Per:", charList['charList'][character]['per'])
			print("WpMast:", charList['charList'][character]['wpmast'])
			print("MagMast:", charList['charList'][character]['magmast'])
			print("EleMast:", charList['charList'][character]['elemast'])
			'''
	elif length.lower() == "short":
		for character in charList:
			print("Character", cont, ":", character)
			cont += 1
	else:
		print("invalid print length")
	print()

def make_character(name, VIT, STR, DEX, INT, AGI, PER, WpMast, MagMast, EleMast):
	global charCount
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
		print("Character %s created with success\n" % name)

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

def upload_changes():
	global charList
	tempCharList = open('charList.json', 'w')
	tempCharList.write(json.dumps(charList))
	tempCharList.close()

def scale(var, currectLower, currentUpper, targetLower, targetUpper):
	return targetLower+var*(currentUpper-currentLower)/(targetUpper-targetLower)
	#

main()