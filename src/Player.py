# -*- coding: utf-8 -*-

'''
Created on 03/03/2014

@author: DaGal
'''

# -*- coding: utf-8 -*-

from Character import Character
import pygame
from PlayerController import PlayerController

class Player(Character):
	def __init__(self, x, y, *args):
		Character.__init__(self, x, y)
		self.controller = PlayerController(self)
		self.rect = pygame.Rect(x, y, 10, 10)
