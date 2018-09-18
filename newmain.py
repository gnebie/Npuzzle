import sys
from math import sqrt
import time
from unitests import *
import NpuzzleCreateTab
import NpuzzleControle
import NpuzzleHeuristique
import NpuzzleAlgorithm
# import NpuzzleTab


def main():
	create = NpuzzleCreateTab.NpuzzleCreateTab()
	# parse_args(argv, tab)
	# controle = NpuzzleControle(tab.linenbrmax)
	# check_tab(tab, controle)
	# result = False
	# nbr_coup = [0]
	# print(tab)
	# i = 0
	# while not result:
	# 	result = controle.get_closer_to_this_numbre(tab.lines, tab.listsort, nbr_coup, i)
	# 	i += 1
	tab = create.gettab()
	option = create.get_options()
	algo = NpuzzleAlgorithm.NpuzzleAlgorithm(tab, option)
	algo.run()
	print(tab.list)
	# print("nbr_coup : ",nbr_coup, "\n ", tab.lines)

if __name__ == '__main__':
	main()
