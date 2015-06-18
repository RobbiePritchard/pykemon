from pokemon import *
from trainer import Trainer


class Main_game(object):
	def choose_starter(self):
		print('1. Bulbasaur\n2. Charmander\n3. Squirtle')
		start = int(input('Choose a Starter: '))
		if start == 1:
			self.starter = Pokemon(pokemonNumber = 0)
		if start == 2:
			self.starter = Pokemon(pokemonNumber = 3)
			print(self.starter.name)
		if start == 3:
			self.starter = Pokemon(pokemonNumber = 6)

	def __init__(self):
		self.pokemon_team = []
		self.choose_starter()
		self.player = Trainer()
		self.pokemon_team.append(self.starter)
		print("you just got a {}".format(self.starter.name))
