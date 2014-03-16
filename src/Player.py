# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

# -*- coding: utf-8 -*-

from Character import Character
from PlayerController import PlayerController
import pygame
from Constants import POS_DOWN

PLAYER_SPEED = 0.25
TIME_TO_ROTATE_POS = 50

class Player(Character):
	def __init__(self, x, y, *args):
		Character.__init__(self, x, y, "player-alt.png", -1, "coordPlayerAlt2.txt", [3, 3, 3, 3], (-4, 10, 4, 6, -2, 4, 2, 8))
		self.controller = PlayerController(self)
		self.posIndex = POS_DOWN
		self.posImageIndex = 1

		# Better collisions this way
		self.rect.inflate_ip(-4, -6)
