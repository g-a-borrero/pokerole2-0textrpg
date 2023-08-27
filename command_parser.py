import re
from pokemon import Pokemon
from rooms import rooms

def parse_command(user_command, current_room):
	if user_command.lower() in ["quit", "qq", "q", "close", "exit"]:
		return [False, current_room]
	elif current_room == 0:
		return char_creation()
	else:
		commands = user_command.split(" ")
		main_command = commands[0].lower()
		if len(commands) > 1:
			second_command = commands[1].lower()
			if len(commands) > 2:
				third_command = commands[2].lower()
		if main_command in ["say", "speak", "ask", "inquire"]:
			endstr = ""
			if commands[-1][-1] not in [".", "?", "!"]:
				endstr = "." if main_command not in ["ask", "inquire"] else "?"
			if second_command in ["to", "of"]:
				talk_target = third_command
				# check for presence of talk target
				# if talk target is here...
				talk_str = "You %s %s %s, \"%s%s\"" % (main_command, second_command, talk_target, " ".join(commands[3:]).capitalize(), endstr)
			else:
				talk_str = "You %s, \"%s%s\"" % (main_command, " ".join(commands[1:]).capitalize(), endstr)
			print(talk_str)
		elif main_command in ["look", "observe"]:
			try:
				look_target = third_command
			except:
				try:
					look_target = second_command
				except:
					look_target = "room"
			#change me
			if look_target == "room":
				room_str = "| " + rooms[rooms["ID"]==current_room]["Short Description"].values[0] + " |"
				print("+" + "-"*(len(room_str)-2) + "+")
				print(room_str)
				print("+" + "-"*(len(room_str)-2) + "+")
				print(rooms[rooms["ID"]==current_room]["Long Description"].values[0])
			else:
				print("You are looking at %s." % (look_target))
		return [True, current_room]

def char_creation():
	player_name = input("What's your name?\n> ")
	print("That's a wonderful name! It's great to meet you, %s." % (player_name[:player_name.index(" ")] if " " in player_name else player_name))
	player_age = int(input("Tell me, how old are you? Please select your age from 8 to 100.\n> "))
	print("You're just starting out, so your rank is that of a Starter.")
	player_nature = input("How would you describe your nature? Adamant, Bashful, Bold, Brave, Calm, Careful, Docile, Gentle, Hardy, Hasty, Impish, Jolly, Lax, Lonely, Mild, Modest, Naive, Naughty, Quiet, Quirky, Rash, Relaxed, Sassy, Serious, Timid?\n> ")
	print("Aah, I see.")
	player = Pokemon("Human", name=player_name, rank="Starter", age=player_age, nature=player_nature, rand=True)
	print("So you're a %s Starter trainer, age %d, named %s. Your journey starts now!" % (player.nature_, player.age, player.name))
	return [True, 1]
