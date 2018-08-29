import sys
from math import sqrt
import time
from unitests import *

def copydbllist(lst):
	newlst = []
	for l in lst:
		newlst.append(list(l))
	return newlst

class NpuzzleControle:
	def __init__(self, tabsize):
		self.tabsize = tabsize
		self.tabmax = tabsize
		self.tabmin = 0

	def printtab(self, tab):
		print("print tab : ")
		for linenbr in tab:
			for nbr in linenbr:
				print(nbr, end=' ')
			print("")
		print("")

	def next_diff_indexnbr(self, origintab1, orgintab2):
		""" Tupples return : (nbr, y_value_tab, x_value_tab)"""
		tab1 = copydbllist(origintab1)
		tab2 = copydbllist(orgintab2)
		tab1.reverse()
		tab2.reverse()
		linenbr = self.tabsize
		line_first = []
		for tab1line, tab2line in zip(tab1, tab2):
			linenbr -= 1
			nbrnbr = self.tabsize
			tab1line.reverse()
			tab2line.reverse()
			for tabnbr1, tabnbr2 in zip(tab1line, tab2line):
				nbrnbr -= 1
				if tabnbr1 != tabnbr2:
					if linenbr == 1:
						line_first = [tabnbr2, linenbr, nbrnbr]
						break
					if (len(line_first) and line_first[2] < nbrnbr):
						return (line_first[0], line_first[1], line_first[2])
					return (tabnbr2, linenbr, nbrnbr)
		if len(line_first):
			return (line_first[0], line_first[1], line_first[2])
		return (0, -1, -1) # list sort

# a sortir de controle ???

