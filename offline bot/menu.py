import list_handling

def menu_start():
	boot_type = input("Reset?\n")
	if boot_type == 'yes':
		list_handling.reset_list('character')
		list_handling.reset_list('object')
	list_handling.reload_list('character')
	list_handling.reload_list('object')
	menu = "help\nexit\nreset list\nreload list\nprint list\nnew character\ndelete character\nchange stats\nprint character\nnew object\n"
	print("help for command list, exit to quit\n")
	while(True):
		INPUT = input()

		if INPUT == "help":
			print(menu)

		elif INPUT == "reset list":
			type_in = input("Character, object, weapon, armor?\n").lower()
			list_handling.reset_list(type_in)
			list_handling.print_list(type_in, "short")

		elif INPUT == "reload list":
			type_in = input("Character, object?\n").lower()
			list_handling.reload_list(type_in)
			print(type_in, "list loaded\n")

		elif INPUT == "print list":
			type_in = input("Character, object, weapon, armor?\n").lower()
			len_in = input("Short or long?\n")
			list_handling.print_list(type_in, len_in)

		elif INPUT == "new character":
			newChar = input("Input name, VIT, STR, DEX, INT, AGI, PER, WpMast, MagMast, EleMast\n").split()
			newCharName = newChar[0]+" "+newChar[1]
			if len(newChar) != 11:
				print("Invalid number of information\n")
				continue
			else:
				list_handling.new_character(newCharName, newChar[2], newChar[3], newChar[4], newChar[5], newChar[6], newChar[7], newChar[8], newChar[9], newChar[10])

		elif INPUT == "delete character":
			charName = input("Input name\n")
			list_handling.delete_character(charName)

		elif INPUT == "change stats":
			charName = input("Input name\n")
			list_handling.change_stats(charName)

		elif INPUT == "print character":
			charName = input("Input name\n")
			list_handling.print_character(charName)

		elif INPUT == "new object":
			type_in = input("Type of object: ")
			list_handling.new_object(type_in)

		elif INPUT == "exit":
			print("exiting\n")
			exit()
			
		else:
			print("Invalid command\n")
			continue
