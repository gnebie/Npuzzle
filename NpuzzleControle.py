class NpuzzleControle:
	def __init__(self, tabsize):
		self.tabsize = tabsize
		self.tabmax = tabsize
		self.tabmin = 0

	def switch_left(self, tab):
		nbr = 0
		try:
			for tabline in tab:
				if nbr in tabline:
					index = tabline.index(nbr)
					if tabline.index(nbr) == 0:
						return -1
					if not (tabline[index] == 0 or tabline[index - 1] == 0):
						return -1
					tabline[index], tabline[index - 1] = tabline[index - 1], tabline[index]
					return 0
		except ValueError:
			print("Error ", ValueError)
		return -1

	def switch_right(self, tab):
		nbr = 0
		try:
			for tabline in tab:
				if nbr in tabline:
					index = tabline.index(nbr)
					if tabline.index(nbr) + 1 == len(tabline):
						return -1
					if not (tabline[index] == 0 or tabline[index + 1] == 0):
						return -1
					tabline[index], tabline[index + 1] = tabline[index + 1], tabline[index]
					return 0
		except ValueError:
			print("Error ", ValueError)
		return -1

	def switch_up(self, tab):
		nbr = 0
		try:
			linenbr = 0
			for tabline in tab:
				if nbr in tabline:
					index = tabline.index(nbr)
					if self.tabmin == linenbr:
						return -1
					if not (tab[linenbr][index] == 0 or tab[linenbr - 1][index]):
						return -1
					tab[linenbr][index], tab[linenbr - 1][index] = tab[linenbr - 1][index], tab[linenbr][index]
					return 0
				linenbr += 1
		except ValueError:
			print("Error ", ValueError)
		return -1

	def switch_down(self, tab):
		nbr = 0
		try:
			linenbr = 0
			for tabline in tab:
				linenbr += 1
				if nbr in tabline:
					if self.tabmax <= linenbr:
						return -1
					index = tabline.index(nbr)
					# print (linenbr, "    ", index, "  ", self.tabmax)
					if not (tab[linenbr][index] == 0 or linenbr == 0 or tab[linenbr - 1][index] == 0):
						return -1
					tab[linenbr][index], tab[linenbr - 1][index] = tab[linenbr - 1][index], tab[linenbr][index]
					return 0
		except ValueError:
			print("Error ", ValueError)
		return -1