# heuristiques
	def manhattan_distance(self, tup1, tup2):
		dist = abs(tup1[1] - tup2[1]) + abs(tup1[2] - tup2[2])
		return (dist)

	def euclide_distance(self, tup1, tup2):
		dist = sqrt((tup1[1] - tup2[1])**2 + (tup1[2] - tup2[2])**2)
		return (dist)

	def tchebychev_distance(self, tup1, tup2):
		dist = max(abs(tup1[1] - tup2[1]), abs(tup1[2] - tup2[2]))

	def heurisique(self, tup1, tup2):
		return self.manhattan_distance(tup1, tup2)
		# return self.euclide_distance(tup1, tup2)
		# return self.tchebychev_distance(tup1, tup2)

	def get_heuristique_all_map(self, tab, tab_ref):
		manhattan_distance = 0;
		for tab_line in tab:
			for tabnbr1 in tab_line:
				if (tabnbr1 == 0):
					continue ;
				dist1 = self.get_indexnbr(tabnbr1, tab)
				dist2 = self.get_indexnbr(tabnbr1, tab_ref)
				manhattan_distance += self.heurisique_distance(dist1, dist2)
		return manhattan_distance

	def check_step(self, tab, tab_ref, step):
		tab1 = copydbllist(tab)
		tab2 = copydbllist(tab_ref)
		tab1.reverse()
		tab2.reverse()
		lingne_trie = 0
		if self.tabsize < step + 2:
			return False
		for tab1line, tab2line in zip(tab1, tab2):
			lingne_trie += 1
			for tabnbr1, tabnbr2 in zip(tab1line, tab2line):
				if (tabnbr1 != tabnbr2):
					if lingne_trie <= step:
						return False
					return True
		return True

	def index_target(self, tab, tab_ref):
		nbr_target = self.next_diff_indexnbr(tab, tab_ref)
		if (nbr_target[0] == 0):
			return nbr_target;
		print(nbr_target)
		print(tab)
		print("tab size ", self.tabsize)
		time.sleep(1)
		if (nbr_target[1] <= 1): # si on est sur la ligne - 1
			# new_target = nbr_target
			if (nbr_target[2] <= 1):
				new_target = nbr_target
			elif (nbr_target[1] == 1 and tab[nbr_target[1]][nbr_target[2] - 1] == tab_ref[nbr_target[1]][nbr_target[2]] and tab[nbr_target[1]][nbr_target[2]] == tab_ref[nbr_target[1] - 1][nbr_target[2]]) or (tab[nbr_target[1] - 1][nbr_target[2]] == tab_ref[nbr_target[1]][nbr_target[2]] and tab[nbr_target[1]][nbr_target[2]] == tab_ref[nbr_target[1]][nbr_target[2] - 1]):
				print("test ___________________________________")
				new_target = nbr_target
			elif nbr_target[1] == 1 and tab[nbr_target[1]][nbr_target[2] - 1] == tab_ref[nbr_target[1]][nbr_target[2]] and (tab_ref[nbr_target[1] - 1][nbr_target[2]] == tab[nbr_target[1] - 1][nbr_target[2]]):
				new_target = (tab_ref[nbr_target[1] - 1][nbr_target[2]],nbr_target[1] - 1, nbr_target[2] - 2)
			else :
				new_target = nbr_target
			# if tab[nbr_target[1 - 1]][nbr_target[2]] == tab_ref[nbr_target[1] - 1][nbr_target[2]] or tab[nbr_target[1]][nbr_target[2] - 1] == tab_ref[nbr_target[1] - 1][nbr_target[2]]:
			# 	new_target = (tab_ref[nbr_target[1] - 1][nbr_target[2]], nbr_target[1], nbr_target[2] - 1)
			print(new_target)
			return new_target
		elif nbr_target[2] < 2 and nbr_target[1] == self.tabsize - 1:
			print("rentréeeee ___________________________________")
			if nbr_target[2] == 0 and tab[nbr_target[1]][1] == tab_ref[nbr_target[1]][1] and tab[nbr_target[1] - 1][0] != tab_ref[nbr_target[1]][0]:
				return (tab_ref[nbr_target[1]][1], nbr_target[1], 0)
			if nbr_target[2] == 1 and tab[nbr_target[1]][0] == tab_ref[nbr_target[1]][1] and tab[nbr_target[1] - 1][0] == tab_ref[nbr_target[1]][0]:
				return nbr_target
			elif nbr_target[2] == 1 and (tab[nbr_target[1]][0] == tab_ref[nbr_target[1]][0] or tab[nbr_target[1] - 1][0] == tab_ref[nbr_target[1]][0]):
				new_target = (tab_ref[nbr_target[1]][0], nbr_target[1] - 2, nbr_target[2])
				print(new_target)
				return new_target
			elif nbr_target[2] == 1 and tab_ref[nbr_target[1]][1] != tab[nbr_target[1]][0]:
				return (nbr_target[0], nbr_target[1], 0)
			elif nbr_target[2] == 1 and tab_ref[nbr_target[1]][0] != tab[nbr_target[1] - 1][0]:
				return (tab_ref[nbr_target[1]][0], nbr_target[1] - 1, 0)
		return nbr_target

# ???
	# besoin exception pour les deux dernieres lignes
	def get_closer_to_this_numbre(self, tab, tab_ref, nbr_coup, nbr_target):
		if self.ida_start(tab, tab_ref, nbr_target, nbr_coup) == False:
			exit (-1)
		# print("debug : MD ", self.manhattan_distance(nbr, nbr_0), "  nbr_0 ", nbr_0, " nbr ", nbr )
		if self.get_heuristique_all_map(tab, tab_ref) == 0:
			return True;
		return False
		nbr_target = self.index_target(tab, tab_ref) # a changer
		print("get heuristique all ", self.get_heuristique_all_map(tab, tab_ref))
		exit (0)
		if (tab == tab_ref or nbr_target[0] == 0): # si liste triée
			print("lite triée")
			# self.printtab(tab)
			return True

		if nbr_target[1] < self.tabsize - 2:
			self.tabmin = nbr_target[1]

		nbr = self.get_indexnbr(nbr_target[0], tab)
		# print(nbr,nbr_target)

