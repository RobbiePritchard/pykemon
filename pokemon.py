#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import random
import math


from moves import Moves


class Pokemon(object):
	level = 0
	wild_or_trainer = 1
	current_ev = 0
	firstTime = True
	def exp_gain_formula(self):
		'''
		Calculates and returns the experience gained after defeating a pokemon
		'''
		#wild_or_trainer
		# 1 if the fainted Pokémon is wild
		# 1.5 if the fainted Pokémon is owned by a Trainer
		wild_or_trainer = self.wild_or_trainer

		#original_Trainer
		#1 if the winning Pokémon's current owner is its Original Trainer
		#1.5 if the Pokémon was gained in a domestic trade
		original_Trainer = 1

		#Lucky_egg
		#1.5 if the winning Pokémon is holding a Lucky Egg
		#1 otherwise.
		Lucky_egg = 1

		#exp_all
		#If Exp. All is not in the player's Bag...
			#The number of Pokémon that participated in the battle and have not fainted
		#If Exp. All is in the player's Bag...
			#Twice the number of Pokémon that participated and have not fainted, when calculating the experience of a Pokémon that participated in battle
			#Twice the number of Pokémon that participated and have not fainted times the number of Pokémon in the player's party, when calculating the experience given by Exp. All
		exp_all = 1
		self.firstTime = False
		return int((wild_or_trainer * original_Trainer * self.baseExperience * Lucky_egg * self.level) / (7 * exp_all))

	def given_ev(self, victorious_Pokemon):
		"""
		Takes one argument, victorious_Pokemon, victorious_Pokemon 
		is an array of pokemon that did damage to the current Pokemon(self)
		Calculates the evs gained for defeating current pokemon(self)
		Adds the added evs to the victorious Pokemon
		"""
		max = 25600
		for pok in victorious_Pokemon:
			if pok.current_ev < 25600:
				pok.evHp += self.baseHP
				pok.evAtk += self.baseAtk
				pok.evDef += self.baseDef
				pok.evSpAtk += self.baseSpAtk
				pok.evSpDef += self.baseSpDef
				pok.evSpd += self.baseSpd
				total = self.baseHP + self.baseAtk + self.baseDef + self.baseSpAtk + self.baseSpDef + self.baseSpd
				pok.current_ev += total

	def Update_Stats(self):
		"""
		updates the stats of the current pokemon
		"""
		self.hp = self.calculate_stat(self.ivHP, self.baseHP, self.evHp, self.level, True)
		self.Atk = self.calculate_stat(self.ivAtk, self.baseAtk, self.evAtk, self.level, False)
		self.Def = self.calculate_stat(self.ivDef, self.baseDef, self.evDef, self.level, False)
		self.SpAtk = self.calculate_stat(self.ivSpAtk, self.baseSpAtk, self.evSpAtk, self.level, False)
		self.SpDef = self.calculate_stat(self.ivSpDef, self.baseSpDef, self.evSpDef, self.level, False)
		self.Spd = self.calculate_stat(self.ivSpd, self.baseSpd, self.evSpd, self.level, False)
		self.currentHP = self.hp

	#from pokemon_data.txt set up a new pokemon with all the base stats
	def calculate_stat(self, iv, base, ev, level, is_HP):
		"""
		Takes 5 Arguments:
		iv is the iv value of the stat
		base is the base value of the stat
		ev is the current ev value of the stat
		level is the current level of the pokemon
		is_HP is a boolean, true if the stat being calculated is hp
		Calculates and returns the new stat
		"""
		if is_HP:
			return int( (((iv + base + ( math.sqrt(ev) / 8 )) * level) / 50) + 10)
		else:
			return int( (((iv + base + ( math.sqrt(ev) / 8 )) * level) / 50) + 5)

	def random_pokemon(self,pokemonNumber):
		"""
		Loads a random pokemon from pokemon_data.txt 
		"""
		try:
			filename = 'pokemon_data.txt'

			with open(filename, 'r') as f:
				data = f.readlines()[pokemonNumber]
				#choose a random pokemon from the pokemon_data
				# choice_data = random.choice(data)
				# split_data = choice_data.split('-')

				split_data = data.split('-')
				self.number = int(split_data[0])
				self.name = split_data[1]
				self.type = []
				if ',' in split_data[2]:
					pktype = split_data[2].split(',')
					for t in pktype:
						self.type.append(self.get_type_number(t))
				else:
					self.type.append(self.get_type_number(split_data[2]))

				self.baseHP = int(split_data[3])
				self.ivHP = random.randrange(0, 16)

				self.baseAtk = int(split_data[4])
				self.ivAtk = random.randrange(0, 16)

				self.baseDef = int(split_data[5])
				self.ivDef = random.randrange(0, 16)


				self.baseSpAtk = int(split_data[6])
				self.ivSpAtk = random.randrange(0, 16)


				self.baseSpDef = int(split_data[7])
				self.ivSpDef = random.randrange(0, 16)

				self.baseSpd = int(split_data[8])
				self.ivSpd = random.randrange(0, 16)

				self.Update_Stats()
				self.baseExperience = int(split_data[9])
				self.accuracy = 1.0
				self.evasion = 1.0


				learned_moves = split_data[10].split(',')
				self.moves_can_be_learned = {}
				for move in learned_moves:
					move = move.split('/')
					level_learned = int(move[0])
					move_learned = Moves()
					move_learned.get_move(int(move[1]))
					self.moves_can_be_learned[level_learned] = move_learned
				# male = print('\x0b') --> ♂
				# female = print('\x0c') --> ♀
				self.gender = random.choice(['Male','Female'])
				if self.gender == 'Male':
					self.genderSymbol = '♂'
				else:
					self.genderSymbol = '♀'
				self.give_moves()

				self.owner = None
				self.heldItem = None


		except (OSError, IOError) as e:
			print('Couldnt find {}'.format(filename))

	def give_moves(self):
		for key in self.moves_can_be_learned.keys():
			if key < self.level:
				self.moves_to_be_learned.append(self.moves_can_be_learned[key])
				del self.moves_can_be_learned[key]
		while len(self.moves) < 4 and len(self.moves_to_be_learned) > 0 :
			self.moves.append(self.moves_to_be_learned.pop())
		if len(self.moves) == 4 and len(self.moves_to_be_learned) > 0 and not self.firstTime:
			print('{} cannot learn more than 4'.format(self.name))
			self.change_moves(self.moves_to_be_learned.pop())
	
	def change_moves(self,move):
		name = raw_input('Trying to learn {} but cant learn more than 4 moves\nwould you like to delete a move to make room for {}: (y)es (n)o '.format(move.name,move.name))
		if name == 'y':
			i = 1
			for known_moves in self.moves:
  				print str(i) + ":", known_moves.name
  				i += 1
  			name = int(raw_input('Which move would you like to swap for {}: '.format(move.name)))
  			if name in range(1,5):
  				forgot = self.moves[name-1]
  				sure = raw_input('Are you sure you want to forget {} and learn {}? '.format(forgot.name,move.name))
  				if sure == 'y':
  					self.moves.pop(name-1)
  					self.moves.insert(name-1, move)
  					print('{} forgot {} and learned {}'.format(self.name,forgot.name,move.name))
  				else:
  					print('move was not learned')

		elif name == 'n':
			name = raw_input('Are you sure? (y)es (n)o ')
			if name == 'y':
				return
			else:
				self.change_moves

	def level_up(self):
		"""
		Changes the level of a pokemon
		"""
		#level cannot be higher than 100
		if self.level <= 100:
			self.level += 1
			print('{} has grown to level {}'.format(self.name,self.level))
			self.experience = 0
			self.Update_Stats()
			self.give_moves()

	def get_type_number(self,typeName):
		typetoNumber = {
		'Normal' : 6,
		'Fighting' : 7,
		'Flying' : 8,
		'Ground' : 9,
		'Rock' : 10,
		'Bug' : 11,
		'Poison' : 12,
		'Ghost' : 13,
		'Dragon' : 14,
		'Fire' : 0,
		'Water' : 1,
		'Grass' : 2,
		'Electric' : 3,
		'Ice' : 4,
		'Psychic' : 5
		}
		return typetoNumber[typeName]
	
	def __init__(self, level = 5,pokemonNumber = 0):
		# When initiailizing a pokemon all Wild Pokemon stats have a value of 0
		self.moves = []
		self.moves_to_be_learned = []
		self.level = level
		self.evHp = 0
		self.evAtk = 0
		self.evDef = 0
		self.evSpAtk = 0
		self.evSpDef = 0
		self.evSpd = 0
		self.experience = 0
		self.random_pokemon(pokemonNumber)

	def  __str__(self):
		return "{}\tHP:{}/{}\tEXP:{}".format(self.name,self.currentHP,self.hp,self.experience)

class WildPokemon(Pokemon):
	wild_or_trainer = 1


class TrainerPokemon(Pokemon):
	wild_or_trainer = 1.5


