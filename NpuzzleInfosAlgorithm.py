import NpuzzleControle
import NpuzzleHeuristique
import time

class NpuzzleInfosAlgorithm:
	def __init__(self):
		self.nbr_de_coup = 0
		self.time_start = time.clock()
		# self.time_end = 0

	def end(self):
		self.time_end = time.clock()