### heristique debut
		# if nbr_target[1] >= self.tabsize - 2: # grosse exeption degueux pour gerer la fin
		# 	if nbr_target[1] == self.tabsize - 1 and nbr_target[2] < self.tabsize - 2:
		# 		new_nbr_target = (nbr_target[0], nbr_target[1] - 1, nbr_target[2])
		# 		if new_nbr_target == nbr:
		# 			nbr_target = (tab_ref[new_nbr_target[1]][new_nbr_target[2]], new_nbr_target[1], new_nbr_target[2])
		# 		else :
		# 			nbr_target = new_nbr_target
		# 		nbr = self.get_indexnbr(nbr_target[0], tab)

			# if nbr_target[1] == self.tabsize - 2 and nbr_target[2] < self.tabsize - 2:
			# 	new_nbr_target = (nbr_target[0], nbr_target[1] + 1, nbr_target[2] + 1)
			# 	if new_nbr_target == nbr:
			# 		nbr_target = (tab_ref[nbr_target[1] + 1][nbr_target[2]], nbr_target[1] + 1, nbr_target[2])
			# 		nbr = self.get_indexnbr(nbr_target[0], tab)
			# 		print(nbr,nbr_target, new_nbr_target )
			# 	else :
			# 		nbr_target = new_nbr_target

		# elif (nbr_target[2] == self.tabsize - 2) and nbr == (nbr_target[0], nbr_target[1], nbr_target[2] + 1): # trik pour les fins de lignes
		# 	nbr = self.get_indexnbr(nbr[0] + 1, tab)
		# 	nbr_target = self.get_indexnbr(nbr[0], tab_ref)
