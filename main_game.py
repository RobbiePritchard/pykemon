from pokemon import *
from trainer import Trainer


class Main_game(object):

	def __init__(self):
		self.starter = Pokemon(5)
		self.player = Trainer()
		self.pokemon_team.append(self.starter)
		print("you just got a {}".format(self.starter.name))
