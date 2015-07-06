from pokemon import Pokemon
from moves import Moves
import random


class Battle(object):
    def did_move_hit(self, attacker, attacker_move, defender):

        probability = attacker_move.accuracy * attacker.accuracy / defender.evasion * 100
        if random.randrange(1, 101) <= probability:
            return True
        else:
            print('But the attack missed!')
            return False

    def choose_attack(self, attacker):
        i = 1
        for known_moves in attacker.moves:
            print str(i) + ":", known_moves.name
            i += 1
        choice = int(raw_input('> '))
        choice -= 1
        if attacker.moves[choice].pp > 0:
            self.attacker_move = attacker.moves[choice]
        else:
            print('{} has no PP left'.format(attacker.moves[choice].name))
            self.choose_attack(attacker)

    def damage_delt(self, attacker, attacker_move, defender):
        '''
		((2A/5+2)*B*C)/D)/50)+2)*X)*Y/10)*Z)/255

		A = attacker's Level
		B = attacker's Attack or Special
		C = attack Power
		D = defender's Defense or Special
		X = same-Type attack bonus (1 or 1.5)
		Y = Type modifiers (40, 20, 10, 5, 2.5, or 0)
		Z = a random number between 217 and 255
		'''
        if self.did_move_hit(attacker, attacker_move, defender):
            critical = 1
            if random.randrange(0, 513) <= attacker.baseSpd:
                critical = 2
                print("A Critical Hit!")
            A = attacker.level
            C = attacker_move.power
            if attacker_move.kind == 'Physical':
                B = attacker.Atk
                D = defender.Def
            else:
                B = attacker.SpAtk
                D = defender.SpDef
            X = self.stab_calc(attacker, attacker_move)
            Y = self.type_mod(attacker_move, defender)
            Z = random.randrange(217, 256)
            if C == None:
                print("attack doesn't do damage")
                return 0
            damage = ((((((((2 * A * critical / 5 + 2) * B * C) / D) / 50) + 2) * X) * Y / 10) * Z) / 255
            defender.currentHP -= int(damage)
            if defender.currentHP < 0:
                defender.currentHP = 0


        else:
            return 0

    def stab_calc(self, attacker, attacker_move):
        # if attacker has the same type as the move return 1.5
        #else return 1
        for pkType in attacker.type:
            if pkType == attacker_move.type:
                return 1.5
        return 1


    def type_mod(self, attacker_move, defender):
        typeMatchup = {
            'Fire': [.5, .5, 2, 1, 2, 1, 1, 1, 1, 1, .5, 2, 1, 1, .5],
            'Water': [2, .5, .5, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, .5],
            'Grass': [.5, 2, .5, 1, 1, 1, 1, 1, .5, 2, 2, .5, .5, 1, .5],
            'Electric': [1, 2, .5, .5, 1, 1, 1, 1, 2, 0, 1, 1, 1, 1, .5],
            'Ice': [1, .5, 2, 1, .5, 1, 1, 1, 2, 2, 1, 1, 1, 1, 2],
            'Psychic': [1, 1, 1, 1, 1, .5, 1, 2, 1, 1, 1, 1, 2, 1, 1],
            'Normal': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, .5, 1, 1, 0, 1],
            'Fighting': [1, 1, 1, 1, 2, .5, 2, 1, .5, 1, 2, .5, .5, 0, 1],
            'Flying': [1, 1, 2, .5, 1, 1, 1, 2, 1, 1, .5, 2, 1, 1, 1],
            'Ground': [2, 1, .5, 2, 1, 1, 1, 1, 0, 1, 2, .5, 2, 1, 1],
            'Rock': [2, 1, 1, 1, 2, 1, 1, .5, 2, .5, 1, 2, 1, 1, 1],
            'Bug': [.5, 1, 2, 1, 1, 2, 1, .5, .5, 1, 1, 1, 2, 1, 1],
            'Poison': [1, 1, 2, 1, 1, 1, 1, 1, 1, .5, .5, 2, .5, .5, 1],
            'Ghost': [1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 2, 1],
            'Dragon': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        }

        typeMulti = 1
        for typ in defender.type:
            typeMulti *= (typeMatchup[attacker_move.type][typ])
        return typeMulti * 10

    def __init__(self, pokemon1, pokemon2):
        turn = 0
        pokemonBattling = [pokemon1, pokemon2]

        while pokemon1.currentHP > 0 and pokemon2.currentHP > 0:
            attacker = pokemonBattling[turn%len(pokemonBattling)]
            defender = pokemonBattling[(turn+1)%len(pokemonBattling)]
            print("\n{} choose an attack".format(attacker.name))
            self.choose_attack(attacker)
            self.damage_delt(attacker, self.attacker_move, defender)
            print("")
            print(pokemon1)
            print(pokemon2)
            print("")
            turn += 1
        if pokemon1.currentHP == 0:
            print("{} defeated {}".format(pokemon2.name,pokemon1.name))
            pokemon1.given_ev([pokemon2])
            experinceGained = pokemon1.exp_gain_formula()
            pokemon2.experience += experinceGained
            print("{} gained {} exp".format(pokemon2.name,experinceGained))
            print(pokemon2)
        else:
            print("{} defeated {}".format(pokemon1.name,pokemon2.name))
            pokemon2.given_ev([pokemon1])
            experinceGained = pokemon2.exp_gain_formula()
            pokemon1.experience += experinceGained
            print("{} gained {} exp".format(pokemon1.name,experinceGained))
            print(pokemon1)



class Trainer_Battle(Battle):
    trainer_pokemon = []
    pass


class Wild_Battle(Battle):
    pass
