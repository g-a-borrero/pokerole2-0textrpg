import re

from pokedex import pokedex as pdex
from pokemon import Pokemon as pkmn
from command_parser import parse_command

game = True
current_room = 0

while game:
	game, current_room = parse_command(input("> "), current_room)
