import NpuzzleControle
import NpuzzleHeuristique
import time

class NpuzzleInfosAlgorithm:
	def __init__(self, args):
		self.nbr_de_coup = 0
		self.time_start = time.clock()
		self.time_end = 0
		self.nbropen = 0
		self.greedy = args.greedy
		self.uniform_cost = args.uniform_cost
		self.graph = args.graph
		self.url = args.url

	def end(self):
		if (self.time_end == 0):
			self.time_end = time.clock()
		return self.time_end - self.time_start
