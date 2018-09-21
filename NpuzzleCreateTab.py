import argparse
import random
import NpuzzleTab
import NpuzzleControle

class NpuzzleCreateTab:
	"""NpuzzleTab class, stock Npuzzle tab"""
	def __init__(self):
		args = self.pars_arg()
		self.tab = NpuzzleTab.NpuzzleTab()
		if args.file_name == False:
			self.tab.add_full_list(self.generete_random_table())
		else:
			self.parse_file(args.file_name, self.tab)
		self.args = args
		self.check_tab()

	def gettab(self):
		return self.tab

	def get_options(self):
		return self.args

	def pars_arg(self):
		parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
		parser.add_argument("-f", "--file_name", default=False, help="File name\nif no filename is given, the programme will create a 3 * 3 random table")
		parser.add_argument("-v", "--verbose", action="store_true", default=False, help="Print all the stats of the programme")
		parser.add_argument("-s", "--show", action="store_true", default=False, help="Show the programme running step by step")
		parser.add_argument("-g", "--greedy", action="store_true", default=False, help="be faster by only take the optimum rule")
		parser.add_argument("-e", "--heuristic", type=int, choices=[0, 1, 2],default=0, help="Choose your heuristic: \n\t1 => manhattan \n\t2 => euclide \n\t3 => tchebychev")
		args = parser.parse_args()
		return args

	def generete_random_table(self):
		tab = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
		size_melange = 1000
		random.seed()
		TabControle = NpuzzleControle.NpuzzleControle(3)
		i = 0
		while (i < size_melange):
			j = random.choice([1, 2, 3, 4])
			i += 1
			if (j == 1):
				i += TabControle.switch_up(tab)
			if (j == 2):
				i += TabControle.switch_down(tab)
			if (j == 3):
				i += TabControle.switch_right(tab)
			if (j == 4):
				i += TabControle.switch_left(tab)
		return tab

	def readfile(self, line, tab):
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

	def parse_file(self, file_name, tab):
		try:
			with open(file_name, 'r') as f:
				for line in f:
					self.readfile(line, tab);
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

	def make_goal(self, puzzle_size): # foncton de zaz
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

	def test_tab_resolve_possibility(self, tabinitial, tabfinal):
		paires = 0
		tabfnbr = 0
		for tf in tabfinal:
			tabinbr = 0
			for ti in tabinitial:
				if tf == ti:
					break
				if tabfinal.index(tf) < tabfinal.index(ti):# and tabfinal.index(ti) > tabinitial.index(ti):
					paires += 1
				tabinbr += 1
			tabfnbr += 1
		if(paires & 1):
			print(tabinitial)
			print(tabfinal)
			print("Paires finds : ", paires)
			print("Taquin proposé impossible")
			exit(-1) #pair

	def check_tab(self):
		tab = self.tab
		flat_tab = []
		for elem in tab.list :
			flat_tab.extend(elem)
		if not 0 in flat_tab:
			print("0 not fond  ",  flat_tab)
			exit (-1)
		if len(flat_tab) != len(set(flat_tab)):
			print("duplicates numbers in the tab")
			exit(-1)
		inittab = list(flat_tab[0:])
		tmp_flat_tab = flat_tab[0:]
		new_flat_tab = flat_tab[0:]
		tmp_flat_tab.sort()
		new_nbr = 0
		for nbr in tmp_flat_tab :
			new_flat_tab[flat_tab.index(nbr)] = new_nbr
			new_nbr += 1
		sorttabslist = self.make_goal(tab.linenbrmax)
		self.test_tab_resolve_possibility(new_flat_tab, sorttabslist)
		tab.list_2 = [new_flat_tab[i:i + tab.linenbrmax] for i in range(0, len(new_flat_tab), tab.linenbrmax)]
		tab.listsort = [sorttabslist[i:i + tab.linenbrmax] for i in range(0, len(sorttabslist), tab.linenbrmax)]
