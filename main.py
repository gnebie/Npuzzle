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

	def printtab(self, tab):
		print("print tab : ")
		for linenbr in tab:
			for nbr in linenbr:
				print(nbr, end=' ')
			print("")
		print("")

	def next_diff_indexnbr(self, tab1, tab2):
		""" Tupples return : (nbr, y_value_tab, x_value_tab)"""
		linenbr = 0
		line_first = []
		for tab1line, tab2line in zip(tab1, tab2):
			nbrnbr = 0
			for tabnbr1, tabnbr2 in zip(tab1line, tab2line):
				if tabnbr1 != tabnbr2:
					if linenbr == self.tabsize - 2:
						line_first = [tabnbr2, linenbr, nbrnbr]
						break
					if (len(line_first) and line_first[2] <= nbrnbr):
						return (line_first[0], line_first[1], line_first[2])
					return (tabnbr2, linenbr, nbrnbr)
				nbrnbr += 1
			linenbr += 1
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

# ???

	def get_closer_to_this_numbre(self, tab, tab_ref, nbr_coup):
		nbr_target = self.next_diff_indexnbr(tab, tab_ref)
		if (nbr_target[0] == 0):
			print("lite triée")
			self.printtab(tab)
			return True
		nbr = self.get_indexnbr(nbr_target[0], tab)
		nbr_0 = self.get_indexnbr(0, tab) # toujours avoir 0 de stocke et le modifer quand on bouge ??
		print("tab test begin ")
		while self.manhattan_distance(nbr, nbr_0) > 1:
			nbr_coup[0] += 1
			# self.printtab(tab)
			# print("debug : MD ", self.manhattan_distance(nbr, nbr_0), "  nbr_0 ", nbr_0, " nbr ", nbr )
			if (nbr[1] > nbr_0[1]): # au dessous
				# print("D")
				self.switch_down(tab)
			elif (nbr[2] > nbr_0[2]): # a droite
				# print("R")
				self.switch_right(tab)
			elif (nbr[2] < nbr_0[2]): # a gauche
				# print("L")
				self.switch_left(tab)
			elif (nbr[1] < nbr_0[1]): # au dessus
				# print("U")
				self.switch_up(tab)
			else:
				print("error get_closer_to_this_numbre ", nbr, nbr_0)
				exit (-1)
			self.printtab(tab)
			print("tab test ::::::::::: ")
			nbr_0 = self.get_indexnbr(0, tab);
			# time.sleep(1)
		# self.printtab(tab)
		print("debug : MD ", self.manhattan_distance(nbr, nbr_0), "  nbr_0 ", nbr_0, " nbr ", nbr )
		if self.ida_start(tab, tab_ref, nbr_target, nbr_coup) == False:
			exit (-1)
		return False

	def chage_tab(self, tab, instructions):
		for instruct in instructions:
			if instruct == "U":
				self.switch_up(tab)
			if instruct == "D":
				self.switch_down(tab)
			if instruct == "R":
				self.switch_right(tab)
			if instruct == "L":
				self.switch_left(tab)
			print("change tab : ", instruct)
			self.printtab(tab)

	def ida_start(self, tab, tab_ref, nbr_target, nbr_coup):
		# nbr_target = self.next_diff_indexnbr(tab, tab_ref)
		# if (nbr_target == 0):
			# print("lite triée")
			# return
		nbr = self.get_indexnbr(nbr_target[0], tab)
		nbr_0 = self.get_indexnbr(0, tab) # toujours avoir 0 de stocke et le modifer quand on bouge ??
		profondeur = 20 # a supp, inutile
		instructions = []
		# print("test pour le nombre ", nbr)
		while profondeur < 21:
			if self.ida(tab, tab_ref, profondeur, nbr_target, 0, instructions) == True:
				# print("find in profondeur : ", profondeur)
				instructions.reverse()
				# print("nombre de coups : ", len(instructions), "nombre de coups total: ", nbr_coup)
				nbr_coup[0] += len(instructions)
				self.chage_tab(tab, instructions)
				self.printtab(tab)
				time.sleep(1)
				return True;
			profondeur += 1
		print("not find in profondeur : ", profondeur - 1)
		return False

	def ida(self, tab, tab_ref, profondeur, nbr_target, last, instructions):
		"""last : 0 begin 1 up 2 down 3 lft 4 right"""
		nbr = self.get_indexnbr(nbr_target[0], tab)
		dist = self.heurisique(nbr, nbr_target)
		# print("action ", last, " profondeur ", profondeur, " dist ", dist)
		# self.printtab(tab)
		# time.sleep(1)
		if 0 == profondeur: # a supp
			if dist == 0:
				return True
			else:
				return False

		if (last != 1):
			new_tab_down = copydbllist(tab)
			swdn = self.switch_down(new_tab_down)
			if (swdn != -1):
				nbr = self.get_indexnbr(nbr_target[0], new_tab_down)
				new_dist = self.heurisique(nbr, nbr_target)
				if new_dist == 0:
					instructions.append("D")
					return True
				if new_dist > dist:
					swdn = -1
				if new_dist < dist:
					if self.ida(new_tab_down, tab_ref, profondeur - 1, nbr_target, 2, instructions) == True:
						instructions.append("D")
						return True
					return False

		if (last != 3):
			new_tab_right = copydbllist(tab)
			swrt = self.switch_right(new_tab_right)
			if (swrt != -1):
				nbr = self.get_indexnbr(nbr_target[0], new_tab_right)
				new_dist = self.heurisique(nbr, nbr_target)
				if new_dist == 0:
					instructions.append("R")
					return True
				if new_dist > dist:
					swrt = -1
				if new_dist < dist:
					if self.ida(new_tab_right, tab_ref, profondeur - 1, nbr_target, 4, instructions) == True:
						instructions.append("R")
						return True
					return False

		if (last != 4):
			new_tab_left = copydbllist(tab)
			swlt = self.switch_left(new_tab_left)
			if (swlt != -1):
				nbr = self.get_indexnbr(nbr_target[0], new_tab_left)
				new_dist = self.heurisique(nbr, nbr_target)
				if new_dist == 0:
					instructions.append("L")
					return True
				if new_dist > dist:
					swlt = -1
				if new_dist < dist:
					if self.ida(new_tab_left, tab_ref, profondeur - 1, nbr_target, 3, instructions) == True:
						instructions.append("L")
						return True
					return False

		if (last != 2):
			new_tab_up = copydbllist(tab)
			swup = self.switch_up(new_tab_up)
			if (swup != -1):
				nbr = self.get_indexnbr(nbr_target[0], new_tab_up)
				new_dist = self.heurisique(nbr, nbr_target)
				if new_dist == 0:
					instructions.append("U")
					return True
				if new_dist > dist:
					swup = -1
				if new_dist < dist:
					if self.ida(new_tab_up, tab_ref, profondeur - 1, nbr_target, 1, instructions) == True:
						instructions.append("U")
						return True
					return False

		if last != 1 and swdn != -1 and self.ida(new_tab_down, tab_ref, profondeur - 1, nbr_target, 2, instructions) == True:
			instructions.append("D")
			return True
		if last != 3 and swrt != -1 and self.ida(new_tab_right, tab_ref, profondeur - 1, nbr_target, 4, instructions) == True:
			instructions.append("R")
			return True
		if last != 2 and swup != -1 and self.ida(new_tab_up, tab_ref, profondeur - 1, nbr_target, 1, instructions) == True:
			instructions.append("U")
			return True
		if last != 4 and swlt != -1 and self.ida(new_tab_left, tab_ref, profondeur - 1, nbr_target, 3, instructions) == True:
			instructions.append("L")
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
					if 0 == linenbr:
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
					if self.tabsize == linenbr:
						return -1
					index = tabline.index(nbr)
					if not (tab[linenbr][index] == 0 or tab[linenbr - 1][index] == 0):
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
	# print("find : ", paires)
	if(paires & 1):
		print("Taquin proposé impossible")
		exit(-1) #impair
	# else
	# pair

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
	alltab = alltab[1:len(alltab)] + alltab[0:1]
	sorttabslist = [alltab[i:i + tab.linenbrmax] for i in range(0, len(alltab), tab.linenbrmax)]
	test_tab_resolve_possibility(inittab, alltab)
	tab.listsort = sorttabslist

def main(argv):
	tab = NpuzzleTab()
	parse_args(argv, tab)
	controle = NpuzzleControle(tab.linenbrmax)
	check_tab(tab, controle)
	result = False
	nbr_coup = [0]
	while not result:
		result = controle.get_closer_to_this_numbre(tab.lines, tab.listsort, nbr_coup)

	print(tab.lines)
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