### heristique fin


		nbr_0 = self.get_indexnbr(0, tab) # toujours avoir 0 de stocke et le modifer quand on bouge ??
		# print("tab test begin ")
		list = []
		while self.manhattan_distance(nbr, nbr_0) > 1: #amelioration de la recherche du prochain nbr
			# print(list)
			nbr_coup[0] += 1
			if False:
				return False
			elif (nbr[1] < nbr_0[1]): # au dessus
				self.switch_up(tab)
				list.append("U")
			elif (nbr[2] < nbr_0[2]): # a gauche
				self.switch_left(tab)
				list.append("L")
			elif (nbr[1] > nbr_0[1]): # au dessous
				self.switch_down(tab)
				list.append("D")
			elif (nbr[2] > nbr_0[2]): # a droite
				self.switch_right(tab)
				list.append("R")
			else:
				print("error get_closer_to_this_numbre ", nbr, nbr_0)
				exit (-1)
			nbr_0 = self.get_indexnbr(0, tab);
		print("Before : ", list)
		self.printtab(tab)
		# print("debug : MD ", self.manhattan_distance(nbr, nbr_0), "  nbr_0 ", nbr_0, " nbr ", nbr, nbr_target)
		# if nbr_target[1] < self.tabsize - 2 and nbr_target[2] == self.tabsize - 2:
		# if self.ida_start(tab, tab_ref, (nbr_target[0], nbr_target[1], nbr_target[2] + 1), nbr_coup) == False:
			# exit (-1)
		# else :
		if self.ida_start(tab, tab_ref, nbr_target, nbr_coup) == False:
			exit (-1)
		# print("debug : MD ", self.manhattan_distance(nbr, nbr_0), "  nbr_0 ", nbr_0, " nbr ", nbr )
		return False

	def chage_tab(self, tab, instructions):
		# print("change tab : ")
		for instruct in instructions:
			if instruct == "U":
				self.switch_up(tab)
			if instruct == "D":
				self.switch_down(tab)
			if instruct == "R":
				self.switch_right(tab)
			if instruct == "L":
				self.switch_left(tab)
			# print(instruct, end='\n')
			# self.printtab(tab)
		print(instructions)

	def ida_start(self, tab, tab_ref, nbr_target, nbr_coup):
		# nbr_target = self.next_diff_indexnbr(tab, tab_ref)
		# if (nbr_target == 0):
			# print("lite triée")
			# return
		# nbr = self.get_indexnbr(nbr_target[0], tab)
		# nbr_0 = self.get_indexnbr(0, tab) # toujours avoir 0 de stocke et le modifer quand on bouge ??
		profondeur = 40 # a supp, inutile
		profondeur_max = profondeur + 30
		instructions = []
		# print("test pour le nombre ", nbr)
		while profondeur < profondeur_max:
			print("profondeur", profondeur)
			if self.ida(tab, tab_ref, profondeur, nbr_target, 0, instructions) == True:
				print("find in profondeur : ", profondeur)
				instructions.reverse()
				# print("nombre de coups : ", len(instructions), "nombre de coups total: ", nbr_coup)
				nbr_coup[0] += len(instructions)
				self.chage_tab(tab, instructions)
				self.printtab(tab)
				# time.sleep(1)
				# if (self.tabmax > 1):
					# self.tabmax -= 1
				print("profondeur ", profondeur, " profondeur_max", profondeur_max, " nbr : ", nbr_target)
				return True;
			profondeur += 1
		print(nbr_target[0], " not find in profondeur : ", profondeur - 1)
		self.printtab(tab)
		return False

	def test_laststeps(self, tab, new_tab, tab_ref, step):
		if self.tabsize >= step + 2:
			return False
		tab_check1 = tab[0]
		tab_check2 = tab[1]
		new_tab_check1 = new_tab[0]
		new_tab_check2 = new_tab[1]
		tab_ref_check1 = tab_ref[0]
		tab_ref_check2 = tab_ref[1]
		i = 0
		# print("test")
		while i < self.tabsize:
			i += 1
			if new_tab_check1[self.tabsize - i] == tab_ref_check1[self.tabsize - i] and new_tab_check2[self.tabsize - i] == tab_ref_check2[self.tabsize - i] and (tab_check1[self.tabsize - i] != tab_ref_check1[self.tabsize - i] or tab_check2[self.tabsize - i] != tab_ref_check2[self.tabsize - i]):
				print (True, " file true tab ", tab, " tab_ref ", tab_ref, " new_tab ", new_tab, " step ")
				print("i = ", i, "  ", new_tab_check1[self.tabsize - i], tab_ref_check1[self.tabsize - i], " // ", new_tab_check2[self.tabsize - i], tab_ref_check2[self.tabsize - i], "  //  ", tab_check1[self.tabsize - i], "  //  ", tab_check2[self.tabsize - i])
				return True;
			elif new_tab_check1[self.tabsize - i] != tab_ref_check1[self.tabsize - i] or new_tab_check1[self.tabsize - i] != tab_ref_check2[self.tabsize - i]:
				return False
		return False

	def ida(self, tab, tab_ref, profondeur, nbr_target, last, instructions):
		"""last : 0 begin 1 up 2 down 3 lft 4 right"""
		#nbr_target = (nombre, pos_y_du_tab, pos_x_du_tab)
		# nbr = self.get_indexnbr(nbr_target[0], tab)
		# dist = self.heurisique(nbr, nbr_target)
		dist = self.get_heuristique_all_map(tab, tab_ref)
		# print("action ", last, " profondeur ", profondeur, " dist ", dist)
		# self.printtab(tab)
		# time.sleep(1)
		if 0 == profondeur: # a supp
			return False
		if (last != 2):
			new_tab_up = copydbllist(tab)
			swup = self.switch_up(new_tab_up)
			if (swup != -1):
				# nbr = self.get_indexnbr(nbr_target[0], new_tab_up)
				# new_dist = self.heurisique(nbr, nbr_target)
				new_dist = self.get_heuristique_all_map(new_tab_up, tab_ref)
				if new_dist == 0 or self.check_step(new_tab_up, tab_ref, nbr_target):
					instructions.append("U")
					return True
				if new_dist < dist: #self.test_laststeps(tab, new_tab_up, tab_ref, nbr_target) or
					# print(new_tab_up)
					if self.ida(new_tab_up, tab_ref, profondeur - 1, nbr_target, 1, instructions) == True:
						instructions.append("U")
						return True
					swup = -1
				# if new_dist > dist:
				# 	swup = -1



		if (last != 3):
			new_tab_right = copydbllist(tab)
			swrt = self.switch_right(new_tab_right)
			if (swrt != -1):
				# nbr = self.get_indexnbr(nbr_target[0], new_tab_right)
				# new_dist = self.heurisique(nbr, nbr_target)
				new_dist = self.get_heuristique_all_map(new_tab_right, tab_ref)
				if new_dist == 0 or self.check_step(new_tab_right, tab_ref, nbr_target):
					instructions.append("R")
					return True
				if new_dist < dist: #self.test_laststeps(tab, new_tab_right, tab_ref, nbr_target) or
					# print(new_tab_right)
					if self.ida(new_tab_right, tab_ref, profondeur - 1, nbr_target, 4, instructions) == True:
						instructions.append("R")
						return True
					swrt = -1
				# if new_dist > dist:
				# 	swrt = -1

		if (last != 4):
			new_tab_left = copydbllist(tab)
			swlt = self.switch_left(new_tab_left)
			if (swlt != -1):
				# nbr = self.get_indexnbr(nbr_target[0], new_tab_left)
				# new_dist = self.heurisique(nbr, nbr_target)
				new_dist = self.get_heuristique_all_map(new_tab_left, tab_ref)
				if new_dist == 0 or self.check_step(new_tab_left, tab_ref, nbr_target):
					instructions.append("L")
					return True
				if new_dist < dist: #self.test_laststeps(tab, new_tab_left, tab_ref, nbr_target) or
					# print(new_tab_left)
					if self.ida(new_tab_left, tab_ref, profondeur - 1, nbr_target, 3, instructions) == True:
						instructions.append("L")
						return True
					swlt = -1
				# if new_dist > dist:
				# 	swlt = -1

		if (last != 1):
			new_tab_down = copydbllist(tab)
			swdn = self.switch_down(new_tab_down)
			if (swdn != -1):
				# nbr = self.get_indexnbr(nbr_target[0], new_tab_down)
				# new_dist = self.heurisique(nbr, nbr_target)
				new_dist = self.get_heuristique_all_map(new_tab_down, tab_ref)
				if new_dist == 0 or self.check_step(new_tab_down, tab_ref, nbr_target):
					instructions.append("D")
					return True
				if new_dist < dist: #self.test_laststeps(tab, new_tab_down, tab_ref, nbr_target) or
					# print(new_tab_down)
					if self.ida(new_tab_down, tab_ref, profondeur - 1, nbr_target, 2, instructions) == True:
						instructions.append("D")
						return True
					swdn = -1
				# if new_dist > dist:
				# 	swdn = -1


		if last != 2 and swup != -1 and self.ida(new_tab_up, tab_ref, profondeur - 1, nbr_target, 1, instructions) == True:
			instructions.append("U")
			return True
		if last != 3 and swrt != -1 and self.ida(new_tab_right, tab_ref, profondeur - 1, nbr_target, 4, instructions) == True:
			instructions.append("R")
			return True
		if last != 4 and swlt != -1 and self.ida(new_tab_left, tab_ref, profondeur - 1, nbr_target, 3, instructions) == True:
			instructions.append("L")
			return True
		if last != 1 and swdn != -1 and self.ida(new_tab_down, tab_ref, profondeur - 1, nbr_target, 2, instructions) == True:
			instructions.append("D")
			return True

		return False

	def get_indexnbr(self, nbr, tab):
		linenbr = 0
		for tabline in tab:
			if nbr in tabline:
				return (nbr, linenbr, tabline.index(nbr))
			linenbr += 1
		return (nbr, -1, -1)

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

