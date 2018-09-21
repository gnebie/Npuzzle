import NpuzzleControle
import NpuzzleHeuristique
import copy

ARRAY,HEURISTIC,DAD,DEPTH = 0,1,2,3

def removekey(d, key):
	r = dict(d)
	del r[key]
	return r

class NpuzzleAstar:
	"""NpuzzleAstar class, do the work"""
	def __init__(self, tab, Heuristique, Controle, Info):
		self.linenbr = 0
		self.linenbrmax = 0
		self.lines = []
		self.listsort = []
		self.Co = Controle
		self.He = Heuristique
		self.Info = Info

	def reconstruct_path(self, current):
		total_path = [current]
		while current[DAD] != 0:
			# print(current[HEURISTIC])
			current = current[DAD]
			total_path.append(current)
		# print(total_path)
		return total_path

	# format = {hash: [tab, heu, *father, depth]}
	def Astar(self, start, goal):
		closedSet = {}
		openSet = {self.get_hash(start): [start, self.He.get_heuristique_all_map(start), 0, 0]}
		last = [0, 100000, 0, 0]
		nbropen = len(openSet)
		# print("\n")
		#
		# print(openSet)
		while len(openSet) != 0:
			if (len(openSet) > nbropen):
				nbropen = len(openSet)
			# print('\n')
			# print("openSet: ", openSet)
			# print('\n')
			# print("closedSet: ", closedSet)
			current = openSet[self.gScore_get_lower(openSet)]
			if current[ARRAY] == goal:
				self.Info.nbropen = nbropen;
				self.Info.totalopen = len(openSet) + len(closedSet)
				return self.reconstruct_path(current)
			if (current[HEURISTIC] > last[HEURISTIC]) and not self.Info.greedy:
				newSet = {}
				while (len(openSet)):
					none, current = openSet.popitem()
					closedSet[self.get_hash(current[ARRAY])] = current
					self.moveCurrent(current, newSet, closedSet)
				openSet = newSet
				continue
			else:
				closedSet[self.get_hash(current[ARRAY])] = current
				openSet.pop(self.get_hash(current[ARRAY]), None)
				self.moveCurrent(current, openSet, closedSet)
				last = current

	def moveCurrent(self, current, openSet, closedSet):
		way = self.possible_move(current)
		for i in range(0, len(way), 1):
			neighbor = [0, 0, 0, 0]
			neighbor[ARRAY] = self.get_node(way[i], current[ARRAY]);

			# print(hex(id(current[ARRAY])), hex(id(neighbor[ARRAY])))

			if self.get_hash(neighbor[ARRAY]) in closedSet:
				continue		# Ignore the neighbor which is already evaluated.

				# The distance from start to a neighbor
			neighbor[DEPTH] = current[DEPTH] + 1
			neighbor[DAD] = current
			neighbor[HEURISTIC] = self.He.get_heuristique_all_map(neighbor[ARRAY])

			if self.get_hash(neighbor[ARRAY]) not in openSet:	# Discover a new node
				openSet[self.get_hash(neighbor[ARRAY])] = neighbor

	def get_hash(self, tab):
		# alltab = self.get_numbers(tab)
		hash = ""
		for elem in tab:
			for oneElem in elem:
				hash += str(oneElem)
		return hash

	# def get_numbers(self, tab):
	# 	alltab = []
	# 	print(tab)
	# 	for elem in tab:
	# 		for oneElem in elem:
	# 			print(oneElem)
	# 			print(alltab)
	# 			alltab.extend(str(elem))
	# 	return alltab

	# def heuristic_cost_estimate(self, start, goal):
	# 	list = self.get_numbers(start)
	# 	list.sort(key=float)
	# 	print(list)

	def gScore_get_lower(self, openSet):
		tmp_val = 999999999
		tmp_key = 0
		for key, value in openSet.items():
			if tmp_val > value[HEURISTIC]:
				tmp_val = value[HEURISTIC]
				tmp_key = key
		return tmp_key

	def possible_move(self, node):
		moves = ["U", "D", "L", "R"]
		index_x = -1
		index_y = -1
		for i in range(0, len(node[ARRAY]), 1):
			if 0 in node[ARRAY][i]:
				index_x = node[ARRAY][i].index(0)
				index_y = i
		if index_y == 0:
			moves.remove("U")
		if index_y == (len(node[ARRAY]) - 1):
			moves.remove("D")
		if index_x == 0:
			moves.remove("L")
		if index_x == (len(node[ARRAY][0]) - 1):
			moves.remove("R")
		return moves

	def get_node(self, move_type, node):
		new_node = copy.deepcopy(node)
		index_x = -1
		index_y = -1
		# print("node: ", node, "\nnew_node: ", new_node)
		# print(hex(id(node)), hex(id(new_node)))

		for i in range(0, len(node), 1):
			if 0 in node[i]:
				index_x = node[i].index(0)
				index_y = i
		if move_type == "U":
			self.Co.switch_up(new_node)
		if move_type == "D":
			self.Co.switch_down(new_node)
		if move_type == "L":
			self.Co.switch_left(new_node)
		if move_type == "R":
			self.Co.switch_right(new_node)
		# print("node2:  ", node, "\nnew_node: ", new_node)
		return new_node
