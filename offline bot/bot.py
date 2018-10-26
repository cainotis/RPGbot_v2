import list_handling
import menu

menu.menu_start()

def profile_description():
	"""
	Character Profile
	VIT (HP, tenacity)
	STR (damage, creating)
	DEX (damage, creating)
	INT (damage, creating)
	AGI (offensive actions, defensive actions, hitRate, dodgeRate)
	PER (defensive actions, critRate, hitRate, dodgeRate)
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

