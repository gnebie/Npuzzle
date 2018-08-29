class NpuzzleHeuristique:
	def __init__(self, tab):
		self.tab_ref = tab.listsort
		self.tab_size = tab.linenbrmax
		self.tab_walls = [[0 for i in range(tab.linenbrmax)] for i in range(tab.linenbrmax)]
		self.option = 0
		print(self.tab_walls)

	def manhattan_distance(self, tup1, tup2):
		dist = abs(tup1[1] - tup2[1]) + abs(tup1[2] - tup2[2])
		return (dist)

	def euclide_distance(self, tup1, tup2):
		dist = sqrt((tup1[1] - tup2[1])**2 + (tup1[2] - tup2[2])**2)
		return (dist)

	def tchebychev_distance(self, tup1, tup2):
		dist = max(abs(tup1[1] - tup2[1]), abs(tup1[2] - tup2[2]))

	def heurisique_distance(self, tup1, tup2):
		if (self.option == 0):
			return self.manhattan_distance(tup1, tup2)
		if (self.option == 1):
			return self.euclide_distance(tup1, tup2)
		if (self.option == 2):
			return self.tchebychev_distance(tup1, tup2)
		return self.manhattan_distance(tup1, tup2)

	def get_heuristique_all_map(self, tab):
		tab_ref = self.tab_ref
		heuristique_distance = 0;
		for tab_line in tab:
			for tabnbr1 in tab_line:
				if (tabnbr1 == 0):
					continue ;
				dist1 = self.get_indexnbr(tabnbr1, tab)
				dist2 = self.get_indexnbr(tabnbr1, tab_ref)
				heuristique_distance += self.heurisique_distance(dist1, dist2)
		return heuristique_distance

	def get_indexnbr(self, nbr, tab):
		linenbr = 0
		for tabline in tab:
			if nbr in tabline:
				return (nbr, linenbr, tabline.index(nbr))
			linenbr += 1
		return (nbr, -1, -1)

	def check_walls(self, tab):
		# if self.tab_walls[0][0] == 1:
		# 	return False
		tab1 = tab
		tab2 = self.tab_ref
		i = 0
		while i < self.tab_size:
			j = 0
			k1 = 0
			k2 = 0
			l1 = 0
			l2 = 0
			while j < self.tab_size:
				if (self.tab_walls[i][j] == 1 and tab1[i][j] != tab2[i][j]) or (self.tab_walls[j][i] == 1 and tab1[j][i] != tab2[j][i]):
					return False
				if tab2[i][j] == 0:
					k1 -= 1000
				if tab2[j][i] == 0:
					k2 -= 1000
				if tab1[i][j] == tab2[i][j]:
					k1 += 1
				if tab1[j][i] == tab2[j][i]:
					k2 += 1
				if tab1[i][j] == tab2[i][j] and self.tab_walls[i][j] == 1:
					l1 += 1
				if tab1[j][i] == tab2[j][i] and self.tab_walls[j][i] == 1:
					l2 += 1
				j += 1
			if k1 != l1 and k1 == self.tab_size and i + 2 < self.tab_size and self.tab_walls[i + 2][j - 1] == 0:
				j = 0
				print(self.tab_walls)
				while j < k1:
					print(self.tab_walls[i])
					self.tab_walls[i][j] = 1
					j += 1
				return True
			if k2 != l2 and k2 == self.tab_size and i + 2 < self.tab_size and self.tab_walls[j - 1][i + 2] == 0:
				j = 0
				while j < k2:
					self.tab_walls[j][i] = 1
					j += 1
				return True
			if (k1 == self.tab_size or k2 == self.tab_size or k1 < 0 or k2 < 0):
				return False
			i += 1
		return False
