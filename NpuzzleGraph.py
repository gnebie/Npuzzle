
import time
import pygame
from pygame.locals import *



NPUZZLE_IMAGE_WIDTH = 640
NPUZZLE_IMAGE_HEIGHT = 640
GAME_FRAMS = 60
WAIT_FRAMS = 2
IMG_BACKGROUND = "background.jpg"
IMG_FRONT = "case.jpeg"
# IMG_FRONT = "case.png"
class NpuzzleGraph:
	def __init__(self, list_sort):
		pygame.init()
		self.listsort = []
		for elem in list_sort:
			self.listsort += elem
		self.size = len(list_sort)
		self.bloc_size_width = int(NPUZZLE_IMAGE_WIDTH / self.size)
		self.bloc_size_height = int(NPUZZLE_IMAGE_HEIGHT / self.size)

	def start(self, result, deep):
		result.reverse()
		fenetre = pygame.display.set_mode((NPUZZLE_IMAGE_WIDTH, NPUZZLE_IMAGE_HEIGHT))
		fond = pygame.image.load(IMG_BACKGROUND).convert() # background
		fenetre.blit(fond, (0,0))
		pygame.display.flip()

		#creation des blocks
		bloc_size_width = NPUZZLE_IMAGE_WIDTH / self.size
		bloc_size_height = NPUZZLE_IMAGE_HEIGHT / self.size
		bloc_middle_height = bloc_size_height / 2
		bloc_middle_width = bloc_size_width / 2
		continuer = 1
		game_cases = self.create_game_case()
		wait_fram = int(GAME_FRAMS * 20 / deep)

		titre_fenetre = "Npuzzle"
		pygame.display.set_caption(titre_fenetre)
		pygame.display.flip()
		# time.sleep(10)

		#Boucle infinie
		increm = 0;
		for res_tab in result:
			increm = 0
			while continuer and increm != wait_fram:
				for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
					if event.type == QUIT:     #Si un de ces événements est de type QUIT
						continuer = 0;      #On arrête la boucle
					if event.type == KEYDOWN:
						continuer = 0;      #On arrête la boucle
				pos_line = 0
				pos_col = 0
				increm += 1
				pygame.time.Clock().tick(GAME_FRAMS)
				if (increm == wait_fram):
					fenetre.blit(fond, (0,0))
					for res_line in res_tab[0]:
						i = 0;
						pos_col = 0
						for elem in res_line:
							if (elem != 0):
								print(self.listsort.index(elem))
								fenetre.blit(game_cases[self.listsort.index(elem)], (pos_col, pos_line))
							else:
								pos_0_col = pos_col
								pos_0_line = pos_line
							# print("{} => {}                     {}".format(elem, self.listsort[elem], self.listsort))
							pos_col += bloc_size_width
							i += 1
						pos_line += bloc_size_height
					pygame.display.flip()
					pos_line = 0
		fenetre.blit(game_cases[self.listsort.index(0)], (pos_0_col, pos_0_line))
		pygame.display.flip()
		while continuer:
			for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
				if event.type == QUIT:     #Si un de ces événements est de type QUIT
					continuer = 0;      #On arrête la boucle
				if event.type == KEYDOWN:
					continuer = 0;      #On arrête la boucle


	def create_game_case(self):
		i = 0;
		game_case = []
		img_to_load = pygame.transform.scale(pygame.image.load(IMG_FRONT).convert(), (NPUZZLE_IMAGE_WIDTH, NPUZZLE_IMAGE_HEIGHT))
		pos_line = 0
		pos_col = 0
		while i < self.size * self.size :
			game_case = game_case + [img_to_load.subsurface((pos_col, pos_line, self.bloc_size_width, self.bloc_size_height))]
			i += 1
			if (int(int(i) % int(self.size)) == 0):
				pos_col = 0
				pos_line += self.bloc_size_height
			else:
				pos_col += self.bloc_size_width
		print(i)
		return game_case
