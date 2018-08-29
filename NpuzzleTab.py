class NpuzzleTab:
	"""NpuzzleTab class, stock Npuzzle tab"""
	def __init__(self):
		self.linenbr = 0
		self.linenbrmax = 0
		self.list = []
		self.list_2 = []
		self.listsort = []

	def add_full_list(self, list):
		self.list = list
		self.linenbrmax = len(list)
		self.linenbr = len(list)

	def addline(self, line):
		tabline = line.split()
		tabnbr = []
		if not len(tabline) == self.linenbrmax:
			print("Line Nbr invalid : ", line, tabline)
			exit (-1)
		for elem in tabline:
			if not elem.isdigit():
				print("Elem is not a number : {} in line {}", elem, line)
				exit (-1)
			tabnbr.append(int(elem))
		self.list.append(tabnbr)
		self.linenbr += 1

	def addlinemax(self, line):
		if not line.isdigit():
			print("First line must only be a number ", line)
			exit (-1)
		self.linenbrmax = int(line)
		if self.linenbrmax < 3:
			print("less than 3 taquin is not playable ")
			exit (-1)
		if self.linenbrmax >= 100:
			print("Crasy stupids bigs numbers are stupids, try with less than 100")
			exit (-1)

	def printtab(self):
		print("print tab : ")
		for linenbr in self.list:
			for nbr in linenbr:
				print(nbr, end=' ')
			print("")
		print("")
