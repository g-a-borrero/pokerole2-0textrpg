import re

def parse_command(user_command, current_room):
	if user_command.lower() in ["quit", "qq", "q", "close", "exit"]:
		return [False, current_room]
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
			print("You are looking at %s." % (look_target))
		return [True, current_room]