import NpuzzleControle
import NpuzzleHeuristique
import NpuzzleInfosAlgorithm
import NpuzzleAstar

def copydbllist(lst):
	newlst = []
	for l in lst:
		newlst.append(list(l))
	return newlst

class NpuzzleAlgorithm:
	def __init__(self, tab):
		self.He = NpuzzleHeuristique.NpuzzleHeuristique(tab)
		self.Co = NpuzzleControle.NpuzzleControle(tab.linenbrmax)
		self.Tab = tab
		# self.Info = NpuzzleInfosAlgorithm.NpuzzleInfosAlgorithm()

	def run(self):
		# print(self.He.check_walls(self.Tab.list_2))
		# print(self.He.check_walls(self.Tab.list_2))
		# print(self.He.check_walls(self.Tab.list_2))
		# self.baby_ago()
		algo = NpuzzleAstar.NpuzzleAstar(self.Tab)
		result = algo.Astar(self.Tab.list_2, self.Tab.listsort)
		for i in result:
			for y in i[0]:
				print(y)
			print('\n')
		# print('result[0]', result[0], '\n')
		# print('result[1]', result[1], '\n')
		# print('result[2]', result[2], '\n')
		# print('result[3]', result[3], '\n')
		# print('result[4]', result[4], '\n')

	def printtab(self, tab):
		print("print tab : ")
		for linenbr in tab:
			for nbr in linenbr:
				print(nbr, end=' ')
			print("")
		print("")


	def baby_ago(self):
		self.Info = NpuzzleInfosAlgorithm.NpuzzleInfosAlgorithm()
		nbr_coup = [ 0 ]
		self.ida_start(self.Tab.list_2, self.Tab.listsort, nbr_coup)

	def chage_tab(self, tab, instructions):
		for instruct in instructions:
			# self.printtab(tab)
			if instruct == "U":
				self.Co.switch_up(tab)
			if instruct == "D":
				self.Co.switch_down(tab)
			if instruct == "R":
				self.Co.switch_right(tab)
			if instruct == "L":
				self.Co.switch_left(tab)
		print(instructions)

	def ida_start(self, tab, tab_ref, nbr_coup):
		profondeur = 1 # a supp, inutile
		profondeur_max = profondeur + 20
		instructions = []
		while profondeur < profondeur_max:
			print("profondeur", profondeur)
			if self.ida(tab, tab_ref, profondeur, 0, instructions) == True:
				print("find in profondeur : ", profondeur)
				instructions.reverse()
				nbr_coup[0] += len(instructions)
				self.chage_tab(tab, instructions)
				self.printtab(tab)
				print("profondeur ", profondeur, " profondeur_max", profondeur_max, " nbr coups ", nbr_coup[0])
				if self.He.get_heuristique_all_map(tab) == 0:
					return True
				instructions = []
				profondeur = 0
			profondeur += 1
		print("Not found in ", profondeur)
		self.printtab(tab)
		return False

	def ida(self, tab, tab_ref, profondeur, last, instructions):
		"""last : 0 begin 1 up 2 down 3 lft 4 right"""
		dist = self.He.get_heuristique_all_map(tab)
		if 0 == profondeur:
			return False
		if (last != 2):
			new_tab_up = copydbllist(tab)
			swup = self.Co.switch_up(new_tab_up)
			if (swup != -1):
				new_dist = self.He.get_heuristique_all_map(new_tab_up)
				if new_dist == 0 or self.He.check_walls(new_tab_up):
					print("end find !!!!!!!! U")
					print(new_tab_up)
					instructions.append("U")
					return True
				if new_dist < dist:
					if self.ida(new_tab_up, tab_ref, profondeur - 1, 1, instructions) == True:
						instructions.append("U")
						return True
					swup = -1
		if (last != 3):
			new_tab_right = copydbllist(tab)
			swrt = self.Co.switch_right(new_tab_right)
			if (swrt != -1):
				new_dist = self.He.get_heuristique_all_map(new_tab_right)
				if new_dist == 0 or self.He.check_walls(new_tab_right):
					print("end find !!!!!!!! R")
					print(new_tab_right)
					instructions.append("R")
					return True
				if new_dist < dist:
					if self.ida(new_tab_right, tab_ref, profondeur - 1, 4, instructions) == True:
						instructions.append("R")
						return True
					swrt = -1
		if (last != 4):
			new_tab_left = copydbllist(tab)
			swlt = self.Co.switch_left(new_tab_left)
			if (swlt != -1):
				new_dist = self.He.get_heuristique_all_map(new_tab_left)
				if new_dist == 0 or self.He.check_walls(new_tab_left):
					print("end find !!!!!!!! L")
					print(new_tab_left)
					instructions.append("L")
					return True
				if new_dist < dist:
					if self.ida(new_tab_left, tab_ref, profondeur - 1, 3, instructions) == True:
						instructions.append("L")
						return True
					swlt = -1
		if (last != 1):
			new_tab_down = copydbllist(tab)
			swdn = self.Co.switch_down(new_tab_down)
			if (swdn != -1):
				new_dist = self.He.get_heuristique_all_map(new_tab_down)
				if new_dist == 0 or self.He.check_walls(new_tab_down):
					print("end find !!!!!!!! D")
					print(new_tab_down)
					instructions.append("D")
					return True
				if new_dist < dist:
					if self.ida(new_tab_down, tab_ref, profondeur - 1, 2, instructions) == True:
						instructions.append("D")
						return True
					swdn = -1
		if last != 2 and swup != -1 and self.ida(new_tab_up, tab_ref, profondeur - 1, 1, instructions) == True:
			instructions.append("U")
			return True
		if last != 3 and swrt != -1 and self.ida(new_tab_right, tab_ref, profondeur - 1, 4, instructions) == True:
			instructions.append("R")
			return True
		if last != 4 and swlt != -1 and self.ida(new_tab_left, tab_ref, profondeur - 1, 3, instructions) == True:
			instructions.append("L")
			return True
		if last != 1 and swdn != -1 and self.ida(new_tab_down, tab_ref, profondeur - 1, 2, instructions) == True:
			instructions.append("D")
			return True
		return False