class NpuzzleTab:
	"""NpuzzleTab class, stock Npuzzle tab"""
	def __init__(self):
		self.linenbr = 0
		self.linenbrmax = 0
		self.lines = []
		self.listsort = []

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
		self.lines.append(tabnbr)
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
		for linenbr in self.lines:
			for nbr in linenbr:
				print(nbr, end=' ')
			print("")
		print("")

def readfile(line, tab):
	lineend = line.find("#");
	if lineend != -1:
		line = line[0:lineend]
	else:
		line = line[0:-1]
	if len(line) == 0:
		return
	if tab.linenbrmax != 0:
		tab.addline(line)
	else:
		tab.addlinemax(line)


def test_tab_resolve_possibility(tabinitial, tabfinal):
	paires = 0
	tabfnbr = 0
	for t1 in tabfinal:
		tabinbr = 0
		if t1 == 0:
			continue ;
		for t2 in tabinitial:
			if t1 == t2:
				break
			if t1 < t2 and t2 != 0:
				# print("t1 ", t1, "    t2", t2)
				paires += 1
			tabinbr += 1
		tabfnbr += 1
	return ;
	if(not (paires & 1)):
		print("find : ", paires)
		print("Taquin proposé impossible")
		exit(-1) #pair
	# else
	# impair

