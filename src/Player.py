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
	def __init__(self, x, y, director):
		Character.__init__(self, x, y, "player-alt.png", -1, "coordPlayerAlt2.txt", [3, 3, 3, 3], (-4, 10, 4, 6, -2, 4, 2, 8))
		self.controller = PlayerController(self, director)
		self.posIndex = POS_DOWN
		self.posImageIndex = 1
		self.hp = 100
		self.atk = 20

		# Better collisions this way
		self.rect.inflate_ip(-4, -6)

	def receive_attack(self, atk):
		self.hp = self.hp - atk;
		print "OUCH!" + str(self.hp)
