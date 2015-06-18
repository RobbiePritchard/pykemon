

class Moves(object):
	def get_move(self,index_of_move):
		filename = 'moves.txt'
		with open(filename, 'r') as f:
			data = f.readlines()[index_of_move]
			data = data.split(',')
			self.number = data[0]
			self.name = data[1]
			self.type = data[2]
			self.kind = data[3]
			self.pp = int(data[4])
			if (data[5]) != 'None':
				self.power = int(data[5])
			else:
				self.power = None
			if (data[6]) != 'None\n':
				self.accuracy = float(data[6])/100
			else:
				self.accuracy = None




	def __init__(self, levelLearned = 0):
		self.number = 0
		self.name = ""
		self.pp = 0
		self.accuracy = 0.0
		self.type = ""
		self.kind = ""
		self.power = 0
		self.levelLearned = levelLearned