def parse_file(argv, tab, i):
	try:
		with open(argv[i], 'r') as f:
			for line in f:
				readfile(line, tab);
				if tab.linenbr > tab.linenbrmax:
					print("To many lines");
					exit (-1)
		f.close();
	except IOError:
		print("Error when file tryed to be open");
		exit(0)
	if not tab.linenbr == tab.linenbrmax:
		print("line nbr invalid");
		exit(-1)

def parse_args(argv, tab):
	# Recuperation des options
	i = 1
	# si utilisation d'un fichier
	parse_file(argv, tab, i)
	return ;
	# sinon aleatoire

def check_tab(tab, controle):
	alltab = []
	for elem in tab.lines :
		alltab.extend(elem)
	if not 0 in alltab:
		print("0 not fond  ",  alltab)
		exit (-1)
	if len(alltab) != len(set(alltab)):
		print("duplicates numbers in the tab")
		exit(-1)
	inittab = list(alltab[0:])
	alltab.sort()
	# alltab = alltab[1:len(alltab)] + alltab[0:1]
	# sorttabslist = [alltab[i:i + tab.linenbrmax] for i in range(0, len(alltab), tab.linenbrmax)]
	# test_tab_resolve_possibility(inittab, alltab)
	sorttabslist = make_goal(tab.linenbrmax)
	sorttabslist = [sorttabslist[i:i + tab.linenbrmax] for i in range(0, len(sorttabslist), tab.linenbrmax)]
	tab.listsort = sorttabslist # ne gere plus les nombre superieur a nbr + 1
	print(tab.listsort)

def make_goal(puzzle_size): # foncton de zaz
	total_case_size = puzzle_size * puzzle_size
	puzzle = [-1 for i in range(total_case_size)]
	case_nbr = 1
	x = 0
	ix = 1
	y = 0
	iy = 0
	while True:
		puzzle[x + y * puzzle_size] = case_nbr
		if case_nbr == 0:
			break
		case_nbr += 1
		if x + ix == puzzle_size or x + ix < 0 or (ix != 0 and puzzle[x + ix + y * puzzle_size] != -1):
			iy = ix
			ix = 0
		elif y + iy == puzzle_size or y + iy < 0 or (iy != 0 and puzzle[x + (y+iy) * puzzle_size] != -1):
			ix = -iy
			iy = 0
		x += ix
		y += iy
		if case_nbr == total_case_size:
			case_nbr = 0

	return puzzle


def main(argv):
	# parser = argparse.ArgumentParser()
	# parser.add_argument("size", type=int, help="Size of the puzzle's side. Must be >3.")
	# parser.add_argument("-s", "--solvable", action="store_true", default=False, help="Forces generation of a solvable puzzle. Overrides -u.")
	# parser.add_argument("-u", "--unsolvable", action="store_true", default=False, help="Forces generation of an unsolvable puzzle")
	# parser.add_argument("-i", "--iterations", type=int, default=10000, help="Number of passes")

	tab = NpuzzleTab()
	parse_args(argv, tab)
	controle = NpuzzleControle(tab.linenbrmax)
	check_tab(tab, controle)
	result = False
	nbr_coup = [0]
	print(tab)
	i = 0
	while not result:
		result = controle.get_closer_to_this_numbre(tab.lines, tab.listsort, nbr_coup, i)
		i += 1

	print("nbr_coup : ",nbr_coup, "\n ", tab.lines)
	# print(tab.lines)
	# print(tab.listsort)
	# print(inittab)
	# print(alltab)
	# test_switch(tab, controle)
	# test_get(tab, controle)
#
	# resolution

if __name__ == '__main__':
	if len(sys.argv) > 1:
		main(sys.argv)
	else:
		print("usage : Main.py [-vitbcp] fichier");
