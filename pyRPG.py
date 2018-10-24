import json

charCount = 0
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
	load_characters()
	make_character("testChar", 10, 10, 10, 10, 10, 10, 10, 10, 10)
	#reset_charList()

def reset_charList():
	charList = open('charList.json', 'w')
	charLista = {}
	abc = {'charCount' : 0, 'charList' : charLista}
	charList.write(json.dumps(abc))
	charList.close()
	

def load_characters():
	global charCount
	global charList
	with open('charList.json', 'r') as file:
		charList = json.load(file)
	charCount = charList['charCount']


def print_list():
	global charCount
	global charList
	load_characters()
	print("Character count: ", charCount)
	for character in charList['charList']:
		print(character)
		print("Vit: {0[vit]}\nStr: {0[str]}\nDex: {0[dex]}\nInt: {0[int]}\nAgi: {0[agi]}\nPer: {0[per]}\nWpMast {0[wpmast]}\nMagMast {0[magmast]}\nEleMast {0[elemast]}\n".format(charList['charList'][character]))
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



def make_character(name, VIT, STR, DEX, INT, AGI, PER, WpMast, MagMast, EleMast):
	global charCount
	global charList
	print("Making character", name)
	if name in charList['charList']:
		print("Character already exists")
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
		charList['charList'][name] = stats

		charCount += 1
		charList['charCount'] = charCount

		charListTemp.write(json.dumps(charList))
		charListTemp.close()
		print("Character %s created with success" % name)
		print_list()
	

def scale(var, currectLower, currentUpper, targetLower, targetUpper):
	return targetLower+var*(currentUpper-currentLower)/(targetUpper-targetLower)
	#

main()