from command_parser import parse_command

game = True
current_room = 0

print("Let's journey through the world of Pokemon!")
while game:
	game, current_room = parse_command(input("> "), current_room)
