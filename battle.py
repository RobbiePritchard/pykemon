from pokemon import Pokemon


class Battle(object):

	#((2A/5+2)*B*C)/D)/50)+2)*X)*Y/10)*Z)/255

	# A = attacker's Level
	# B = attacker's Attack or Special
	# C = attack Power
	# D = defender's Defense or Special
	# X = same-Type attack bonus (1 or 1.5)
	# Y = Type modifiers (40, 20, 10, 5, 2.5, or 0)
	# Z = a random number between 217 and 255


	def damage_delt(attacker, attacker_move, defender):
		attacker = Pokemon()
		defender = Pokemon()
		part_1 = (attacker.level * 2/5)+ 2
		#--------
		# TODO
		#--------
		# if attack is a physical move use Atk/Def
		# if attack is a special move use SpAtk/SpDef

		part_2 = (part_1 * attacker.Atk)*attacker_move.power/ defender.Def
		part_3 = ()
	def __init__(self):
		pass

class Trainer_Battle(Battle):
	trainer_pokemon = []
	pass
class Wild_Battle(Battle):
	pass
