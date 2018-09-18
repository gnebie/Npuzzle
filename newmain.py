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
	tab = create.gettab()
	option = create.get_options()
	algo = NpuzzleAlgorithm.NpuzzleAlgorithm(tab, option)
	algo.run()
	print(tab.list)
	# print("nbr_coup : ",nbr_coup, "\n ", tab.lines)

if __name__ == '__main__':
	main()
